# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from .._serialization import Deserializer, Serializer
from ._configuration import KeyVaultClientConfiguration
from ._operations_mixin import KeyVaultClientOperationsMixin

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class KeyVaultClient(KeyVaultClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """The key vault client performs cryptographic key operations and vault operations against the Key Vault service.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '7.4-preview.1'
    _PROFILE_TAG = "azure.keyvault.KeyVaultClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        api_version: Optional[str] = None,
        profile: KnownProfiles = KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if api_version == '7.2' or api_version == '7.3' or api_version == '7.4-preview.1':
            base_url = '{vaultBaseUrl}'
        else:
            raise ValueError("API version {} is not available".format(api_version))
        self._config = KeyVaultClientConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(KeyVaultClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 7.2: :mod:`v7_2.models<azure.keyvault.v7_2.models>`
           * 7.3: :mod:`v7_3.models<azure.keyvault.v7_3.models>`
           * 7.4-preview.1: :mod:`v7_4_preview_1.models<azure.keyvault.v7_4_preview_1.models>`
        """
        if api_version == '7.2':
            from ..v7_2 import models
            return models
        elif api_version == '7.3':
            from ..v7_3 import models
            return models
        elif api_version == '7.4-preview.1':
            from ..v7_4_preview_1 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def role_assignments(self):
        """Instance depends on the API version:

           * 7.2: :class:`RoleAssignmentsOperations<azure.keyvault.v7_2.aio.operations.RoleAssignmentsOperations>`
           * 7.3: :class:`RoleAssignmentsOperations<azure.keyvault.v7_3.aio.operations.RoleAssignmentsOperations>`
           * 7.4-preview.1: :class:`RoleAssignmentsOperations<azure.keyvault.v7_4_preview_1.aio.operations.RoleAssignmentsOperations>`
        """
        api_version = self._get_api_version('role_assignments')
        if api_version == '7.2':
            from ..v7_2.aio.operations import RoleAssignmentsOperations as OperationClass
        elif api_version == '7.3':
            from ..v7_3.aio.operations import RoleAssignmentsOperations as OperationClass
        elif api_version == '7.4-preview.1':
            from ..v7_4_preview_1.aio.operations import RoleAssignmentsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'role_assignments'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def role_definitions(self):
        """Instance depends on the API version:

           * 7.2: :class:`RoleDefinitionsOperations<azure.keyvault.v7_2.aio.operations.RoleDefinitionsOperations>`
           * 7.3: :class:`RoleDefinitionsOperations<azure.keyvault.v7_3.aio.operations.RoleDefinitionsOperations>`
           * 7.4-preview.1: :class:`RoleDefinitionsOperations<azure.keyvault.v7_4_preview_1.aio.operations.RoleDefinitionsOperations>`
        """
        api_version = self._get_api_version('role_definitions')
        if api_version == '7.2':
            from ..v7_2.aio.operations import RoleDefinitionsOperations as OperationClass
        elif api_version == '7.3':
            from ..v7_3.aio.operations import RoleDefinitionsOperations as OperationClass
        elif api_version == '7.4-preview.1':
            from ..v7_4_preview_1.aio.operations import RoleDefinitionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'role_definitions'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
