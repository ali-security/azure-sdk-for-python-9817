# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-monitor
# USAGE
    python create_or_update_action_group.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MonitorManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="187f412d-1758-44d9-b052-169e2564721d",
    )

    response = client.action_groups.create_or_update(
        resource_group_name="Default-NotificationRules",
        action_group_name="SampleActionGroup",
        action_group={
            "location": "Global",
            "properties": {
                "armRoleReceivers": [
                    {
                        "name": "Sample armRole",
                        "roleId": "8e3af657-a8ff-443c-a75c-2fe8c4bcb635",
                        "useCommonAlertSchema": True,
                    }
                ],
                "automationRunbookReceivers": [
                    {
                        "automationAccountId": "/subscriptions/187f412d-1758-44d9-b052-169e2564721d/resourceGroups/runbookTest/providers/Microsoft.Automation/automationAccounts/runbooktest",
                        "isGlobalRunbook": False,
                        "name": "testRunbook",
                        "runbookName": "Sample runbook",
                        "serviceUri": "<serviceUri>",
                        "useCommonAlertSchema": True,
                        "webhookResourceId": "/subscriptions/187f412d-1758-44d9-b052-169e2564721d/resourceGroups/runbookTest/providers/Microsoft.Automation/automationAccounts/runbooktest/webhooks/Alert1510184037084",
                    }
                ],
                "azureAppPushReceivers": [{"emailAddress": "johndoe@email.com", "name": "Sample azureAppPush"}],
                "azureFunctionReceivers": [
                    {
                        "functionAppResourceId": "/subscriptions/5def922a-3ed4-49c1-b9fd-05ec533819a3/resourceGroups/aznsTest/providers/Microsoft.Web/sites/testFunctionApp",
                        "functionName": "HttpTriggerCSharp1",
                        "httpTriggerUrl": "http://test.me",
                        "name": "Sample azureFunction",
                        "useCommonAlertSchema": True,
                    }
                ],
                "emailReceivers": [
                    {"emailAddress": "johndoe@email.com", "name": "John Doe's email", "useCommonAlertSchema": False},
                    {"emailAddress": "janesmith@email.com", "name": "Jane Smith's email", "useCommonAlertSchema": True},
                ],
                "enabled": True,
                "eventHubReceivers": [
                    {
                        "eventHubName": "testEventHub",
                        "eventHubNameSpace": "testEventHubNameSpace",
                        "name": "Sample eventHub",
                        "subscriptionId": "187f412d-1758-44d9-b052-169e2564721d",
                        "tenantId": "68a4459a-ccb8-493c-b9da-dd30457d1b84",
                    }
                ],
                "groupShortName": "sample",
                "itsmReceivers": [
                    {
                        "connectionId": "a3b9076c-ce8e-434e-85b4-aff10cb3c8f1",
                        "name": "Sample itsm",
                        "region": "westcentralus",
                        "ticketConfiguration": '{"PayloadRevision":0,"WorkItemType":"Incident","UseTemplate":false,"WorkItemData":"{}","CreateOneWIPerCI":false}',
                        "workspaceId": "5def922a-3ed4-49c1-b9fd-05ec533819a3|55dfd1f8-7e59-4f89-bf56-4c82f5ace23c",
                    }
                ],
                "logicAppReceivers": [
                    {
                        "callbackUrl": "https://prod-27.northcentralus.logic.azure.com/workflows/68e572e818e5457ba898763b7db90877/triggers/manual/paths/invoke/azns/test?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=Abpsb72UYJxPPvmDo937uzofupO5r_vIeWEx7KVHo7w",
                        "name": "Sample logicApp",
                        "resourceId": "/subscriptions/187f412d-1758-44d9-b052-169e2564721d/resourceGroups/LogicApp/providers/Microsoft.Logic/workflows/testLogicApp",
                        "useCommonAlertSchema": False,
                    }
                ],
                "smsReceivers": [
                    {"countryCode": "1", "name": "John Doe's mobile", "phoneNumber": "1234567890"},
                    {"countryCode": "1", "name": "Jane Smith's mobile", "phoneNumber": "0987654321"},
                ],
                "voiceReceivers": [{"countryCode": "1", "name": "Sample voice", "phoneNumber": "1234567890"}],
                "webhookReceivers": [
                    {
                        "name": "Sample webhook 1",
                        "serviceUri": "http://www.example.com/webhook1",
                        "useCommonAlertSchema": True,
                    },
                    {
                        "identifierUri": "http://someidentifier/d7811ba3-7996-4a93-99b6-6b2f3f355f8a",
                        "name": "Sample webhook 2",
                        "objectId": "d3bb868c-fe44-452c-aa26-769a6538c808",
                        "serviceUri": "http://www.example.com/webhook2",
                        "tenantId": "68a4459a-ccb8-493c-b9da-dd30457d1b84",
                        "useAadAuth": True,
                        "useCommonAlertSchema": True,
                    },
                ],
            },
            "tags": {},
        },
    )
    print(response)


# x-ms-original-file: specification/monitor/resource-manager/Microsoft.Insights/stable/2023-01-01/examples/createOrUpdateActionGroup.json
if __name__ == "__main__":
    main()
