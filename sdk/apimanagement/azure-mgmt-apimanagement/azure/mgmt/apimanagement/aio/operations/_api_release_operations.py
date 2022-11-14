# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
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
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._api_release_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_entity_tag_request,
    build_get_request,
    build_list_by_service_request,
    build_update_request,
)
from .._vendor import ApiManagementClientMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ApiReleaseOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.apimanagement.aio.ApiManagementClient`'s
        :attr:`api_release` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_service(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.ApiReleaseContract"]:
        """Lists all releases of an API. An API release is created when making an API Revision current.
        Releases are also used to rollback to previous revisions. Results will be paged and can be
        constrained by the $top and $skip parameters.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param filter: |     Field     |     Usage     |     Supported operators     |     Supported
         functions     |</br>|-------------|-------------|-------------|-------------|</br>| notes |
         filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |</br>. Default
         value is None.
        :type filter: str
        :param top: Number of records to return. Default value is None.
        :type top: int
        :param skip: Number of records to skip. Default value is None.
        :type skip: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ApiReleaseContract or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.apimanagement.models.ApiReleaseContract]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2021-08-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ApiReleaseCollection]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_service_request(
                    resource_group_name=resource_group_name,
                    service_name=service_name,
                    api_id=api_id,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    skip=skip,
                    api_version=api_version,
                    template_url=self.list_by_service.metadata["url"],
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
            deserialized = self._deserialize("ApiReleaseCollection", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_service.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases"}  # type: ignore

    @distributed_trace_async
    async def get_entity_tag(
        self, resource_group_name: str, service_name: str, api_id: str, release_id: str, **kwargs: Any
    ) -> bool:
        """Returns the etag of an API release.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param release_id: Release identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type release_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool or the result of cls(response)
        :rtype: bool
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
        )  # type: Literal["2021-08-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_entity_tag_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            release_id=release_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_entity_tag.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        if cls:
            return cls(pipeline_response, None, response_headers)
        return 200 <= response.status_code <= 299

    get_entity_tag.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId}"}  # type: ignore

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, service_name: str, api_id: str, release_id: str, **kwargs: Any
    ) -> _models.ApiReleaseContract:
        """Returns the details of an API release.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param release_id: Release identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type release_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiReleaseContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.ApiReleaseContract
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
        )  # type: Literal["2021-08-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ApiReleaseContract]

        request = build_get_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            release_id=release_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("ApiReleaseContract", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId}"}  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        release_id: str,
        parameters: _models.ApiReleaseContract,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApiReleaseContract:
        """Creates a new Release for the API.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param release_id: Release identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type release_id: str
        :param parameters: Create parameters. Required.
        :type parameters: ~azure.mgmt.apimanagement.models.ApiReleaseContract
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiReleaseContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.ApiReleaseContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        release_id: str,
        parameters: IO,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApiReleaseContract:
        """Creates a new Release for the API.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param release_id: Release identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type release_id: str
        :param parameters: Create parameters. Required.
        :type parameters: IO
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiReleaseContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.ApiReleaseContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        release_id: str,
        parameters: Union[_models.ApiReleaseContract, IO],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ApiReleaseContract:
        """Creates a new Release for the API.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param release_id: Release identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type release_id: str
        :param parameters: Create parameters. Is either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.apimanagement.models.ApiReleaseContract or IO
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiReleaseContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.ApiReleaseContract
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
        )  # type: Literal["2021-08-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ApiReleaseContract]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ApiReleaseContract", is_xml=True)

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            release_id=release_id,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

            deserialized = self._deserialize("ApiReleaseContract", pipeline_response)

        if response.status_code == 201:
            response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

            deserialized = self._deserialize("ApiReleaseContract", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId}"}  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        release_id: str,
        if_match: str,
        parameters: _models.ApiReleaseContract,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApiReleaseContract:
        """Updates the details of the release of the API specified by its identifier.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param release_id: Release identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type release_id: str
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update. Required.
        :type if_match: str
        :param parameters: API Release Update parameters. Required.
        :type parameters: ~azure.mgmt.apimanagement.models.ApiReleaseContract
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiReleaseContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.ApiReleaseContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        release_id: str,
        if_match: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApiReleaseContract:
        """Updates the details of the release of the API specified by its identifier.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param release_id: Release identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type release_id: str
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update. Required.
        :type if_match: str
        :param parameters: API Release Update parameters. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiReleaseContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.ApiReleaseContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        release_id: str,
        if_match: str,
        parameters: Union[_models.ApiReleaseContract, IO],
        **kwargs: Any
    ) -> _models.ApiReleaseContract:
        """Updates the details of the release of the API specified by its identifier.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param release_id: Release identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type release_id: str
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update. Required.
        :type if_match: str
        :param parameters: API Release Update parameters. Is either a model type or a IO type.
         Required.
        :type parameters: ~azure.mgmt.apimanagement.models.ApiReleaseContract or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiReleaseContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.ApiReleaseContract
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
        )  # type: Literal["2021-08-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ApiReleaseContract]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ApiReleaseContract", is_xml=True)

        request = build_update_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            release_id=release_id,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("ApiReleaseContract", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, service_name: str, api_id: str, release_id: str, if_match: str, **kwargs: Any
    ) -> None:
        """Deletes the specified release in the API.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API identifier. Must be unique in the current API Management service instance.
         Required.
        :type api_id: str
        :param release_id: Release identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type release_id: str
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update. Required.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
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
        )  # type: Literal["2021-08-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            release_id=release_id,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId}"}  # type: ignore
