# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import DeploymentScriptsClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resource
# USAGE
    python deployment_scripts_get_logs_default.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DeploymentScriptsClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.deployment_scripts.get_logs_default(
        resource_group_name="script-rg",
        script_name="MyDeploymentScript",
    )
    print(response)


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Resources/stable/2020-10-01/examples/DeploymentScripts_GetLogsDefault.json
if __name__ == "__main__":
    main()
