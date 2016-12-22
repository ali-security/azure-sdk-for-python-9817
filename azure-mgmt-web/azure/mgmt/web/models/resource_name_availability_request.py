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


class ResourceNameAvailabilityRequest(Model):
    """Resource name availability request content.

    :param name: Resource name to verify.
    :type name: str
    :param type: Resource type used for verification. Possible values include:
     'Site', 'Slot', 'HostingEnvironment'
    :type type: str or :class:`CheckNameResourceTypes
     <azure.mgmt.web.models.CheckNameResourceTypes>`
    :param is_fqdn: Is fully qualified domain name.
    :type is_fqdn: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'is_fqdn': {'key': 'isFqdn', 'type': 'bool'},
    }

    def __init__(self, name=None, type=None, is_fqdn=None):
        self.name = name
        self.type = type
        self.is_fqdn = is_fqdn
