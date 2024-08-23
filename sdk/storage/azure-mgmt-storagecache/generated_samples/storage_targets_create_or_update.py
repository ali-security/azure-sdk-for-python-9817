# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.storagecache import StorageCacheManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storagecache
# USAGE
    python storage_targets_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageCacheManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.storage_targets.begin_create_or_update(
        resource_group_name="scgroup",
        cache_name="sc1",
        storage_target_name="st1",
        storagetarget={
            "properties": {
                "junctions": [
                    {
                        "namespacePath": "/path/on/cache",
                        "nfsAccessPolicy": "default",
                        "nfsExport": "exp1",
                        "targetPath": "/path/on/exp1",
                    },
                    {
                        "namespacePath": "/path2/on/cache",
                        "nfsAccessPolicy": "rootSquash",
                        "nfsExport": "exp2",
                        "targetPath": "/path2/on/exp2",
                    },
                ],
                "nfs3": {"target": "10.0.44.44", "usageModel": "READ_ONLY", "verificationTimer": 30},
                "targetType": "nfs3",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/storagecache/resource-manager/Microsoft.StorageCache/stable/2024-03-01/examples/StorageTargets_CreateOrUpdate.json
if __name__ == "__main__":
    main()
