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


class EnvironmentVariable(Model):
    """Environment variable to set within the container.

    :param name: The name of the environment variable.
    :type name: str
    :param value: The value of the environment variable.
    :type value: str
    """

    _validation = {
        'name': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, name, value):
        self.name = name
        self.value = value
