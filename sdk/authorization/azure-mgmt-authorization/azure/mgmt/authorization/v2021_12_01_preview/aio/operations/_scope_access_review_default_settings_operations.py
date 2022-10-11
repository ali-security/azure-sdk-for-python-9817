# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._scope_access_review_default_settings_operations import build_get_request, build_put_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ScopeAccessReviewDefaultSettingsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.v2021_12_01_preview.aio.AuthorizationManagementClient`'s
        :attr:`scope_access_review_default_settings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, scope: str, **kwargs: Any) -> _models.AccessReviewDefaultSettings:
        """Get access review default settings for the subscription.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewDefaultSettings or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewDefaultSettings
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AccessReviewDefaultSettings]

        request = build_get_request(
            scope=scope,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AccessReviewDefaultSettings", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleSettings/default"}  # type: ignore

    @overload
    async def put(
        self,
        scope: str,
        properties: _models.AccessReviewScheduleSettings,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AccessReviewDefaultSettings:
        """Get access review default settings for the subscription.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param properties: Access review schedule settings. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewScheduleSettings
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewDefaultSettings or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewDefaultSettings
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put(
        self, scope: str, properties: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AccessReviewDefaultSettings:
        """Get access review default settings for the subscription.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param properties: Access review schedule settings. Required.
        :type properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewDefaultSettings or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewDefaultSettings
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put(
        self, scope: str, properties: Union[_models.AccessReviewScheduleSettings, IO], **kwargs: Any
    ) -> _models.AccessReviewDefaultSettings:
        """Get access review default settings for the subscription.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param properties: Access review schedule settings. Is either a model type or a IO type.
         Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewScheduleSettings or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewDefaultSettings or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewDefaultSettings
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AccessReviewDefaultSettings]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IO, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "AccessReviewScheduleSettings")

        request = build_put_request(
            scope=scope,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.put.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AccessReviewDefaultSettings", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleSettings/default"}  # type: ignore
