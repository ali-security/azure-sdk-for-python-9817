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


class DomainAvailablilityCheckResult(Model):
    """
    Domain availablility check result

    :param name: Name of the domain
    :type name: str
    :param available: If true then domain can be purchased using CreateDomain
     Api
    :type available: bool
    :param domain_type: Domain type. Possible values include: 'Regular',
     'SoftDeleted'
    :type domain_type: str or :class:`DomainType
     <azure.mgmt.web.models.DomainType>`
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'available': {'key': 'available', 'type': 'bool'},
        'domain_type': {'key': 'domainType', 'type': 'DomainType'},
    }

    def __init__(self, name=None, available=None, domain_type=None):
        self.name = name
        self.available = available
        self.domain_type = domain_type
