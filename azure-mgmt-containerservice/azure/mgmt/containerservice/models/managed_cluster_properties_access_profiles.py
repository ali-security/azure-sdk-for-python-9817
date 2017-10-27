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


class ManagedClusterPropertiesAccessProfiles(Model):
    """Access profiles for the managed cluster.

    :param cluster_admin: An access profile with administrative privileges to
     the cluster.
    :type cluster_admin: :class:`AccessProfile
     <azure.mgmt.containerservice.models.AccessProfile>`
    :param cluster_user: An access profile with user-level privileges to the
     cluster.
    :type cluster_user: :class:`AccessProfile
     <azure.mgmt.containerservice.models.AccessProfile>`
    """

    _attribute_map = {
        'cluster_admin': {'key': 'clusterAdmin', 'type': 'AccessProfile'},
        'cluster_user': {'key': 'clusterUser', 'type': 'AccessProfile'},
    }

    def __init__(self, cluster_admin=None, cluster_user=None):
        self.cluster_admin = cluster_admin
        self.cluster_user = cluster_user
