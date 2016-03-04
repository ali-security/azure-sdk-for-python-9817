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


class DiskEncryptionSettings(Model):
    """
    Describes a Encryption Settings for a Disk

    :param KeyVaultSecretReference disk_encryption_key: Gets or sets the disk
     encryption key which is a KeyVault Secret.
    :param KeyVaultKeyReference key_encryption_key: Gets or sets the key
     encryption key which is KeyVault Key.
    """ 

    _validation = {
        'disk_encryption_key': {'required': True},
    }

    _attribute_map = {
        'disk_encryption_key': {'key': 'diskEncryptionKey', 'type': 'KeyVaultSecretReference'},
        'key_encryption_key': {'key': 'keyEncryptionKey', 'type': 'KeyVaultKeyReference'},
    }

    def __init__(self, disk_encryption_key, key_encryption_key=None, **kwargs):
        self.disk_encryption_key = disk_encryption_key
        self.key_encryption_key = key_encryption_key
