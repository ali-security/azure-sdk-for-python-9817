# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.profiles_operations import ProfilesOperations
from .operations.endpoints_operations import EndpointsOperations
from .operations.origins_operations import OriginsOperations
from .operations.custom_domains_operations import CustomDomainsOperations
from .operations.name_availability_operations import NameAvailabilityOperations
from .operations.operations_operations import OperationsOperations
from . import models


class CdnManagementClientConfiguration(AzureConfiguration):
    """Configuration for CdnManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Gets Azure subscription credentials.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client
     request. Current version is 2015-06-01
    :type api_version: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, subscription_id, api_version='2015-06-01', accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if api_version is not None and not isinstance(api_version, str):
            raise TypeError("Optional parameter 'api_version' must be str.")
        if accept_language is not None and not isinstance(accept_language, str):
            raise TypeError("Optional parameter 'accept_language' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(CdnManagementClientConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('cdnmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id
        self.api_version = api_version
        self.accept_language = accept_language
        self.long_running_operation_retry_timeout = long_running_operation_retry_timeout
        self.generate_client_request_id = generate_client_request_id


class CdnManagementClient(object):
    """Use these APIs to manage Azure CDN resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure. For more information, see &lt;a href="https://msdn.microsoft.com/en-us/library/azure/dn790557.aspx"&gt;Authenticating Azure Resource Manager requests.&lt;/a&gt;

    :param config: Configuration for client.
    :type config: CdnManagementClientConfiguration

    :ivar profiles: Profiles operations
    :vartype profiles: .operations.ProfilesOperations
    :ivar endpoints: Endpoints operations
    :vartype endpoints: .operations.EndpointsOperations
    :ivar origins: Origins operations
    :vartype origins: .operations.OriginsOperations
    :ivar custom_domains: CustomDomains operations
    :vartype custom_domains: .operations.CustomDomainsOperations
    :ivar name_availability: NameAvailability operations
    :vartype name_availability: .operations.NameAvailabilityOperations
    :ivar operations: Operations operations
    :vartype operations: .operations.OperationsOperations
    """

    def __init__(self, config):

        self._client = ServiceClient(config.credentials, config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer()
        self._deserialize = Deserializer(client_models)

        self.config = config
        self.profiles = ProfilesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.endpoints = EndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.origins = OriginsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.custom_domains = CustomDomainsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.name_availability = NameAvailabilityOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = OperationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
