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


class OSProfile(Model):
    """
    Describes an OS profile.

    :param computer_name: Gets or sets the computer name.
    :type computer_name: str
    :param admin_username: Gets or sets the admin user name.
    :type admin_username: str
    :param admin_password: Gets or sets the admin user password.
    :type admin_password: str
    :param custom_data: Gets or sets a base-64 encoded string of custom data.
    :type custom_data: str
    :param windows_configuration: Gets or sets the Windows Configuration of
     the OS profile.
    :type windows_configuration: :class:`WindowsConfiguration
     <azure.mgmt.compute.models.WindowsConfiguration>`
    :param linux_configuration: Gets or sets the Linux Configuration of the
     OS profile.
    :type linux_configuration: :class:`LinuxConfiguration
     <azure.mgmt.compute.models.LinuxConfiguration>`
    :param secrets: Gets or sets the List of certificates for addition to the
     VM.
    :type secrets: list of :class:`VaultSecretGroup
     <azure.mgmt.compute.models.VaultSecretGroup>`
    """ 

    _attribute_map = {
        'computer_name': {'key': 'computerName', 'type': 'str'},
        'admin_username': {'key': 'adminUsername', 'type': 'str'},
        'admin_password': {'key': 'adminPassword', 'type': 'str'},
        'custom_data': {'key': 'customData', 'type': 'str'},
        'windows_configuration': {'key': 'windowsConfiguration', 'type': 'WindowsConfiguration'},
        'linux_configuration': {'key': 'linuxConfiguration', 'type': 'LinuxConfiguration'},
        'secrets': {'key': 'secrets', 'type': '[VaultSecretGroup]'},
    }

    def __init__(self, computer_name=None, admin_username=None, admin_password=None, custom_data=None, windows_configuration=None, linux_configuration=None, secrets=None):
        self.computer_name = computer_name
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.custom_data = custom_data
        self.windows_configuration = windows_configuration
        self.linux_configuration = linux_configuration
        self.secrets = secrets
