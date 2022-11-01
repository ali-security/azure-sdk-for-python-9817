# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._provider_share_subscriptions_operations import (
    build_adjust_request,
    build_get_by_share_request,
    build_list_by_share_request,
    build_reinstate_request,
    build_revoke_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ProviderShareSubscriptionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.datashare.aio.DataShareManagementClient`'s
        :attr:`provider_share_subscriptions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def adjust(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        provider_share_subscription_id: str,
        provider_share_subscription: _models.ProviderShareSubscription,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ProviderShareSubscription:
        """Adjust the expiration date of a share subscription in a provider share.

        Adjust a share subscription's expiration date in a provider share.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param account_name: The name of the share account. Required.
        :type account_name: str
        :param share_name: The name of the share. Required.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription. Required.
        :type provider_share_subscription_id: str
        :param provider_share_subscription: The provider share subscription. Required.
        :type provider_share_subscription: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscription or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def adjust(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        provider_share_subscription_id: str,
        provider_share_subscription: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ProviderShareSubscription:
        """Adjust the expiration date of a share subscription in a provider share.

        Adjust a share subscription's expiration date in a provider share.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param account_name: The name of the share account. Required.
        :type account_name: str
        :param share_name: The name of the share. Required.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription. Required.
        :type provider_share_subscription_id: str
        :param provider_share_subscription: The provider share subscription. Required.
        :type provider_share_subscription: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscription or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def adjust(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        provider_share_subscription_id: str,
        provider_share_subscription: Union[_models.ProviderShareSubscription, IO],
        **kwargs: Any
    ) -> _models.ProviderShareSubscription:
        """Adjust the expiration date of a share subscription in a provider share.

        Adjust a share subscription's expiration date in a provider share.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param account_name: The name of the share account. Required.
        :type account_name: str
        :param share_name: The name of the share. Required.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription. Required.
        :type provider_share_subscription_id: str
        :param provider_share_subscription: The provider share subscription. Is either a model type or
         a IO type. Required.
        :type provider_share_subscription: ~azure.mgmt.datashare.models.ProviderShareSubscription or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscription or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-09-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ProviderShareSubscription]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(provider_share_subscription, (IO, bytes)):
            _content = provider_share_subscription
        else:
            _json = self._serialize.body(provider_share_subscription, "ProviderShareSubscription")

        request = build_adjust_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            provider_share_subscription_id=provider_share_subscription_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.adjust.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DataShareError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ProviderShareSubscription", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    adjust.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/adjust"}  # type: ignore

    @overload
    async def reinstate(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        provider_share_subscription_id: str,
        provider_share_subscription: _models.ProviderShareSubscription,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ProviderShareSubscription:
        """Reinstate share subscription in a provider share.

        Reinstate share subscription in a provider share.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param account_name: The name of the share account. Required.
        :type account_name: str
        :param share_name: The name of the share. Required.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription. Required.
        :type provider_share_subscription_id: str
        :param provider_share_subscription: The provider share subscription. Required.
        :type provider_share_subscription: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscription or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def reinstate(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        provider_share_subscription_id: str,
        provider_share_subscription: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ProviderShareSubscription:
        """Reinstate share subscription in a provider share.

        Reinstate share subscription in a provider share.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param account_name: The name of the share account. Required.
        :type account_name: str
        :param share_name: The name of the share. Required.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription. Required.
        :type provider_share_subscription_id: str
        :param provider_share_subscription: The provider share subscription. Required.
        :type provider_share_subscription: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscription or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def reinstate(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        provider_share_subscription_id: str,
        provider_share_subscription: Union[_models.ProviderShareSubscription, IO],
        **kwargs: Any
    ) -> _models.ProviderShareSubscription:
        """Reinstate share subscription in a provider share.

        Reinstate share subscription in a provider share.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param account_name: The name of the share account. Required.
        :type account_name: str
        :param share_name: The name of the share. Required.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription. Required.
        :type provider_share_subscription_id: str
        :param provider_share_subscription: The provider share subscription. Is either a model type or
         a IO type. Required.
        :type provider_share_subscription: ~azure.mgmt.datashare.models.ProviderShareSubscription or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscription or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-09-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ProviderShareSubscription]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(provider_share_subscription, (IO, bytes)):
            _content = provider_share_subscription
        else:
            _json = self._serialize.body(provider_share_subscription, "ProviderShareSubscription")

        request = build_reinstate_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            provider_share_subscription_id=provider_share_subscription_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.reinstate.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DataShareError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ProviderShareSubscription", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    reinstate.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/reinstate"}  # type: ignore

    async def _revoke_initial(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        provider_share_subscription_id: str,
        **kwargs: Any
    ) -> _models.ProviderShareSubscription:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-09-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ProviderShareSubscription]

        request = build_revoke_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            provider_share_subscription_id=provider_share_subscription_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._revoke_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DataShareError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ProviderShareSubscription", pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize("ProviderShareSubscription", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _revoke_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/revoke"}  # type: ignore

    @distributed_trace_async
    async def begin_revoke(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        provider_share_subscription_id: str,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ProviderShareSubscription]:
        """Revoke share subscription in a provider share.

        Revoke share subscription in a provider share.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param account_name: The name of the share account. Required.
        :type account_name: str
        :param share_name: The name of the share. Required.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription. Required.
        :type provider_share_subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either ProviderShareSubscription or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.datashare.models.ProviderShareSubscription]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-09-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ProviderShareSubscription]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._revoke_initial(  # type: ignore
                resource_group_name=resource_group_name,
                account_name=account_name,
                share_name=share_name,
                provider_share_subscription_id=provider_share_subscription_id,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("ProviderShareSubscription", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_revoke.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/revoke"}  # type: ignore

    @distributed_trace_async
    async def get_by_share(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        provider_share_subscription_id: str,
        **kwargs: Any
    ) -> _models.ProviderShareSubscription:
        """Get share subscription in a provider share.

        Get share subscription in a provider share.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param account_name: The name of the share account. Required.
        :type account_name: str
        :param share_name: The name of the share. Required.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription. Required.
        :type provider_share_subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscription or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-09-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ProviderShareSubscription]

        request = build_get_by_share_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            provider_share_subscription_id=provider_share_subscription_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_by_share.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DataShareError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ProviderShareSubscription", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_share.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}"}  # type: ignore

    @distributed_trace
    def list_by_share(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.ProviderShareSubscription"]:
        """List of available share subscriptions to a provider share.

        List share subscriptions in a provider share.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param account_name: The name of the share account. Required.
        :type account_name: str
        :param share_name: The name of the share. Required.
        :type share_name: str
        :param skip_token: Continuation Token. Default value is None.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProviderShareSubscription or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.datashare.models.ProviderShareSubscription]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-09-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ProviderShareSubscriptionList]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_share_request(
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    share_name=share_name,
                    subscription_id=self._config.subscription_id,
                    skip_token=skip_token,
                    api_version=api_version,
                    template_url=self.list_by_share.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ProviderShareSubscriptionList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.DataShareError, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_share.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions"}  # type: ignore
