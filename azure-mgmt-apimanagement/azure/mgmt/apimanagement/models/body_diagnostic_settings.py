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


class BodyDiagnosticSettings(Model):
    """Body logging settings.

    :param bytes: Number of request body bytes to log.
    :type bytes: int
    """

    _validation = {
        'bytes': {'maximum': 8192},
    }

    _attribute_map = {
        'bytes': {'key': 'bytes', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(BodyDiagnosticSettings, self).__init__(**kwargs)
        self.bytes = kwargs.get('bytes', None)
