# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.linked_services_operations import LinkedServicesOperations
from .operations.data_sources_operations import DataSourcesOperations
from .operations.workspaces_operations import WorkspacesOperations
from .operations.storage_insights_operations import StorageInsightsOperations
from .operations.saved_searches_operations import SavedSearchesOperations
from . import models


class LogAnalyticsManagementClientConfiguration(AzureConfiguration):
    """Configuration for LogAnalyticsManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(LogAnalyticsManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('loganalyticsmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class LogAnalyticsManagementClient(object):
    """The Log Analytics Client.

    :ivar config: Configuration for client.
    :vartype config: LogAnalyticsManagementClientConfiguration

    :ivar linked_services: LinkedServices operations
    :vartype linked_services: azure.mgmt.loganalytics.operations.LinkedServicesOperations
    :ivar data_sources: DataSources operations
    :vartype data_sources: azure.mgmt.loganalytics.operations.DataSourcesOperations
    :ivar workspaces: Workspaces operations
    :vartype workspaces: azure.mgmt.loganalytics.operations.WorkspacesOperations
    :ivar storage_insights: StorageInsights operations
    :vartype storage_insights: azure.mgmt.loganalytics.operations.StorageInsightsOperations
    :ivar saved_searches: SavedSearches operations
    :vartype saved_searches: azure.mgmt.loganalytics.operations.SavedSearchesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = LogAnalyticsManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.linked_services = LinkedServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_sources = DataSourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.storage_insights = StorageInsightsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.saved_searches = SavedSearchesOperations(
            self._client, self.config, self._serialize, self._deserialize)
