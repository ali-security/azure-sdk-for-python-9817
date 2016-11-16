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


class Location(Model):
    """A region in which the Azure DocumentDB database account is deployed.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The unique identifier of the region within the database account.
     Example: &lt;accountName&gt;-&lt;locationName&gt;.
    :vartype id: str
    :param location_name: The name of the region.
    :type location_name: str
    :ivar document_endpoint: The connection endpoint for the specific region.
     Example:
     https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
    :vartype document_endpoint: str
    :param provisioning_state:
    :type provisioning_state: str
    :param failover_priority: The failover priority of the region. A failover
     priority of 0 indicates a write region. The maximum value for a failover
     priority = (total number of regions - 1). Failover priority values must be
     unique for each of the regions in which the database account exists.
    :type failover_priority: int
    """ 

    _validation = {
        'id': {'readonly': True},
        'document_endpoint': {'readonly': True},
        'failover_priority': {'minimum': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location_name': {'key': 'locationName', 'type': 'str'},
        'document_endpoint': {'key': 'documentEndpoint', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'failover_priority': {'key': 'failoverPriority', 'type': 'int'},
    }

    def __init__(self, location_name=None, provisioning_state=None, failover_priority=None):
        self.id = None
        self.location_name = location_name
        self.document_endpoint = None
        self.provisioning_state = provisioning_state
        self.failover_priority = failover_priority
