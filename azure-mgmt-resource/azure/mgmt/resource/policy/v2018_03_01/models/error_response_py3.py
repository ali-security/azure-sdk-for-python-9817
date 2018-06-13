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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ErrorResponse(Model):
    """Error reponse indicates Azure Resource Manager is not able to process the
    incoming request. The reason is provided in the error message.

    :param http_status: Http status code.
    :type http_status: str
    :param error_code: Error code.
    :type error_code: str
    :param error_message: Error message indicating why the operation failed.
    :type error_message: str
    """

    _attribute_map = {
        'http_status': {'key': 'httpStatus', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(self, *, http_status: str=None, error_code: str=None, error_message: str=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.http_status = http_status
        self.error_code = error_code
        self.error_message = error_message


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)
