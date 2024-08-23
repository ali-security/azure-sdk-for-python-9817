# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.containerservice import ContainerServiceClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContainerServiceManagedClustersOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerServiceClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.managed_clusters.list(
            api_version="2018-03-31",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.managed_clusters.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2018-03-31",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get_upgrade_profile(self, resource_group):
        response = self.client.managed_clusters.get_upgrade_profile(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2018-03-31",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get_access_profile(self, resource_group):
        response = self.client.managed_clusters.get_access_profile(
            resource_group_name=resource_group.name,
            resource_name="str",
            role_name="str",
            api_version="2018-03-31",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_cluster_admin_credentials(self, resource_group):
        response = self.client.managed_clusters.list_cluster_admin_credentials(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2018-03-31",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_cluster_user_credentials(self, resource_group):
        response = self.client.managed_clusters.list_cluster_user_credentials(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2018-03-31",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.managed_clusters.get(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2018-03-31",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.managed_clusters.begin_create_or_update(
            resource_group_name=resource_group.name,
            resource_name="str",
            parameters={
                "location": "str",
                "aadProfile": {"clientAppID": "str", "serverAppID": "str", "serverAppSecret": "str", "tenantID": "str"},
                "addonProfiles": {"str": {"enabled": bool, "config": {"str": "str"}}},
                "agentPoolProfiles": [
                    {
                        "name": "str",
                        "vmSize": "str",
                        "count": 1,
                        "maxPods": 0,
                        "osDiskSizeGB": 0,
                        "osType": "Linux",
                        "storageProfile": "str",
                        "vnetSubnetID": "str",
                    }
                ],
                "dnsPrefix": "str",
                "enableRBAC": bool,
                "fqdn": "str",
                "id": "str",
                "kubernetesVersion": "str",
                "linuxProfile": {"adminUsername": "str", "ssh": {"publicKeys": [{"keyData": "str"}]}},
                "name": "str",
                "networkProfile": {
                    "dnsServiceIP": "10.0.0.10",
                    "dockerBridgeCidr": "172.17.0.1/16",
                    "networkPlugin": "kubenet",
                    "networkPolicy": "str",
                    "podCidr": "10.244.0.0/16",
                    "serviceCidr": "10.0.0.0/16",
                },
                "nodeResourceGroup": "str",
                "provisioningState": "str",
                "servicePrincipalProfile": {"clientId": "str", "secret": "str"},
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2018-03-31",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update_tags(self, resource_group):
        response = self.client.managed_clusters.begin_update_tags(
            resource_group_name=resource_group.name,
            resource_name="str",
            parameters={"tags": {"str": "str"}},
            api_version="2018-03-31",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.managed_clusters.begin_delete(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2018-03-31",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_reset_service_principal_profile(self, resource_group):
        response = self.client.managed_clusters.begin_reset_service_principal_profile(
            resource_group_name=resource_group.name,
            resource_name="str",
            parameters={"clientId": "str", "secret": "str"},
            api_version="2018-03-31",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_reset_aad_profile(self, resource_group):
        response = self.client.managed_clusters.begin_reset_aad_profile(
            resource_group_name=resource_group.name,
            resource_name="str",
            parameters={"clientAppID": "str", "serverAppID": "str", "serverAppSecret": "str", "tenantID": "str"},
            api_version="2018-03-31",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
