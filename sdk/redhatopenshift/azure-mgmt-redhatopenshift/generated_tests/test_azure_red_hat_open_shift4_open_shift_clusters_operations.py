# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.redhatopenshift import AzureRedHatOpenShiftClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAzureRedHatOpenShift4OpenShiftClustersOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AzureRedHatOpenShiftClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.open_shift_clusters.list(
            api_version="2020-04-30",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.open_shift_clusters.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2020-04-30",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.open_shift_clusters.get(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2020-04-30",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.open_shift_clusters.begin_create_or_update(
            resource_group_name=resource_group.name,
            resource_name="str",
            parameters={
                "location": "str",
                "apiserverProfile": {"ip": "str", "url": "str", "visibility": "str"},
                "clusterProfile": {"domain": "str", "pullSecret": "str", "resourceGroupId": "str", "version": "str"},
                "consoleProfile": {"url": "str"},
                "id": "str",
                "ingressProfiles": [{"ip": "str", "name": "str", "visibility": "str"}],
                "masterProfile": {"subnetId": "str", "vmSize": "str"},
                "name": "str",
                "networkProfile": {"podCidr": "str", "serviceCidr": "str"},
                "provisioningState": "str",
                "servicePrincipalProfile": {"clientId": "str", "clientSecret": "str"},
                "tags": {"str": "str"},
                "type": "str",
                "workerProfiles": [{"count": 0, "diskSizeGB": 0, "name": "str", "subnetId": "str", "vmSize": "str"}],
            },
            api_version="2020-04-30",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.open_shift_clusters.begin_delete(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2020-04-30",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.open_shift_clusters.begin_update(
            resource_group_name=resource_group.name,
            resource_name="str",
            parameters={
                "apiserverProfile": {"ip": "str", "url": "str", "visibility": "str"},
                "clusterProfile": {"domain": "str", "pullSecret": "str", "resourceGroupId": "str", "version": "str"},
                "consoleProfile": {"url": "str"},
                "ingressProfiles": [{"ip": "str", "name": "str", "visibility": "str"}],
                "masterProfile": {"subnetId": "str", "vmSize": "str"},
                "networkProfile": {"podCidr": "str", "serviceCidr": "str"},
                "provisioningState": "str",
                "servicePrincipalProfile": {"clientId": "str", "clientSecret": "str"},
                "tags": {"str": "str"},
                "workerProfiles": [{"count": 0, "diskSizeGB": 0, "name": "str", "subnetId": "str", "vmSize": "str"}],
            },
            api_version="2020-04-30",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_credentials(self, resource_group):
        response = self.client.open_shift_clusters.list_credentials(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2020-04-30",
        )

        # please add some check logic here by yourself
        # ...
