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


class EffectiveRoute(SubResource):
    """Effective Route.

    :param id: Resource Id
    :type id: str
    :param user_defined_route: Gets the Id of the effective route. This is
     optional, only user defined routes have the name.
    :type user_defined_route: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param source: Gets who created the route. Possible values include:
     'Unknown', 'User', 'VirtualNetworkGateway', 'Default'
    :type source: str or :class:`EffectiveRouteSource
     <azure.mgmt.network.models.EffectiveRouteSource>`
    :param state: Gets value of effective route. Possible values include:
     'Active', 'Invalid'
    :type state: str or :class:`EffectiveRouteState
     <azure.mgmt.network.models.EffectiveRouteState>`
    :param address_prefix: Gets address prefixes of the effective routes in
     CIDR notation.
    :type address_prefix: list of str
    :param next_hop_ip_address: Gets the IP address of the next hop of the
     effective route
    :type next_hop_ip_address: list of str
    :param next_hop_type: Gets or sets the type of Azure hop the packet
     should be sent to. Possible values include: 'VirtualNetworkGateway',
     'VnetLocal', 'Internet', 'VirtualAppliance', 'None'
    :type next_hop_type: str or :class:`RouteNextHopType
     <azure.mgmt.network.models.RouteNextHopType>`
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'user_defined_route': {'key': 'userDefinedRoute', 'type': 'SubResource'},
        'source': {'key': 'source', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'address_prefix': {'key': 'addressPrefix', 'type': '[str]'},
        'next_hop_ip_address': {'key': 'nextHopIpAddress', 'type': '[str]'},
        'next_hop_type': {'key': 'nextHopType', 'type': 'str'},
    }

    def __init__(self, id=None, user_defined_route=None, source=None, state=None, address_prefix=None, next_hop_ip_address=None, next_hop_type=None):
        super(EffectiveRoute, self).__init__(id=id)
        self.user_defined_route = user_defined_route
        self.source = source
        self.state = state
        self.address_prefix = address_prefix
        self.next_hop_ip_address = next_hop_ip_address
        self.next_hop_type = next_hop_type
