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
from .operations.objects_operations import ObjectsOperations
from .operations.applications_operations import ApplicationsOperations
from .operations.groups_operations import GroupsOperations
from .operations.service_principals_operations import ServicePrincipalsOperations
from .operations.users_operations import UsersOperations
from .operations.domains_operations import DomainsOperations
from . import models


class GraphRbacManagementClientConfiguration(AzureConfiguration):
    """Configuration for GraphRbacManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, tenant_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if tenant_id is None:
            raise ValueError("Parameter 'tenant_id' must not be None.")
        if not base_url:
            base_url = 'https://graph.windows.net'

        super(GraphRbacManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-graphrbac/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.tenant_id = tenant_id


class GraphRbacManagementClient(object):
    """The Graph RBAC Management Client

    :ivar config: Configuration for client.
    :vartype config: GraphRbacManagementClientConfiguration

    :ivar objects: Objects operations
    :vartype objects: azure.graphrbac.operations.ObjectsOperations
    :ivar applications: Applications operations
    :vartype applications: azure.graphrbac.operations.ApplicationsOperations
    :ivar groups: Groups operations
    :vartype groups: azure.graphrbac.operations.GroupsOperations
    :ivar service_principals: ServicePrincipals operations
    :vartype service_principals: azure.graphrbac.operations.ServicePrincipalsOperations
    :ivar users: Users operations
    :vartype users: azure.graphrbac.operations.UsersOperations
    :ivar domains: Domains operations
    :vartype domains: azure.graphrbac.operations.DomainsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, tenant_id, base_url=None):

        self.config = GraphRbacManagementClientConfiguration(credentials, tenant_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.6'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.objects = ObjectsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.applications = ApplicationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.groups = GroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_principals = ServicePrincipalsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.domains = DomainsOperations(
            self._client, self.config, self._serialize, self._deserialize)
