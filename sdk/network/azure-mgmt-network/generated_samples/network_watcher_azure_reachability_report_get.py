# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python network_watcher_azure_reachability_report_get.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.network_watchers.begin_get_azure_reachability_report(
        resource_group_name="rg1",
        network_watcher_name="nw1",
        parameters={
            "azureLocations": ["West US"],
            "endTime": "2017-09-10T00:00:00Z",
            "providerLocation": {"country": "United States", "state": "washington"},
            "providers": ["Frontier Communications of America, Inc. - ASN 5650"],
            "startTime": "2017-09-07T00:00:00Z",
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-09-01/examples/NetworkWatcherAzureReachabilityReportGet.json
if __name__ == "__main__":
    main()
