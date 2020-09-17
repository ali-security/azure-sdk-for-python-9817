# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccessUri
    from ._models_py3 import ApiError
    from ._models_py3 import ApiErrorBase
    from ._models_py3 import CreationData
    from ._models_py3 import Disk
    from ._models_py3 import DiskEncryptionSet
    from ._models_py3 import DiskEncryptionSetList
    from ._models_py3 import DiskEncryptionSetUpdate
    from ._models_py3 import DiskList
    from ._models_py3 import DiskSku
    from ._models_py3 import DiskUpdate
    from ._models_py3 import Encryption
    from ._models_py3 import EncryptionSetIdentity
    from ._models_py3 import EncryptionSettingsCollection
    from ._models_py3 import EncryptionSettingsElement
    from ._models_py3 import GrantAccessData
    from ._models_py3 import ImageDiskReference
    from ._models_py3 import InnerError
    from ._models_py3 import KeyVaultAndKeyReference
    from ._models_py3 import KeyVaultAndSecretReference
    from ._models_py3 import Resource
    from ._models_py3 import ShareInfoElement
    from ._models_py3 import Snapshot
    from ._models_py3 import SnapshotList
    from ._models_py3 import SnapshotSku
    from ._models_py3 import SnapshotUpdate
    from ._models_py3 import SourceVault
except (SyntaxError, ImportError):
    from ._models import AccessUri  # type: ignore
    from ._models import ApiError  # type: ignore
    from ._models import ApiErrorBase  # type: ignore
    from ._models import CreationData  # type: ignore
    from ._models import Disk  # type: ignore
    from ._models import DiskEncryptionSet  # type: ignore
    from ._models import DiskEncryptionSetList  # type: ignore
    from ._models import DiskEncryptionSetUpdate  # type: ignore
    from ._models import DiskList  # type: ignore
    from ._models import DiskSku  # type: ignore
    from ._models import DiskUpdate  # type: ignore
    from ._models import Encryption  # type: ignore
    from ._models import EncryptionSetIdentity  # type: ignore
    from ._models import EncryptionSettingsCollection  # type: ignore
    from ._models import EncryptionSettingsElement  # type: ignore
    from ._models import GrantAccessData  # type: ignore
    from ._models import ImageDiskReference  # type: ignore
    from ._models import InnerError  # type: ignore
    from ._models import KeyVaultAndKeyReference  # type: ignore
    from ._models import KeyVaultAndSecretReference  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ShareInfoElement  # type: ignore
    from ._models import Snapshot  # type: ignore
    from ._models import SnapshotList  # type: ignore
    from ._models import SnapshotSku  # type: ignore
    from ._models import SnapshotUpdate  # type: ignore
    from ._models import SourceVault  # type: ignore

from ._compute_management_client_enums import (
    AccessLevel,
    DiskCreateOption,
    DiskEncryptionSetIdentityType,
    DiskState,
    DiskStorageAccountTypes,
    EncryptionType,
    HyperVGeneration,
    OperatingSystemTypes,
    SnapshotStorageAccountTypes,
)

__all__ = [
    'AccessUri',
    'ApiError',
    'ApiErrorBase',
    'CreationData',
    'Disk',
    'DiskEncryptionSet',
    'DiskEncryptionSetList',
    'DiskEncryptionSetUpdate',
    'DiskList',
    'DiskSku',
    'DiskUpdate',
    'Encryption',
    'EncryptionSetIdentity',
    'EncryptionSettingsCollection',
    'EncryptionSettingsElement',
    'GrantAccessData',
    'ImageDiskReference',
    'InnerError',
    'KeyVaultAndKeyReference',
    'KeyVaultAndSecretReference',
    'Resource',
    'ShareInfoElement',
    'Snapshot',
    'SnapshotList',
    'SnapshotSku',
    'SnapshotUpdate',
    'SourceVault',
    'AccessLevel',
    'DiskCreateOption',
    'DiskEncryptionSetIdentityType',
    'DiskState',
    'DiskStorageAccountTypes',
    'EncryptionType',
    'HyperVGeneration',
    'OperatingSystemTypes',
    'SnapshotStorageAccountTypes',
]
