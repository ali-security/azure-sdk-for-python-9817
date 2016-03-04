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


class PolicyAssignmentProperties(Model):
    """
    Policy Assignment properties.

    :param str scope: Gets or sets the policy assignment scope.
    :param str display_name: Gets or sets the policy assignment display name.
    :param str policy_definition_id: Gets or sets the policy definition Id.
    """ 

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'policyDefinitionId', 'type': 'str'},
    }

    def __init__(self, scope=None, display_name=None, policy_definition_id=None, **kwargs):
        self.scope = scope
        self.display_name = display_name
        self.policy_definition_id = policy_definition_id
