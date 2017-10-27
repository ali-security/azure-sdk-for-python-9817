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


class FailoverPolicies(Model):
    """The list of new failover policies for the failover priority change.

    :param failover_policies: List of failover policies.
    :type failover_policies: list[~azure.mgmt.cosmosdb.models.FailoverPolicy]
    """

    _attribute_map = {
        'failover_policies': {'key': 'failoverPolicies', 'type': '[FailoverPolicy]'},
    }

    def __init__(self, failover_policies=None):
        self.failover_policies = failover_policies
