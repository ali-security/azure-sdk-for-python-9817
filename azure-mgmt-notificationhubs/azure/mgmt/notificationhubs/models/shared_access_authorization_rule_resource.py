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


class SharedAccessAuthorizationRuleResource(Model):
    """
    Description of a Namespace AuthorizationRules.

    :param id: Gets or sets the id of the created Namespace
     AuthorizationRules.
    :type id: str
    :param location: Gets or sets datacenter location of the Namespace
     AuthorizationRules.
    :type location: str
    :param name: Gets or sets name of the Namespace AuthorizationRules.
    :type name: str
    :param type: Gets or sets resource type of the Namespace
     AuthorizationRules.
    :type type: str
    :param tags: Gets or sets tags of the Namespace AuthorizationRules.
    :type tags: dict
    :param properties: Gets or sets properties of the Namespace.
    :type properties: :class:`SharedAccessAuthorizationRuleProperties
     <azure.mgmt.notificationhubs.models.SharedAccessAuthorizationRuleProperties>`
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'SharedAccessAuthorizationRuleProperties'},
    }

    def __init__(self, id=None, location=None, name=None, type=None, tags=None, properties=None, **kwargs):
        self.id = id
        self.location = location
        self.name = name
        self.type = type
        self.tags = tags
        self.properties = properties
