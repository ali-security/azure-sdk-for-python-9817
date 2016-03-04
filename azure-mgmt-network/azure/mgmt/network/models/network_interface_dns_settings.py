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


class NetworkInterfaceDnsSettings(Model):
    """
    Dns Settings of a network interface

    :param list dns_servers: Gets or sets list of DNS servers IP addresses
    :param list applied_dns_servers: Gets or sets list of Applied DNS servers
     IP addresses
    :param str internal_dns_name_label: Gets or sets the Internal DNS name
    :param str internal_fqdn: Gets or sets full IDNS name in the form,
     DnsName.VnetId.ZoneId.TopleveSuffix. This is set when the NIC is
     associated to a VM
    """ 

    _attribute_map = {
        'dns_servers': {'key': 'dnsServers', 'type': '[str]'},
        'applied_dns_servers': {'key': 'appliedDnsServers', 'type': '[str]'},
        'internal_dns_name_label': {'key': 'internalDnsNameLabel', 'type': 'str'},
        'internal_fqdn': {'key': 'internalFqdn', 'type': 'str'},
    }

    def __init__(self, dns_servers=None, applied_dns_servers=None, internal_dns_name_label=None, internal_fqdn=None, **kwargs):
        self.dns_servers = dns_servers
        self.applied_dns_servers = applied_dns_servers
        self.internal_dns_name_label = internal_dns_name_label
        self.internal_fqdn = internal_fqdn
