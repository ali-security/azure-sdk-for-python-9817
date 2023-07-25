# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.mobilenetwork import MobileNetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-mobilenetwork
# USAGE
    python sim_policy_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MobileNetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.sim_policies.begin_create_or_update(
        resource_group_name="rg1",
        mobile_network_name="testMobileNetwork",
        sim_policy_name="testPolicy",
        parameters={
            "location": "eastus",
            "properties": {
                "defaultSlice": {
                    "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/slices/testSlice"
                },
                "registrationTimer": 3240,
                "sliceConfigurations": [
                    {
                        "dataNetworkConfigurations": [
                            {
                                "5qi": 9,
                                "additionalAllowedSessionTypes": [],
                                "allocationAndRetentionPriorityLevel": 9,
                                "allowedServices": [
                                    {
                                        "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/services/testService"
                                    }
                                ],
                                "dataNetwork": {
                                    "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/dataNetworks/testdataNetwork"
                                },
                                "defaultSessionType": "IPv4",
                                "maximumNumberOfBufferedPackets": 200,
                                "preemptionCapability": "NotPreempt",
                                "preemptionVulnerability": "Preemptable",
                                "sessionAmbr": {"downlink": "1 Gbps", "uplink": "500 Mbps"},
                            }
                        ],
                        "defaultDataNetwork": {
                            "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/dataNetworks/testdataNetwork"
                        },
                        "slice": {
                            "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/slices/testSlice"
                        },
                    }
                ],
                "ueAmbr": {"downlink": "1 Gbps", "uplink": "500 Mbps"},
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/mobilenetwork/resource-manager/Microsoft.MobileNetwork/stable/2023-06-01/examples/SimPolicyCreate.json
if __name__ == "__main__":
    main()
