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


class InternalError(Model):
    """InternalError.

    :param code:
    :type code: str
    :param message:
    :type message: str
    :param inner_error:
    :type inner_error:
     ~azure.cognitiveservices.language.textanalytics.models.InternalError
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'InternalError'},
    }

    def __init__(self, code=None, message=None, inner_error=None):
        super(InternalError, self).__init__()
        self.code = code
        self.message = message
        self.inner_error = inner_error
