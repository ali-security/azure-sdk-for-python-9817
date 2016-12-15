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


class KeyCredentialsUpdateParameters(Model):
    """Request parameters for a KeyCredentials update operation.

    :param value: A collection of KeyCredentials.
    :type value: list of :class:`KeyCredential
     <azure.graphrbac.models.KeyCredential>`
    """ 

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[KeyCredential]'},
    }

    def __init__(self, value):
        self.value = value
