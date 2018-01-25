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


class ManagedClusterUpgradeProfile(Model):
    """The list of available upgrades for compute pools.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Id of upgrade profile.
    :vartype id: str
    :ivar name: Name of upgrade profile.
    :vartype name: str
    :ivar type: Type of upgrade profile.
    :vartype type: str
    :param control_plane_profile: The list of available upgrade versions for
     the control plane.
    :type control_plane_profile:
     ~azure.mgmt.containerservice.models.ManagedClusterPoolUpgradeProfile
    :param agent_pool_profiles: The list of available upgrade versions for
     agent pools.
    :type agent_pool_profiles:
     list[~azure.mgmt.containerservice.models.ManagedClusterPoolUpgradeProfile]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'control_plane_profile': {'required': True},
        'agent_pool_profiles': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'control_plane_profile': {'key': 'properties.controlPlaneProfile', 'type': 'ManagedClusterPoolUpgradeProfile'},
        'agent_pool_profiles': {'key': 'properties.agentPoolProfiles', 'type': '[ManagedClusterPoolUpgradeProfile]'},
    }

    def __init__(self, control_plane_profile, agent_pool_profiles):
        super(ManagedClusterUpgradeProfile, self).__init__()
        self.id = None
        self.name = None
        self.type = None
        self.control_plane_profile = control_plane_profile
        self.agent_pool_profiles = agent_pool_profiles
