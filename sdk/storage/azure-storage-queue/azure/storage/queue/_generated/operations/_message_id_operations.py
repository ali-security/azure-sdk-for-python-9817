# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Literal, Optional, Type, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_update_request(
    url: str,
    *,
    pop_receipt: str,
    visibilitytimeout: int,
    timeout: Optional[int] = None,
    request_id_parameter: Optional[str] = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    version: Literal["2018-03-28"] = kwargs.pop("version", _headers.pop("x-ms-version", "2018-03-28"))
    accept = _headers.pop("Accept", "application/xml")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}/messages")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["popreceipt"] = _SERIALIZER.query("pop_receipt", pop_receipt, "str")
    _params["visibilitytimeout"] = _SERIALIZER.query(
        "visibilitytimeout", visibilitytimeout, "int", maximum=604800, minimum=0
    )
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int", minimum=0)

    # Construct headers
    _headers["x-ms-version"] = _SERIALIZER.header("version", version, "str")
    if request_id_parameter is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("request_id_parameter", request_id_parameter, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, content=content, **kwargs)


def build_delete_request(
    url: str,
    *,
    pop_receipt: str,
    timeout: Optional[int] = None,
    request_id_parameter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    version: Literal["2018-03-28"] = kwargs.pop("version", _headers.pop("x-ms-version", "2018-03-28"))
    accept = _headers.pop("Accept", "application/xml")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}/messages")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["popreceipt"] = _SERIALIZER.query("pop_receipt", pop_receipt, "str")
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int", minimum=0)

    # Construct headers
    _headers["x-ms-version"] = _SERIALIZER.header("version", version, "str")
    if request_id_parameter is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("request_id_parameter", request_id_parameter, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


class MessageIdOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.queue.AzureQueueStorage`'s
        :attr:`message_id` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def update(  # pylint: disable=inconsistent-return-statements
        self,
        pop_receipt: str,
        visibilitytimeout: int,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        queue_message: Optional[_models.QueueMessage] = None,
        **kwargs: Any
    ) -> None:
        """The Update operation was introduced with version 2011-08-18 of the Queue service API. The
        Update Message operation updates the visibility timeout of a message. You can also use this
        operation to update the contents of a message. A message must be in a format that can be
        included in an XML request with UTF-8 encoding, and the encoded message can be up to 64KB in
        size.

        :param pop_receipt: Required. Specifies the valid pop receipt value returned from an earlier
         call to the Get Messages or Update Message operation. Required.
        :type pop_receipt: str
        :param visibilitytimeout: Optional. Specifies the new visibility timeout value, in seconds,
         relative to server time. The default value is 30 seconds. A specified value must be larger than
         or equal to 1 second, and cannot be larger than 7 days, or larger than 2 hours on REST protocol
         versions prior to version 2011-08-18. The visibility timeout of a message can be set to a value
         later than the expiry time. Required.
        :type visibilitytimeout: int
        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param queue_message: A Message object which can be stored in a Queue. Default value is None.
        :type queue_message: ~azure.storage.queue.models.QueueMessage
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/xml"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        if queue_message is not None:
            _content = self._serialize.body(queue_message, "QueueMessage", is_xml=True)
        else:
            _content = None

        _request = build_update_request(
            url=self._config.url,
            pop_receipt=pop_receipt,
            visibilitytimeout=visibilitytimeout,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["x-ms-popreceipt"] = self._deserialize("str", response.headers.get("x-ms-popreceipt"))
        response_headers["x-ms-time-next-visible"] = self._deserialize(
            "rfc-1123", response.headers.get("x-ms-time-next-visible")
        )

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, pop_receipt: str, timeout: Optional[int] = None, request_id_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """The Delete operation deletes the specified message.

        :param pop_receipt: Required. Specifies the valid pop receipt value returned from an earlier
         call to the Get Messages or Update Message operation. Required.
        :type pop_receipt: str
        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            url=self._config.url,
            pop_receipt=pop_receipt,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore
