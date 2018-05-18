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


class EntityNameAvailabilityCheckOutput(Model):
    """The response from the check name availability request.

    All required parameters must be populated in order to send to Azure.

    :param name_available: Required. Specifies if the name is available.
    :type name_available: bool
    :param reason: Specifies the reason if the name is not available.
    :type reason: str
    :param message: Specifies the detailed reason if the name is not
     available.
    :type message: str
    """

    _validation = {
        'name_available': {'required': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EntityNameAvailabilityCheckOutput, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.reason = kwargs.get('reason', None)
        self.message = kwargs.get('message', None)
