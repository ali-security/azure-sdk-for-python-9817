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


class ManagementGroupChildInfo(Model):
    """The child information of a management group.

    :param child_type: The type of child resource. Possible values include:
     'ManagementGroup', 'Subscription'
    :type child_type: str or ~azure.mgmt.resource.managementgroups.models.enum
    :param child_id: The fully qualified ID for the child resource (management
     group or subscription).  For example,
     /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
    :type child_id: str
    :param display_name: The friendly name of the child resource.
    :type display_name: str
    :param children: The list of children.
    :type children:
     list[~azure.mgmt.resource.managementgroups.models.ManagementGroupChildInfo]
    """

    _attribute_map = {
        'child_type': {'key': 'childType', 'type': 'str'},
        'child_id': {'key': 'childId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'children': {'key': 'children', 'type': '[ManagementGroupChildInfo]'},
    }

    def __init__(self, child_type=None, child_id=None, display_name=None, children=None):
        super(ManagementGroupChildInfo, self).__init__()
        self.child_type = child_type
        self.child_id = child_id
        self.display_name = display_name
        self.children = children
