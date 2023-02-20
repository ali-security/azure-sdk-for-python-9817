# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import ComputeManagementClientConfiguration
from .operations import (
    DiskAccessesOperations,
    DiskEncryptionSetsOperations,
    DiskRestorePointOperations,
    DisksOperations,
    GalleriesOperations,
    GalleryApplicationVersionsOperations,
    GalleryApplicationsOperations,
    GalleryImageVersionsOperations,
    GalleryImagesOperations,
    GallerySharingProfileOperations,
    SharedGalleriesOperations,
    SharedGalleryImageVersionsOperations,
    SharedGalleryImagesOperations,
    SnapshotsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class ComputeManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Compute Client.

    :ivar disks: DisksOperations operations
    :vartype disks: azure.mgmt.compute.v2020_09_30.operations.DisksOperations
    :ivar snapshots: SnapshotsOperations operations
    :vartype snapshots: azure.mgmt.compute.v2020_09_30.operations.SnapshotsOperations
    :ivar disk_encryption_sets: DiskEncryptionSetsOperations operations
    :vartype disk_encryption_sets:
     azure.mgmt.compute.v2020_09_30.operations.DiskEncryptionSetsOperations
    :ivar disk_accesses: DiskAccessesOperations operations
    :vartype disk_accesses: azure.mgmt.compute.v2020_09_30.operations.DiskAccessesOperations
    :ivar disk_restore_point: DiskRestorePointOperations operations
    :vartype disk_restore_point:
     azure.mgmt.compute.v2020_09_30.operations.DiskRestorePointOperations
    :ivar galleries: GalleriesOperations operations
    :vartype galleries: azure.mgmt.compute.v2020_09_30.operations.GalleriesOperations
    :ivar gallery_images: GalleryImagesOperations operations
    :vartype gallery_images: azure.mgmt.compute.v2020_09_30.operations.GalleryImagesOperations
    :ivar gallery_image_versions: GalleryImageVersionsOperations operations
    :vartype gallery_image_versions:
     azure.mgmt.compute.v2020_09_30.operations.GalleryImageVersionsOperations
    :ivar gallery_applications: GalleryApplicationsOperations operations
    :vartype gallery_applications:
     azure.mgmt.compute.v2020_09_30.operations.GalleryApplicationsOperations
    :ivar gallery_application_versions: GalleryApplicationVersionsOperations operations
    :vartype gallery_application_versions:
     azure.mgmt.compute.v2020_09_30.operations.GalleryApplicationVersionsOperations
    :ivar gallery_sharing_profile: GallerySharingProfileOperations operations
    :vartype gallery_sharing_profile:
     azure.mgmt.compute.v2020_09_30.operations.GallerySharingProfileOperations
    :ivar shared_galleries: SharedGalleriesOperations operations
    :vartype shared_galleries: azure.mgmt.compute.v2020_09_30.operations.SharedGalleriesOperations
    :ivar shared_gallery_images: SharedGalleryImagesOperations operations
    :vartype shared_gallery_images:
     azure.mgmt.compute.v2020_09_30.operations.SharedGalleryImagesOperations
    :ivar shared_gallery_image_versions: SharedGalleryImageVersionsOperations operations
    :vartype shared_gallery_image_versions:
     azure.mgmt.compute.v2020_09_30.operations.SharedGalleryImageVersionsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2020-09-30". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ComputeManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.disks = DisksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.snapshots = SnapshotsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.disk_encryption_sets = DiskEncryptionSetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.disk_accesses = DiskAccessesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.disk_restore_point = DiskRestorePointOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.galleries = GalleriesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.gallery_images = GalleryImagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.gallery_image_versions = GalleryImageVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.gallery_applications = GalleryApplicationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.gallery_application_versions = GalleryApplicationVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.gallery_sharing_profile = GallerySharingProfileOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.shared_galleries = SharedGalleriesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.shared_gallery_images = SharedGalleryImagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.shared_gallery_image_versions = SharedGalleryImageVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ComputeManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
