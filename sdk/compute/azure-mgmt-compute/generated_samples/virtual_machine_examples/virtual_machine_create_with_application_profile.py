# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python virtual_machine_create_with_application_profile.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.virtual_machines.begin_create_or_update(
        resource_group_name="myResourceGroup",
        vm_name="myVM",
        parameters={
            "location": "westus",
            "properties": {
                "applicationProfile": {
                    "galleryApplications": [
                        {
                            "configurationReference": "https://mystorageaccount.blob.core.windows.net/configurations/settings.config",
                            "enableAutomaticUpgrade": False,
                            "order": 1,
                            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdb/resourceGroups/myresourceGroupName2/providers/Microsoft.Compute/galleries/myGallery1/applications/MyApplication1/versions/1.0",
                            "tags": "myTag1",
                            "treatFailureAsDeploymentFailure": False,
                        },
                        {
                            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"
                        },
                    ]
                },
                "hardwareProfile": {"vmSize": "Standard_D1_v2"},
                "networkProfile": {
                    "networkInterfaces": [
                        {
                            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}",
                            "properties": {"primary": True},
                        }
                    ]
                },
                "osProfile": {
                    "adminPassword": "{your-password}",
                    "adminUsername": "{your-username}",
                    "computerName": "myVM",
                },
                "storageProfile": {
                    "imageReference": {
                        "offer": "{image_offer}",
                        "publisher": "{image_publisher}",
                        "sku": "{image_sku}",
                        "version": "latest",
                    },
                    "osDisk": {
                        "caching": "ReadWrite",
                        "createOption": "FromImage",
                        "managedDisk": {"storageAccountType": "Standard_LRS"},
                        "name": "myVMosdisk",
                    },
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2024-07-01/examples/virtualMachineExamples/VirtualMachine_Create_WithApplicationProfile.json
if __name__ == "__main__":
    main()
