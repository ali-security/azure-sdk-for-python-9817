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


class AssetStorageEncryptionKey(Model):
    """The Asset Storage encryption key.

    :param storage_encryption_key: The Asset storage encryption key.
    :type storage_encryption_key: str
    """

    _attribute_map = {
        'storage_encryption_key': {'key': 'storageEncryptionKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AssetStorageEncryptionKey, self).__init__(**kwargs)
        self.storage_encryption_key = kwargs.get('storage_encryption_key', None)
