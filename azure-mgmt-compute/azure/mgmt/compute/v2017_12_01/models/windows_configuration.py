# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WindowsConfiguration(Model):
    """Specifies Windows operating system settings on the virtual machine.

    :param provision_vm_agent: Indicates whether virtual machine agent should
     be provisioned on the virtual machine. <br><br> When this property is not
     specified in the request body, default behavior is to set it to true.
     This will ensure that VM Agent is installed on the VM so that extensions
     can be added to the VM later.
    :type provision_vm_agent: bool
    :param enable_automatic_updates: Indicates whether virtual machine is
     enabled for automatic updates.
    :type enable_automatic_updates: bool
    :param time_zone: Specifies the time zone of the virtual machine. e.g.
     "Pacific Standard Time"
    :type time_zone: str
    :param additional_unattend_content: Specifies additional base-64 encoded
     XML formatted information that can be included in the Unattend.xml file,
     which is used by Windows Setup.
    :type additional_unattend_content:
     list[~azure.mgmt.compute.v2017_12_01.models.AdditionalUnattendContent]
    :param win_rm: Specifies the Windows Remote Management listeners. This
     enables remote Windows PowerShell.
    :type win_rm: ~azure.mgmt.compute.v2017_12_01.models.WinRMConfiguration
    """

    _attribute_map = {
        'provision_vm_agent': {'key': 'provisionVMAgent', 'type': 'bool'},
        'enable_automatic_updates': {'key': 'enableAutomaticUpdates', 'type': 'bool'},
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'additional_unattend_content': {'key': 'additionalUnattendContent', 'type': '[AdditionalUnattendContent]'},
        'win_rm': {'key': 'winRM', 'type': 'WinRMConfiguration'},
    }

    def __init__(self, provision_vm_agent=None, enable_automatic_updates=None, time_zone=None, additional_unattend_content=None, win_rm=None):
        self.provision_vm_agent = provision_vm_agent
        self.enable_automatic_updates = enable_automatic_updates
        self.time_zone = time_zone
        self.additional_unattend_content = additional_unattend_content
        self.win_rm = win_rm
