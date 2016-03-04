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


class WindowsConfiguration(Model):
    """
    Describes Windows Configuration of the OS Profile.

    :param bool provision_vm_agent: Gets or sets whether VM Agent should be
     provisioned on the Virtual Machine.
    :param bool enable_automatic_updates: Gets or sets whether Windows
     updates are automatically installed on the VM
    :param str time_zone: Gets or sets the Time Zone of the VM
    :param list additional_unattend_content: Gets or sets the additional
     base-64 encoded XML formatted information that can be included in the
     Unattend.xml file.
    :param WinRMConfiguration win_rm: Gets or sets the Windows Remote
     Management configuration of the VM
    """ 

    _attribute_map = {
        'provision_vm_agent': {'key': 'provisionVMAgent', 'type': 'bool'},
        'enable_automatic_updates': {'key': 'enableAutomaticUpdates', 'type': 'bool'},
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'additional_unattend_content': {'key': 'additionalUnattendContent', 'type': '[AdditionalUnattendContent]'},
        'win_rm': {'key': 'winRM', 'type': 'WinRMConfiguration'},
    }

    def __init__(self, provision_vm_agent=None, enable_automatic_updates=None, time_zone=None, additional_unattend_content=None, win_rm=None, **kwargs):
        self.provision_vm_agent = provision_vm_agent
        self.enable_automatic_updates = enable_automatic_updates
        self.time_zone = time_zone
        self.additional_unattend_content = additional_unattend_content
        self.win_rm = win_rm
