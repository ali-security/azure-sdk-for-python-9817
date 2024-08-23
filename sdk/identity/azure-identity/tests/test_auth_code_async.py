# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from unittest.mock import Mock, patch
from urllib.parse import urlparse

from azure.core.exceptions import ClientAuthenticationError
from azure.core.pipeline.policies import SansIOHTTPPolicy
from azure.identity._constants import EnvironmentVariables
from azure.identity._internal.user_agent import USER_AGENT
from azure.identity.aio import AuthorizationCodeCredential
import msal
import pytest

from helpers import build_aad_response, mock_response, Request
from helpers_async import async_validating_transport, AsyncMockTransport

pytestmark = pytest.mark.asyncio


async def test_no_scopes():
    """The credential should raise ValueError when get_token is called with no scopes"""

    credential = AuthorizationCodeCredential("tenant-id", "client-id", "auth-code", "http://localhost")
    with pytest.raises(ValueError):
        await credential.get_token()


async def test_policies_configurable():
    policy = Mock(spec_set=SansIOHTTPPolicy, on_request=Mock())

    async def send(*_, **kwargs):
        # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to transport
        assert "claims" not in kwargs
        assert "tenant_id" not in kwargs
        return mock_response(json_payload=build_aad_response(access_token="**"))

    credential = AuthorizationCodeCredential(
        "tenant-id", "client-id", "auth-code", "http://localhost", policies=[policy], transport=Mock(send=send)
    )

    await credential.get_token("scope")

    assert policy.on_request.called


async def test_close():
    transport = AsyncMockTransport()
    credential = AuthorizationCodeCredential(
        "tenant-id", "client-id", "auth-code", "http://localhost", transport=transport
    )

    await credential.close()

    assert transport.__aexit__.call_count == 1


async def test_context_manager():
    transport = AsyncMockTransport()
    credential = AuthorizationCodeCredential(
        "tenant-id", "client-id", "auth-code", "http://localhost", transport=transport
    )

    async with credential:
        assert transport.__aenter__.call_count == 1

    assert transport.__aenter__.call_count == 1
    assert transport.__aexit__.call_count == 1


async def test_user_agent():
    transport = async_validating_transport(
        requests=[Request(required_headers={"User-Agent": USER_AGENT})],
        responses=[mock_response(json_payload=build_aad_response(access_token="**"))],
    )

    credential = AuthorizationCodeCredential(
        "tenant-id", "client-id", "auth-code", "http://localhost", transport=transport
    )

    await credential.get_token("scope")


async def test_tenant_id():
    transport = async_validating_transport(
        requests=[Request(required_headers={"User-Agent": USER_AGENT})],
        responses=[mock_response(json_payload=build_aad_response(access_token="**"))],
    )

    credential = AuthorizationCodeCredential(
        "tenant-id",
        "client-id",
        "auth-code",
        "http://localhost",
        transport=transport,
        additionally_allowed_tenants=["*"],
    )

    await credential.get_token("scope", tenant_id="tenant_id")


async def test_auth_code_credential():
    client_id = "client id"
    secret = "fake-client-secret"
    tenant_id = "tenant"
    expected_code = "auth code"
    redirect_uri = "https://localhost"
    expected_access_token = "access"
    expected_refresh_token = "refresh"
    expected_scope = "scope"

    auth_response = build_aad_response(access_token=expected_access_token, refresh_token=expected_refresh_token)
    transport = async_validating_transport(
        requests=[
            Request(  # first call should redeem the auth code
                url_substring=tenant_id,
                required_data={
                    "client_id": client_id,
                    "client_secret": secret,
                    "code": expected_code,
                    "grant_type": "authorization_code",
                    "redirect_uri": redirect_uri,
                    "scope": expected_scope,
                },
            ),
            Request(  # third call should redeem the refresh token
                url_substring=tenant_id,
                required_data={
                    "client_id": client_id,
                    "client_secret": secret,
                    "grant_type": "refresh_token",
                    "refresh_token": expected_refresh_token,
                    "scope": expected_scope,
                },
            ),
        ],
        responses=[mock_response(json_payload=auth_response)] * 2,
    )
    cache = msal.TokenCache()

    credential = AuthorizationCodeCredential(
        client_id=client_id,
        client_secret=secret,
        tenant_id=tenant_id,
        authorization_code=expected_code,
        redirect_uri=redirect_uri,
        transport=transport,
        cache=cache,
    )

    # first call should redeem the auth code
    token = await credential.get_token(expected_scope)
    assert token.token == expected_access_token
    assert transport.send.call_count == 1

    # no auth code -> credential should return cached token
    token = await credential.get_token(expected_scope)
    assert token.token == expected_access_token
    assert transport.send.call_count == 1

    # no auth code, no cached token -> credential should redeem refresh token
    cached_access_token = list(cache.search(cache.CredentialType.ACCESS_TOKEN))[0]
    cache.remove_at(cached_access_token)
    token = await credential.get_token(expected_scope)
    assert token.token == expected_access_token
    assert transport.send.call_count == 2


async def test_multitenant_authentication():
    first_tenant = "first-tenant"
    first_token = "***"
    second_tenant = "second-tenant"
    second_token = first_token * 2

    async def send(request, **kwargs):
        # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to transport
        assert "claims" not in kwargs
        assert "tenant_id" not in kwargs
        parsed = urlparse(request.url)
        tenant = parsed.path.split("/")[1]
        assert tenant in (first_tenant, second_tenant), 'unexpected tenant "{}"'.format(tenant)
        token = first_token if tenant == first_tenant else second_token
        return mock_response(json_payload=build_aad_response(access_token=token, refresh_token="**"))

    credential = AuthorizationCodeCredential(
        first_tenant,
        "client-id",
        "authcode",
        "https://localhost",
        transport=Mock(send=send),
        additionally_allowed_tenants=["*"],
    )
    token = await credential.get_token("scope")
    assert token.token == first_token

    token = await credential.get_token("scope", tenant_id=first_tenant)
    assert token.token == first_token

    token = await credential.get_token("scope", tenant_id=second_tenant)
    assert token.token == second_token

    # should still default to the first tenant
    token = await credential.get_token("scope")
    assert token.token == first_token


async def test_multitenant_authentication_not_allowed():
    expected_tenant = "expected-tenant"
    expected_token = "***"

    async def send(request, **kwargs):
        # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to transport
        assert "claims" not in kwargs
        assert "tenant_id" not in kwargs
        parsed = urlparse(request.url)
        tenant = parsed.path.split("/")[1]
        token = expected_token if tenant == expected_tenant else expected_token * 2
        return mock_response(json_payload=build_aad_response(access_token=token, refresh_token="**"))

    credential = AuthorizationCodeCredential(
        expected_tenant,
        "client-id",
        "authcode",
        "https://localhost",
        transport=Mock(send=send),
        additionally_allowed_tenants=["*"],
    )

    token = await credential.get_token("scope")
    assert token.token == expected_token

    token = await credential.get_token("scope", tenant_id=expected_tenant)
    assert token.token == expected_token

    token = await credential.get_token("scope", tenant_id="un" + expected_tenant)
    assert token.token == expected_token * 2

    with patch.dict("os.environ", {EnvironmentVariables.AZURE_IDENTITY_DISABLE_MULTITENANTAUTH: "true"}):
        token = await credential.get_token("scope", tenant_id="un" + expected_tenant)
        assert token.token == expected_token
