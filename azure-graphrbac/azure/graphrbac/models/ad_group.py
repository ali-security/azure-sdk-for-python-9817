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


class ADGroup(Model):
    """
    Active Directory group information

    :param object_id: Gets or sets object Id
    :type object_id: str
    :param object_type: Gets or sets object type
    :type object_type: str
    :param display_name: Gets or sets group display name
    :type display_name: str
    :param security_enabled: Gets or sets security enabled field
    :type security_enabled: bool
    :param mail: Gets or sets mail field
    :type mail: str
    """ 

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'security_enabled': {'key': 'securityEnabled', 'type': 'bool'},
        'mail': {'key': 'mail', 'type': 'str'},
    }

    def __init__(self, object_id=None, object_type=None, display_name=None, security_enabled=None, mail=None):
        self.object_id = object_id
        self.object_type = object_type
        self.display_name = display_name
        self.security_enabled = security_enabled
        self.mail = mail
