# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.apimanagement import ApiManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-apimanagement
# USAGE
    python api_management_create_service_with_custom_hostname_key_vault.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ApiManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.api_management_service.begin_create_or_update(
        resource_group_name="rg1",
        service_name="apimService1",
        parameters={
            "identity": {
                "type": "UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.ManagedIdentity/userAssignedIdentities/id1": {}
                },
            },
            "location": "North Europe",
            "properties": {
                "apiVersionConstraint": {"minApiVersion": "2019-01-01"},
                "hostnameConfigurations": [
                    {
                        "defaultSslBinding": True,
                        "hostName": "gateway1.msitesting.net",
                        "identityClientId": "329419bc-adec-4dce-9568-25a6d486e468",
                        "keyVaultId": "https://rpbvtkeyvaultintegration.vault.azure.net/secrets/msitestingCert",
                        "type": "Proxy",
                    },
                    {
                        "hostName": "mgmt.msitesting.net",
                        "identityClientId": "329419bc-adec-4dce-9568-25a6d486e468",
                        "keyVaultId": "https://rpbvtkeyvaultintegration.vault.azure.net/secrets/msitestingCert",
                        "type": "Management",
                    },
                    {
                        "hostName": "portal1.msitesting.net",
                        "identityClientId": "329419bc-adec-4dce-9568-25a6d486e468",
                        "keyVaultId": "https://rpbvtkeyvaultintegration.vault.azure.net/secrets/msitestingCert",
                        "type": "Portal",
                    },
                ],
                "publisherEmail": "apim@autorestsdk.com",
                "publisherName": "autorestsdk",
                "virtualNetworkType": "None",
            },
            "sku": {"capacity": 1, "name": "Premium"},
            "tags": {"tag1": "value1", "tag2": "value2", "tag3": "value3"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/apimanagement/resource-manager/Microsoft.ApiManagement/stable/2021-08-01/examples/ApiManagementCreateServiceWithCustomHostnameKeyVault.json
if __name__ == "__main__":
    main()
