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


class VirtualMachineAgentInstanceView(Model):
    """
    The instance view of the VM Agent running on the virtual machine.

    :param str vm_agent_version: Gets or sets the VM Agent full version.
    :param list extension_handlers: Gets or sets the virtual machine
     extension handler instance view.
    :param list statuses: Gets or sets the resource status information.
    """ 

    _attribute_map = {
        'vm_agent_version': {'key': 'vmAgentVersion', 'type': 'str'},
        'extension_handlers': {'key': 'extensionHandlers', 'type': '[VirtualMachineExtensionHandlerInstanceView]'},
        'statuses': {'key': 'statuses', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, vm_agent_version=None, extension_handlers=None, statuses=None, **kwargs):
        self.vm_agent_version = vm_agent_version
        self.extension_handlers = extension_handlers
        self.statuses = statuses
