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

from msrest.serialization import Model


class ExpressRouteCircuitPeeringConfig(Model):
    """
    Specfies the peering config

    :param list advertised_public_prefixes: Gets or sets the reference of
     AdvertisedPublicPrefixes
    :param str advertised_public_prefixes_state: Gets or sets
     AdvertisedPublicPrefixState of the Peering resource . Possible values
     include: 'NotConfigured', 'Configuring', 'Configured', 'ValidationNeeded'
    :param int customer_asn: Gets or Sets CustomerAsn of the peering.
    :param str routing_registry_name: Gets or Sets RoutingRegistryName of the
     config.
    """

    _required = []

    _attribute_map = {
        'advertised_public_prefixes': {'key': 'advertisedPublicPrefixes', 'type': '[str]'},
        'advertised_public_prefixes_state': {'key': 'advertisedPublicPrefixesState', 'type': 'ExpressRouteCircuitPeeringAdvertisedPublicPrefixState'},
        'customer_asn': {'key': 'customerASN', 'type': 'int'},
        'routing_registry_name': {'key': 'routingRegistryName', 'type': 'str'},
    }

    def __init__(self, advertised_public_prefixes=None, advertised_public_prefixes_state=None, customer_asn=None, routing_registry_name=None):
        self.advertised_public_prefixes = advertised_public_prefixes
        self.advertised_public_prefixes_state = advertised_public_prefixes_state
        self.customer_asn = customer_asn
        self.routing_registry_name = routing_registry_name
