# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ComputeManagementClientConfiguration
from .operations import DisksOperations
from .operations import SnapshotsOperations
from .operations import DiskEncryptionSetsOperations
from .operations import DiskAccessesOperations
from .operations import DiskRestorePointOperations
from .operations import GalleriesOperations
from .operations import GalleryImagesOperations
from .operations import GalleryImageVersionsOperations
from .operations import GalleryApplicationsOperations
from .operations import GalleryApplicationVersionsOperations
from .operations import GallerySharingProfileOperations
from .operations import SharedGalleriesOperations
from .operations import SharedGalleryImagesOperations
from .operations import SharedGalleryImageVersionsOperations
from .. import models


class ComputeManagementClient(object):
    """Compute Client.

    :ivar disks: DisksOperations operations
    :vartype disks: azure.mgmt.compute.v2020_09_30.aio.operations.DisksOperations
    :ivar snapshots: SnapshotsOperations operations
    :vartype snapshots: azure.mgmt.compute.v2020_09_30.aio.operations.SnapshotsOperations
    :ivar disk_encryption_sets: DiskEncryptionSetsOperations operations
    :vartype disk_encryption_sets: azure.mgmt.compute.v2020_09_30.aio.operations.DiskEncryptionSetsOperations
    :ivar disk_accesses: DiskAccessesOperations operations
    :vartype disk_accesses: azure.mgmt.compute.v2020_09_30.aio.operations.DiskAccessesOperations
    :ivar disk_restore_point: DiskRestorePointOperations operations
    :vartype disk_restore_point: azure.mgmt.compute.v2020_09_30.aio.operations.DiskRestorePointOperations
    :ivar galleries: GalleriesOperations operations
    :vartype galleries: azure.mgmt.compute.v2020_09_30.aio.operations.GalleriesOperations
    :ivar gallery_images: GalleryImagesOperations operations
    :vartype gallery_images: azure.mgmt.compute.v2020_09_30.aio.operations.GalleryImagesOperations
    :ivar gallery_image_versions: GalleryImageVersionsOperations operations
    :vartype gallery_image_versions: azure.mgmt.compute.v2020_09_30.aio.operations.GalleryImageVersionsOperations
    :ivar gallery_applications: GalleryApplicationsOperations operations
    :vartype gallery_applications: azure.mgmt.compute.v2020_09_30.aio.operations.GalleryApplicationsOperations
    :ivar gallery_application_versions: GalleryApplicationVersionsOperations operations
    :vartype gallery_application_versions: azure.mgmt.compute.v2020_09_30.aio.operations.GalleryApplicationVersionsOperations
    :ivar gallery_sharing_profile: GallerySharingProfileOperations operations
    :vartype gallery_sharing_profile: azure.mgmt.compute.v2020_09_30.aio.operations.GallerySharingProfileOperations
    :ivar shared_galleries: SharedGalleriesOperations operations
    :vartype shared_galleries: azure.mgmt.compute.v2020_09_30.aio.operations.SharedGalleriesOperations
    :ivar shared_gallery_images: SharedGalleryImagesOperations operations
    :vartype shared_gallery_images: azure.mgmt.compute.v2020_09_30.aio.operations.SharedGalleryImagesOperations
    :ivar shared_gallery_image_versions: SharedGalleryImageVersionsOperations operations
    :vartype shared_gallery_image_versions: azure.mgmt.compute.v2020_09_30.aio.operations.SharedGalleryImageVersionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ComputeManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.disks = DisksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.snapshots = SnapshotsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.disk_encryption_sets = DiskEncryptionSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.disk_accesses = DiskAccessesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.disk_restore_point = DiskRestorePointOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.galleries = GalleriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_images = GalleryImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_image_versions = GalleryImageVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_applications = GalleryApplicationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_application_versions = GalleryApplicationVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_sharing_profile = GallerySharingProfileOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.shared_galleries = SharedGalleriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.shared_gallery_images = SharedGalleryImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.shared_gallery_image_versions = SharedGalleryImageVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ComputeManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
