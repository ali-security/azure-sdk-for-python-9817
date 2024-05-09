# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import PolicyClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resource
# USAGE
    python list_built_in_policy_set_definition_versions.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PolicyClient(
        credential=DefaultAzureCredential(),
        policy_definition_name="POLICY_DEFINITION_NAME",
        policy_definition_version="POLICY_DEFINITION_VERSION",
        policy_set_definition_name="1f3afdf9-d0c9-4c3d-847f-89da613e70a8",
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.policy_set_definition_versions.list_built_in()
    for item in response:
        print(item)


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Authorization/stable/2023-04-01/examples/listBuiltInPolicySetDefinitionVersions.json
if __name__ == "__main__":
    main()
