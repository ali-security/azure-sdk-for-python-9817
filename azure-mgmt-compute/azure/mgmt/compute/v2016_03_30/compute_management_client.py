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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.availability_sets_operations import AvailabilitySetsOperations
from .operations.virtual_machine_extension_images_operations import VirtualMachineExtensionImagesOperations
from .operations.virtual_machine_extensions_operations import VirtualMachineExtensionsOperations
from .operations.virtual_machines_operations import VirtualMachinesOperations
from .operations.virtual_machine_images_operations import VirtualMachineImagesOperations
from .operations.usage_operations import UsageOperations
from .operations.virtual_machine_sizes_operations import VirtualMachineSizesOperations
from .operations.virtual_machine_scale_sets_operations import VirtualMachineScaleSetsOperations
from .operations.virtual_machine_scale_set_vms_operations import VirtualMachineScaleSetVMsOperations
from . import models


class ComputeManagementClientConfiguration(AzureConfiguration):
    """Configuration for ComputeManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ComputeManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-compute/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ComputeManagementClient(SDKClient):
    """Compute Client

    :ivar config: Configuration for client.
    :vartype config: ComputeManagementClientConfiguration

    :ivar availability_sets: AvailabilitySets operations
    :vartype availability_sets: azure.mgmt.compute.v2016_03_30.operations.AvailabilitySetsOperations
    :ivar virtual_machine_extension_images: VirtualMachineExtensionImages operations
    :vartype virtual_machine_extension_images: azure.mgmt.compute.v2016_03_30.operations.VirtualMachineExtensionImagesOperations
    :ivar virtual_machine_extensions: VirtualMachineExtensions operations
    :vartype virtual_machine_extensions: azure.mgmt.compute.v2016_03_30.operations.VirtualMachineExtensionsOperations
    :ivar virtual_machines: VirtualMachines operations
    :vartype virtual_machines: azure.mgmt.compute.v2016_03_30.operations.VirtualMachinesOperations
    :ivar virtual_machine_images: VirtualMachineImages operations
    :vartype virtual_machine_images: azure.mgmt.compute.v2016_03_30.operations.VirtualMachineImagesOperations
    :ivar usage: Usage operations
    :vartype usage: azure.mgmt.compute.v2016_03_30.operations.UsageOperations
    :ivar virtual_machine_sizes: VirtualMachineSizes operations
    :vartype virtual_machine_sizes: azure.mgmt.compute.v2016_03_30.operations.VirtualMachineSizesOperations
    :ivar virtual_machine_scale_sets: VirtualMachineScaleSets operations
    :vartype virtual_machine_scale_sets: azure.mgmt.compute.v2016_03_30.operations.VirtualMachineScaleSetsOperations
    :ivar virtual_machine_scale_set_vms: VirtualMachineScaleSetVMs operations
    :vartype virtual_machine_scale_set_vms: azure.mgmt.compute.v2016_03_30.operations.VirtualMachineScaleSetVMsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ComputeManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ComputeManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-03-30'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.availability_sets = AvailabilitySetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_extension_images = VirtualMachineExtensionImagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_extensions = VirtualMachineExtensionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machines = VirtualMachinesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_images = VirtualMachineImagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usage = UsageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_scale_sets = VirtualMachineScaleSetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_scale_set_vms = VirtualMachineScaleSetVMsOperations(
            self._client, self.config, self._serialize, self._deserialize)
