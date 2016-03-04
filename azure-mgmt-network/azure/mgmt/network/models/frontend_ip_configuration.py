# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class FrontendIPConfiguration(SubResource):
    """
    Frontend IP address of the load balancer

    :param str id: Resource Id
    :param list inbound_nat_rules: Read only.Inbound rules URIs that use this
     frontend IP
    :param list inbound_nat_pools: Read only.Inbound pools URIs that use this
     frontend IP
    :param list outbound_nat_rules: Read only.Outbound rules URIs that use
     this frontend IP
    :param list load_balancing_rules: Gets Load Balancing rules URIs that use
     this frontend IP
    :param str private_ip_address: Gets or sets the privateIPAddress of the
     IP Configuration
    :param str private_ip_allocation_method: Gets or sets PrivateIP
     allocation method (Static/Dynamic). Possible values include: 'Static',
     'Dynamic'
    :param Subnet subnet: Gets or sets the reference of the subnet resource
    :param PublicIPAddress public_ip_address: Gets or sets the reference of
     the PublicIP resource
    :param str provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    :param str name: Gets name of the resource that is unique within a
     resource group. This name can be used to access the resource
    :param str etag: A unique read-only string that changes whenever the
     resource is updated
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'inbound_nat_rules': {'key': 'properties.inboundNatRules', 'type': '[SubResource]'},
        'inbound_nat_pools': {'key': 'properties.inboundNatPools', 'type': '[SubResource]'},
        'outbound_nat_rules': {'key': 'properties.outboundNatRules', 'type': '[SubResource]'},
        'load_balancing_rules': {'key': 'properties.loadBalancingRules', 'type': '[SubResource]'},
        'private_ip_address': {'key': 'properties.privateIPAddress', 'type': 'str'},
        'private_ip_allocation_method': {'key': 'properties.privateIPAllocationMethod', 'type': 'IPAllocationMethod'},
        'subnet': {'key': 'properties.subnet', 'type': 'Subnet'},
        'public_ip_address': {'key': 'properties.publicIPAddress', 'type': 'PublicIPAddress'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, inbound_nat_rules=None, inbound_nat_pools=None, outbound_nat_rules=None, load_balancing_rules=None, private_ip_address=None, private_ip_allocation_method=None, subnet=None, public_ip_address=None, provisioning_state=None, name=None, etag=None, **kwargs):
        super(FrontendIPConfiguration, self).__init__(id=id, **kwargs)
        self.inbound_nat_rules = inbound_nat_rules
        self.inbound_nat_pools = inbound_nat_pools
        self.outbound_nat_rules = outbound_nat_rules
        self.load_balancing_rules = load_balancing_rules
        self.private_ip_address = private_ip_address
        self.private_ip_allocation_method = private_ip_allocation_method
        self.subnet = subnet
        self.public_ip_address = public_ip_address
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
