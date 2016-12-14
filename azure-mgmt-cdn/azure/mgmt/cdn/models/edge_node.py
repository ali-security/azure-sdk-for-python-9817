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


class EdgeNode(Model):
    """Edge node of CDN service.

    :param name: Ip adress group that contains Ipv4 and Ipv6 addresses
    :type name: str
    :param resource_group: The resource group of the edge node.
    :type resource_group: str
    :param ip_address_groups: List of ip address groups.
    :type ip_address_groups: list of :class:`IpAddressGroup
     <azure.mgmt.cdn.models.IpAddressGroup>`
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'ip_address_groups': {'key': 'ipAddressGroups', 'type': '[IpAddressGroup]'},
    }

    def __init__(self, name=None, resource_group=None, ip_address_groups=None):
        self.name = name
        self.resource_group = resource_group
        self.ip_address_groups = ip_address_groups
