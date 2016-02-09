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
from .operations.certificates_operations import CertificatesOperations
from .operations.classic_mobile_services_operations import ClassicMobileServicesOperations
from .operations.domains_operations import DomainsOperations
from .operations.global_model_operations import GlobalModelOperations
from .operations.global_domain_registration_operations import GlobalDomainRegistrationOperations
from .operations.global_resource_groups_operations import GlobalResourceGroupsOperations
from .operations.hosting_environments_operations import HostingEnvironmentsOperations
from .operations.managed_hosting_environments_operations import ManagedHostingEnvironmentsOperations
from .operations.provider_operations import ProviderOperations
from .operations.server_farms_operations import ServerFarmsOperations
from .operations.sites_operations import SitesOperations
from .operations.top_level_domains_operations import TopLevelDomainsOperations
from .operations.usage_operations import UsageOperations
from . import models


class WebSiteManagementClientConfiguration(AzureConfiguration):
    """Configuration for WebSiteManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Gets Azure subscription credentials.
    :type credentials: credentials
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
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
            self, credentials, subscription_id, api_version='2015-08-01', accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        if credentials is None:
            raise ValueError('credentials must not be None.')
        if subscription_id is None:
            raise ValueError('subscription_id must not be None.')
        if not base_url:
            base_url = 'https://management.azure.com'

        super(WebSiteManagementClientConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('websitemanagementclient/2015-08-01')

        self.credentials = credentials
        self.subscription_id = subscription_id
        self.api_version = api_version
        self.accept_language = accept_language
        self.long_running_operation_retry_timeout = long_running_operation_retry_timeout
        self.generate_client_request_id = generate_client_request_id


class WebSiteManagementClient(object):
    """Use these APIs to manage Azure Websites resources through the Azure Resource Manager. All task operations conform to the HTTP/1.1 protocol specification and each operation returns an x-ms-request-id header that can be used to obtain information about the request. You must make sure that requests made to these resources are secure. For more information, see &lt;a href="https://msdn.microsoft.com/en-us/library/azure/dn790557.aspx"&gt;Authenticating Azure Resource Manager requests.&lt;/a&gt;

    :param config: Configuration for client.
    :type config: WebSiteManagementClientConfiguration

    :ivar certificates: Certificates operations
    :vartype certificates: .operations.CertificatesOperations
    :ivar classic_mobile_services: ClassicMobileServices operations
    :vartype classic_mobile_services: .operations.ClassicMobileServicesOperations
    :ivar domains: Domains operations
    :vartype domains: .operations.DomainsOperations
    :ivar global_model: GlobalModel operations
    :vartype global_model: .operations.GlobalModelOperations
    :ivar global_domain_registration: GlobalDomainRegistration operations
    :vartype global_domain_registration: .operations.GlobalDomainRegistrationOperations
    :ivar global_resource_groups: GlobalResourceGroups operations
    :vartype global_resource_groups: .operations.GlobalResourceGroupsOperations
    :ivar hosting_environments: HostingEnvironments operations
    :vartype hosting_environments: .operations.HostingEnvironmentsOperations
    :ivar managed_hosting_environments: ManagedHostingEnvironments operations
    :vartype managed_hosting_environments: .operations.ManagedHostingEnvironmentsOperations
    :ivar provider: Provider operations
    :vartype provider: .operations.ProviderOperations
    :ivar server_farms: ServerFarms operations
    :vartype server_farms: .operations.ServerFarmsOperations
    :ivar sites: Sites operations
    :vartype sites: .operations.SitesOperations
    :ivar top_level_domains: TopLevelDomains operations
    :vartype top_level_domains: .operations.TopLevelDomainsOperations
    :ivar usage: Usage operations
    :vartype usage: .operations.UsageOperations
    """

    def __init__(self, config):

        self._client = ServiceClient(config.credentials, config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer()
        self._deserialize = Deserializer(client_models)

        self.config = config
        self.certificates = CertificatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.classic_mobile_services = ClassicMobileServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.domains = DomainsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.global_model = GlobalModelOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.global_domain_registration = GlobalDomainRegistrationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.global_resource_groups = GlobalResourceGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.hosting_environments = HostingEnvironmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.managed_hosting_environments = ManagedHostingEnvironmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.provider = ProviderOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.server_farms = ServerFarmsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sites = SitesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.top_level_domains = TopLevelDomainsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usage = UsageOperations(
            self._client, self.config, self._serialize, self._deserialize)
