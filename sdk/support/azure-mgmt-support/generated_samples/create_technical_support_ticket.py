# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.support import MicrosoftSupport

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-support
# USAGE
    python create_technical_support_ticket.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MicrosoftSupport(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.support_tickets_no_subscription.begin_create(
        support_ticket_name="testticket",
        create_support_ticket_parameters={
            "properties": {
                "advancedDiagnosticConsent": "Yes",
                "contactDetails": {
                    "country": "usa",
                    "firstName": "abc",
                    "lastName": "xyz",
                    "preferredContactMethod": "email",
                    "preferredSupportLanguage": "en-US",
                    "preferredTimeZone": "Pacific Standard Time",
                    "primaryEmailAddress": "abc@contoso.com",
                },
                "description": "my description",
                "fileWorkspaceName": "6f16735c-1530836f-e9970f1a-2e49-47b7-96cd-9746b83aa066",
                "problemClassificationId": "/providers/Microsoft.Support/services/virtual_machine_running_linux_service_guid/problemClassifications/problemClassification_guid",
                "problemScopingQuestions": '{"articleId":"076846c1-4c0b-4b21-91c6-1a30246b3867","scopingDetails":[{"question":"When did the problem begin?","controlId":"problem_start_time","orderId":1,"inputType":"static","answer":{"displayValue":"2023-08-31T18:55:00.739Z","value":"2023-08-31T18:55:00.739Z","type":"datetime"}},{"question":"API Type of the Cosmos DB account","controlId":"api_type","orderId":2,"inputType":"static","answer":{"displayValue":"Table","value":"tables","type":"string"}},{"question":"Table name","controlId":"collection_name_table","orderId":11,"inputType":"nonstatic","answer":{"displayValue":"Select Table Name","value":"dont_know_answer","type":"string"}},{"question":"Provide additional details about the issue you\'re facing","controlId":"problem_description","orderId":12,"inputType":"nonstatic","answer":{"displayValue":"test ticket, please ignore and close","value":"test ticket, please ignore and close","type":"string"}}]}',
                "secondaryConsent": [{"type": "virtualmachinerunninglinuxservice", "userConsent": "Yes"}],
                "serviceId": "/providers/Microsoft.Support/services/cddd3eb5-1830-b494-44fd-782f691479dc",
                "severity": "moderate",
                "supportPlanId": "U291cmNlOlNDTSxDbGFyaWZ5SW5zdGFsbGF0aW9uU2l0ZUlkOjcsTGluZUl0ZW1JZDo5ODY1NzIyOSxDb250cmFjdElkOjk4NjU5MTk0LFN1YnNjcmlwdGlvbklkOjc2Y2I3N2ZhLThiMTctNGVhYi05NDkzLWI2NWRhY2U5OTgxMyw=",
                "title": "my title",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/support/resource-manager/Microsoft.Support/preview/2023-06-01-preview/examples/CreateTechnicalSupportTicket.json
if __name__ == "__main__":
    main()
