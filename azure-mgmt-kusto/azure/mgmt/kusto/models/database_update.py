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

from .resource import Resource


class DatabaseUpdate(Resource):
    """Class representing an update to a Kusto database.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: Resource location
    :type location: str
    :ivar provisioning_state: The provisioned state of the resource. Possible
     values include: 'Running', 'Creating', 'Deleting', 'Succeeded', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.kusto.models.ProvisioningState
    :param soft_delete_period_in_days: Required. The number of days data
     should be kept before it stops being accessible to queries.
    :type soft_delete_period_in_days: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'soft_delete_period_in_days': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'soft_delete_period_in_days': {'key': 'properties.softDeletePeriodInDays', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(DatabaseUpdate, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.provisioning_state = None
        self.soft_delete_period_in_days = kwargs.get('soft_delete_period_in_days', None)
