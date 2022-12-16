# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.azurestackhci import AzureStackHCIClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-azurestackhci
# USAGE
    python put_virtual_machine_with_gallery_image.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureStackHCIClient(
        credential=DefaultAzureCredential(),
        subscription_id="fd3c3665-1729-4b7b-9a38-238e83b0f98b",
    )

    response = client.virtualmachines.begin_create_or_update(
        resource_group_name="test-rg",
        virtualmachines_name="test-vm",
        virtualmachines={
            "extendedLocation": {
                "name": "/subscriptions/a95612cb-f1fa-4daa-a4fd-272844fa512c/resourceGroups/dogfoodarc/providers/Microsoft.ExtendedLocation/customLocations/dogfood-location",
                "type": "CustomLocation",
            },
            "location": "West US2",
            "properties": {
                "hardwareProfile": {"vmSize": "Default"},
                "networkProfile": {"networkInterfaces": [{"id": "test-nic"}]},
                "osProfile": {"adminPassword": "password", "adminUsername": "localadmin", "computerName": "luamaster"},
                "securityProfile": {"enableTPM": True, "uefiSettings": {"secureBootEnabled": True}},
                "storageProfile": {
                    "imageReference": {
                        "name": "/subscriptions/a95612cb-f1fa-4daa-a4fd-272844fa512c/resourceGroups/dogfoodarc/providers/Microsoft.AzureStackHCI/galleryimages/test-gallery-image"
                    },
                    "vmConfigContainerName": "Default_Container",
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/preview/2021-09-01-preview/examples/PutVirtualMachineWithGalleryImage.json
if __name__ == "__main__":
    main()
