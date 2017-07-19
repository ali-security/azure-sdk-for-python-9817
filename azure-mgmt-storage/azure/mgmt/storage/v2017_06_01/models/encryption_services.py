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


class EncryptionServices(Model):
    """A list of services that support encryption.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param blob: The encryption function of the blob storage service.
    :type blob: :class:`EncryptionService
     <azure.mgmt.storage.v2017_06_01.models.EncryptionService>`
    :param file: The encryption function of the file storage service.
    :type file: :class:`EncryptionService
     <azure.mgmt.storage.v2017_06_01.models.EncryptionService>`
    :ivar table: The encryption function of the table storage service.
    :vartype table: :class:`EncryptionService
     <azure.mgmt.storage.v2017_06_01.models.EncryptionService>`
    :ivar queue: The encryption function of the queue storage service.
    :vartype queue: :class:`EncryptionService
     <azure.mgmt.storage.v2017_06_01.models.EncryptionService>`
    """

    _validation = {
        'table': {'readonly': True},
        'queue': {'readonly': True},
    }

    _attribute_map = {
        'blob': {'key': 'blob', 'type': 'EncryptionService'},
        'file': {'key': 'file', 'type': 'EncryptionService'},
        'table': {'key': 'table', 'type': 'EncryptionService'},
        'queue': {'key': 'queue', 'type': 'EncryptionService'},
    }

    def __init__(self, blob=None, file=None):
        self.blob = blob
        self.file = file
        self.table = None
        self.queue = None
