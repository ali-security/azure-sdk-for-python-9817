# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class CloudErrorBody(_serialization.Model):
    """An error response from the Container service.

    :ivar code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :vartype code: str
    :ivar message: A message describing the error, intended to be suitable for display in a user
     interface.
    :vartype message: str
    :ivar target: The target of the particular error. For example, the name of the property in
     error.
    :vartype target: str
    :ivar details: A list of additional details about the error.
    :vartype details: list[~azure.mgmt.containerservice.v2019_04_30.models.CloudErrorBody]
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[CloudErrorBody]"},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        details: Optional[List["_models.CloudErrorBody"]] = None,
        **kwargs
    ):
        """
        :keyword code: An identifier for the error. Codes are invariant and are intended to be consumed
         programmatically.
        :paramtype code: str
        :keyword message: A message describing the error, intended to be suitable for display in a user
         interface.
        :paramtype message: str
        :keyword target: The target of the particular error. For example, the name of the property in
         error.
        :paramtype target: str
        :keyword details: A list of additional details about the error.
        :paramtype details: list[~azure.mgmt.containerservice.v2019_04_30.models.CloudErrorBody]
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class NetworkProfile(_serialization.Model):
    """Represents the OpenShift networking configuration.

    :ivar vnet_cidr: CIDR for the OpenShift Vnet.
    :vartype vnet_cidr: str
    :ivar peer_vnet_id: CIDR of the Vnet to peer.
    :vartype peer_vnet_id: str
    :ivar vnet_id: ID of the Vnet created for OSA cluster.
    :vartype vnet_id: str
    """

    _attribute_map = {
        "vnet_cidr": {"key": "vnetCidr", "type": "str"},
        "peer_vnet_id": {"key": "peerVnetId", "type": "str"},
        "vnet_id": {"key": "vnetId", "type": "str"},
    }

    def __init__(
        self,
        *,
        vnet_cidr: str = "10.0.0.0/8",
        peer_vnet_id: Optional[str] = None,
        vnet_id: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword vnet_cidr: CIDR for the OpenShift Vnet.
        :paramtype vnet_cidr: str
        :keyword peer_vnet_id: CIDR of the Vnet to peer.
        :paramtype peer_vnet_id: str
        :keyword vnet_id: ID of the Vnet created for OSA cluster.
        :paramtype vnet_id: str
        """
        super().__init__(**kwargs)
        self.vnet_cidr = vnet_cidr
        self.peer_vnet_id = peer_vnet_id
        self.vnet_id = vnet_id


class Resource(_serialization.Model):
    """The Resource model definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs):
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class OpenShiftManagedCluster(Resource):  # pylint: disable=too-many-instance-attributes
    """OpenShift Managed cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar plan: Define the resource plan as required by ARM for billing purposes.
    :vartype plan: ~azure.mgmt.containerservice.v2019_04_30.models.PurchasePlan
    :ivar provisioning_state: The current deployment or provisioning state, which only appears in
     the response.
    :vartype provisioning_state: str
    :ivar open_shift_version: Version of OpenShift specified when creating the cluster.
    :vartype open_shift_version: str
    :ivar cluster_version: Version of OpenShift specified when creating the cluster.
    :vartype cluster_version: str
    :ivar public_hostname: Service generated FQDN for OpenShift API server.
    :vartype public_hostname: str
    :ivar fqdn: Service generated FQDN for OpenShift API server loadbalancer internal hostname.
    :vartype fqdn: str
    :ivar network_profile: Configuration for OpenShift networking.
    :vartype network_profile: ~azure.mgmt.containerservice.v2019_04_30.models.NetworkProfile
    :ivar router_profiles: Configuration for OpenShift router(s).
    :vartype router_profiles:
     list[~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftRouterProfile]
    :ivar master_pool_profile: Configuration for OpenShift master VMs.
    :vartype master_pool_profile:
     ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterMasterPoolProfile
    :ivar agent_pool_profiles: Configuration of OpenShift cluster VMs.
    :vartype agent_pool_profiles:
     list[~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterAgentPoolProfile]
    :ivar auth_profile: Configures OpenShift authentication.
    :vartype auth_profile:
     ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterAuthProfile
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
        "provisioning_state": {"readonly": True},
        "cluster_version": {"readonly": True},
        "public_hostname": {"readonly": True},
        "fqdn": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "plan": {"key": "plan", "type": "PurchasePlan"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "open_shift_version": {"key": "properties.openShiftVersion", "type": "str"},
        "cluster_version": {"key": "properties.clusterVersion", "type": "str"},
        "public_hostname": {"key": "properties.publicHostname", "type": "str"},
        "fqdn": {"key": "properties.fqdn", "type": "str"},
        "network_profile": {"key": "properties.networkProfile", "type": "NetworkProfile"},
        "router_profiles": {"key": "properties.routerProfiles", "type": "[OpenShiftRouterProfile]"},
        "master_pool_profile": {
            "key": "properties.masterPoolProfile",
            "type": "OpenShiftManagedClusterMasterPoolProfile",
        },
        "agent_pool_profiles": {
            "key": "properties.agentPoolProfiles",
            "type": "[OpenShiftManagedClusterAgentPoolProfile]",
        },
        "auth_profile": {"key": "properties.authProfile", "type": "OpenShiftManagedClusterAuthProfile"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        plan: Optional["_models.PurchasePlan"] = None,
        open_shift_version: Optional[str] = None,
        network_profile: Optional["_models.NetworkProfile"] = None,
        router_profiles: Optional[List["_models.OpenShiftRouterProfile"]] = None,
        master_pool_profile: Optional["_models.OpenShiftManagedClusterMasterPoolProfile"] = None,
        agent_pool_profiles: Optional[List["_models.OpenShiftManagedClusterAgentPoolProfile"]] = None,
        auth_profile: Optional["_models.OpenShiftManagedClusterAuthProfile"] = None,
        **kwargs
    ):
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword plan: Define the resource plan as required by ARM for billing purposes.
        :paramtype plan: ~azure.mgmt.containerservice.v2019_04_30.models.PurchasePlan
        :keyword open_shift_version: Version of OpenShift specified when creating the cluster.
        :paramtype open_shift_version: str
        :keyword network_profile: Configuration for OpenShift networking.
        :paramtype network_profile: ~azure.mgmt.containerservice.v2019_04_30.models.NetworkProfile
        :keyword router_profiles: Configuration for OpenShift router(s).
        :paramtype router_profiles:
         list[~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftRouterProfile]
        :keyword master_pool_profile: Configuration for OpenShift master VMs.
        :paramtype master_pool_profile:
         ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterMasterPoolProfile
        :keyword agent_pool_profiles: Configuration of OpenShift cluster VMs.
        :paramtype agent_pool_profiles:
         list[~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterAgentPoolProfile]
        :keyword auth_profile: Configures OpenShift authentication.
        :paramtype auth_profile:
         ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterAuthProfile
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.plan = plan
        self.provisioning_state = None
        self.open_shift_version = open_shift_version
        self.cluster_version = None
        self.public_hostname = None
        self.fqdn = None
        self.network_profile = network_profile
        self.router_profiles = router_profiles
        self.master_pool_profile = master_pool_profile
        self.agent_pool_profiles = agent_pool_profiles
        self.auth_profile = auth_profile


class OpenShiftManagedClusterBaseIdentityProvider(_serialization.Model):
    """Structure for any Identity provider.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    OpenShiftManagedClusterAADIdentityProvider

    All required parameters must be populated in order to send to Azure.

    :ivar kind: The kind of the provider. Required.
    :vartype kind: str
    """

    _validation = {
        "kind": {"required": True},
    }

    _attribute_map = {
        "kind": {"key": "kind", "type": "str"},
    }

    _subtype_map = {"kind": {"AADIdentityProvider": "OpenShiftManagedClusterAADIdentityProvider"}}

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.kind: Optional[str] = None


class OpenShiftManagedClusterAADIdentityProvider(OpenShiftManagedClusterBaseIdentityProvider):
    """Defines the Identity provider for MS AAD.

    All required parameters must be populated in order to send to Azure.

    :ivar kind: The kind of the provider. Required.
    :vartype kind: str
    :ivar client_id: The clientId password associated with the provider.
    :vartype client_id: str
    :ivar secret: The secret password associated with the provider.
    :vartype secret: str
    :ivar tenant_id: The tenantId associated with the provider.
    :vartype tenant_id: str
    :ivar customer_admin_group_id: The groupId to be granted cluster admin role.
    :vartype customer_admin_group_id: str
    """

    _validation = {
        "kind": {"required": True},
    }

    _attribute_map = {
        "kind": {"key": "kind", "type": "str"},
        "client_id": {"key": "clientId", "type": "str"},
        "secret": {"key": "secret", "type": "str"},
        "tenant_id": {"key": "tenantId", "type": "str"},
        "customer_admin_group_id": {"key": "customerAdminGroupId", "type": "str"},
    }

    def __init__(
        self,
        *,
        client_id: Optional[str] = None,
        secret: Optional[str] = None,
        tenant_id: Optional[str] = None,
        customer_admin_group_id: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword client_id: The clientId password associated with the provider.
        :paramtype client_id: str
        :keyword secret: The secret password associated with the provider.
        :paramtype secret: str
        :keyword tenant_id: The tenantId associated with the provider.
        :paramtype tenant_id: str
        :keyword customer_admin_group_id: The groupId to be granted cluster admin role.
        :paramtype customer_admin_group_id: str
        """
        super().__init__(**kwargs)
        self.kind: str = "AADIdentityProvider"
        self.client_id = client_id
        self.secret = secret
        self.tenant_id = tenant_id
        self.customer_admin_group_id = customer_admin_group_id


class OpenShiftManagedClusterAgentPoolProfile(_serialization.Model):
    """Defines the configuration of the OpenShift cluster VMs.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Unique name of the pool profile in the context of the subscription and resource
     group. Required.
    :vartype name: str
    :ivar count: Number of agents (VMs) to host docker containers. Required.
    :vartype count: int
    :ivar vm_size: Size of agent VMs. Required. Known values are: "Standard_D2s_v3",
     "Standard_D4s_v3", "Standard_D8s_v3", "Standard_D16s_v3", "Standard_D32s_v3",
     "Standard_D64s_v3", "Standard_DS4_v2", "Standard_DS5_v2", "Standard_F8s_v2",
     "Standard_F16s_v2", "Standard_F32s_v2", "Standard_F64s_v2", "Standard_F72s_v2", "Standard_F8s",
     "Standard_F16s", "Standard_E4s_v3", "Standard_E8s_v3", "Standard_E16s_v3", "Standard_E20s_v3",
     "Standard_E32s_v3", "Standard_E64s_v3", "Standard_GS2", "Standard_GS3", "Standard_GS4",
     "Standard_GS5", "Standard_DS12_v2", "Standard_DS13_v2", "Standard_DS14_v2", "Standard_DS15_v2",
     "Standard_L4s", "Standard_L8s", "Standard_L16s", and "Standard_L32s".
    :vartype vm_size: str or
     ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftContainerServiceVMSize
    :ivar subnet_cidr: Subnet CIDR for the peering.
    :vartype subnet_cidr: str
    :ivar os_type: OsType to be used to specify os type. Choose from Linux and Windows. Default to
     Linux. Known values are: "Linux" and "Windows".
    :vartype os_type: str or ~azure.mgmt.containerservice.v2019_04_30.models.OSType
    :ivar role: Define the role of the AgentPoolProfile. Known values are: "compute" and "infra".
    :vartype role: str or
     ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftAgentPoolProfileRole
    """

    _validation = {
        "name": {"required": True},
        "count": {"required": True},
        "vm_size": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "count": {"key": "count", "type": "int"},
        "vm_size": {"key": "vmSize", "type": "str"},
        "subnet_cidr": {"key": "subnetCidr", "type": "str"},
        "os_type": {"key": "osType", "type": "str"},
        "role": {"key": "role", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: str,
        count: int,
        vm_size: Union[str, "_models.OpenShiftContainerServiceVMSize"],
        subnet_cidr: str = "10.0.0.0/24",
        os_type: Union[str, "_models.OSType"] = "Linux",
        role: Optional[Union[str, "_models.OpenShiftAgentPoolProfileRole"]] = None,
        **kwargs
    ):
        """
        :keyword name: Unique name of the pool profile in the context of the subscription and resource
         group. Required.
        :paramtype name: str
        :keyword count: Number of agents (VMs) to host docker containers. Required.
        :paramtype count: int
        :keyword vm_size: Size of agent VMs. Required. Known values are: "Standard_D2s_v3",
         "Standard_D4s_v3", "Standard_D8s_v3", "Standard_D16s_v3", "Standard_D32s_v3",
         "Standard_D64s_v3", "Standard_DS4_v2", "Standard_DS5_v2", "Standard_F8s_v2",
         "Standard_F16s_v2", "Standard_F32s_v2", "Standard_F64s_v2", "Standard_F72s_v2", "Standard_F8s",
         "Standard_F16s", "Standard_E4s_v3", "Standard_E8s_v3", "Standard_E16s_v3", "Standard_E20s_v3",
         "Standard_E32s_v3", "Standard_E64s_v3", "Standard_GS2", "Standard_GS3", "Standard_GS4",
         "Standard_GS5", "Standard_DS12_v2", "Standard_DS13_v2", "Standard_DS14_v2", "Standard_DS15_v2",
         "Standard_L4s", "Standard_L8s", "Standard_L16s", and "Standard_L32s".
        :paramtype vm_size: str or
         ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftContainerServiceVMSize
        :keyword subnet_cidr: Subnet CIDR for the peering.
        :paramtype subnet_cidr: str
        :keyword os_type: OsType to be used to specify os type. Choose from Linux and Windows. Default
         to Linux. Known values are: "Linux" and "Windows".
        :paramtype os_type: str or ~azure.mgmt.containerservice.v2019_04_30.models.OSType
        :keyword role: Define the role of the AgentPoolProfile. Known values are: "compute" and
         "infra".
        :paramtype role: str or
         ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftAgentPoolProfileRole
        """
        super().__init__(**kwargs)
        self.name = name
        self.count = count
        self.vm_size = vm_size
        self.subnet_cidr = subnet_cidr
        self.os_type = os_type
        self.role = role


class OpenShiftManagedClusterAuthProfile(_serialization.Model):
    """Defines all possible authentication profiles for the OpenShift cluster.

    :ivar identity_providers: Type of authentication profile to use.
    :vartype identity_providers:
     list[~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterIdentityProvider]
    """

    _attribute_map = {
        "identity_providers": {"key": "identityProviders", "type": "[OpenShiftManagedClusterIdentityProvider]"},
    }

    def __init__(
        self, *, identity_providers: Optional[List["_models.OpenShiftManagedClusterIdentityProvider"]] = None, **kwargs
    ):
        """
        :keyword identity_providers: Type of authentication profile to use.
        :paramtype identity_providers:
         list[~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterIdentityProvider]
        """
        super().__init__(**kwargs)
        self.identity_providers = identity_providers


class OpenShiftManagedClusterIdentityProvider(_serialization.Model):
    """Defines the configuration of the identity providers to be used in the OpenShift cluster.

    :ivar name: Name of the provider.
    :vartype name: str
    :ivar provider: Configuration of the provider.
    :vartype provider:
     ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterBaseIdentityProvider
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "provider": {"key": "provider", "type": "OpenShiftManagedClusterBaseIdentityProvider"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        provider: Optional["_models.OpenShiftManagedClusterBaseIdentityProvider"] = None,
        **kwargs
    ):
        """
        :keyword name: Name of the provider.
        :paramtype name: str
        :keyword provider: Configuration of the provider.
        :paramtype provider:
         ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedClusterBaseIdentityProvider
        """
        super().__init__(**kwargs)
        self.name = name
        self.provider = provider


class OpenShiftManagedClusterListResult(_serialization.Model):
    """The response from the List OpenShift Managed Clusters operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: The list of OpenShift managed clusters.
    :vartype value: list[~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedCluster]
    :ivar next_link: The URL to get the next set of OpenShift managed cluster results.
    :vartype next_link: str
    """

    _validation = {
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[OpenShiftManagedCluster]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.OpenShiftManagedCluster"]] = None, **kwargs):
        """
        :keyword value: The list of OpenShift managed clusters.
        :paramtype value: list[~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftManagedCluster]
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = None


class OpenShiftManagedClusterMasterPoolProfile(_serialization.Model):
    """OpenShiftManagedClusterMaterPoolProfile contains configuration for OpenShift master VMs.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Unique name of the master pool profile in the context of the subscription and
     resource group.
    :vartype name: str
    :ivar count: Number of masters (VMs) to host docker containers. The default value is 3.
     Required.
    :vartype count: int
    :ivar vm_size: Size of agent VMs. Required. Known values are: "Standard_D2s_v3",
     "Standard_D4s_v3", "Standard_D8s_v3", "Standard_D16s_v3", "Standard_D32s_v3",
     "Standard_D64s_v3", "Standard_DS4_v2", "Standard_DS5_v2", "Standard_F8s_v2",
     "Standard_F16s_v2", "Standard_F32s_v2", "Standard_F64s_v2", "Standard_F72s_v2", "Standard_F8s",
     "Standard_F16s", "Standard_E4s_v3", "Standard_E8s_v3", "Standard_E16s_v3", "Standard_E20s_v3",
     "Standard_E32s_v3", "Standard_E64s_v3", "Standard_GS2", "Standard_GS3", "Standard_GS4",
     "Standard_GS5", "Standard_DS12_v2", "Standard_DS13_v2", "Standard_DS14_v2", "Standard_DS15_v2",
     "Standard_L4s", "Standard_L8s", "Standard_L16s", and "Standard_L32s".
    :vartype vm_size: str or
     ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftContainerServiceVMSize
    :ivar subnet_cidr: Subnet CIDR for the peering.
    :vartype subnet_cidr: str
    :ivar os_type: OsType to be used to specify os type. Choose from Linux and Windows. Default to
     Linux. Known values are: "Linux" and "Windows".
    :vartype os_type: str or ~azure.mgmt.containerservice.v2019_04_30.models.OSType
    """

    _validation = {
        "count": {"required": True},
        "vm_size": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "count": {"key": "count", "type": "int"},
        "vm_size": {"key": "vmSize", "type": "str"},
        "subnet_cidr": {"key": "subnetCidr", "type": "str"},
        "os_type": {"key": "osType", "type": "str"},
    }

    def __init__(
        self,
        *,
        count: int,
        vm_size: Union[str, "_models.OpenShiftContainerServiceVMSize"],
        name: Optional[str] = None,
        subnet_cidr: Optional[str] = None,
        os_type: Union[str, "_models.OSType"] = "Linux",
        **kwargs
    ):
        """
        :keyword name: Unique name of the master pool profile in the context of the subscription and
         resource group.
        :paramtype name: str
        :keyword count: Number of masters (VMs) to host docker containers. The default value is 3.
         Required.
        :paramtype count: int
        :keyword vm_size: Size of agent VMs. Required. Known values are: "Standard_D2s_v3",
         "Standard_D4s_v3", "Standard_D8s_v3", "Standard_D16s_v3", "Standard_D32s_v3",
         "Standard_D64s_v3", "Standard_DS4_v2", "Standard_DS5_v2", "Standard_F8s_v2",
         "Standard_F16s_v2", "Standard_F32s_v2", "Standard_F64s_v2", "Standard_F72s_v2", "Standard_F8s",
         "Standard_F16s", "Standard_E4s_v3", "Standard_E8s_v3", "Standard_E16s_v3", "Standard_E20s_v3",
         "Standard_E32s_v3", "Standard_E64s_v3", "Standard_GS2", "Standard_GS3", "Standard_GS4",
         "Standard_GS5", "Standard_DS12_v2", "Standard_DS13_v2", "Standard_DS14_v2", "Standard_DS15_v2",
         "Standard_L4s", "Standard_L8s", "Standard_L16s", and "Standard_L32s".
        :paramtype vm_size: str or
         ~azure.mgmt.containerservice.v2019_04_30.models.OpenShiftContainerServiceVMSize
        :keyword subnet_cidr: Subnet CIDR for the peering.
        :paramtype subnet_cidr: str
        :keyword os_type: OsType to be used to specify os type. Choose from Linux and Windows. Default
         to Linux. Known values are: "Linux" and "Windows".
        :paramtype os_type: str or ~azure.mgmt.containerservice.v2019_04_30.models.OSType
        """
        super().__init__(**kwargs)
        self.name = name
        self.count = count
        self.vm_size = vm_size
        self.subnet_cidr = subnet_cidr
        self.os_type = os_type


class OpenShiftRouterProfile(_serialization.Model):
    """Represents an OpenShift router.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the router profile.
    :vartype name: str
    :ivar public_subdomain: DNS subdomain for OpenShift router.
    :vartype public_subdomain: str
    :ivar fqdn: Auto-allocated FQDN for the OpenShift router.
    :vartype fqdn: str
    """

    _validation = {
        "public_subdomain": {"readonly": True},
        "fqdn": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "public_subdomain": {"key": "publicSubdomain", "type": "str"},
        "fqdn": {"key": "fqdn", "type": "str"},
    }

    def __init__(self, *, name: Optional[str] = None, **kwargs):
        """
        :keyword name: Name of the router profile.
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.public_subdomain = None
        self.fqdn = None


class PurchasePlan(_serialization.Model):
    """Used for establishing the purchase context of any 3rd Party artifact through MarketPlace.

    :ivar name: The plan ID.
    :vartype name: str
    :ivar product: Specifies the product of the image from the marketplace. This is the same value
     as Offer under the imageReference element.
    :vartype product: str
    :ivar promotion_code: The promotion code.
    :vartype promotion_code: str
    :ivar publisher: The plan ID.
    :vartype publisher: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "product": {"key": "product", "type": "str"},
        "promotion_code": {"key": "promotionCode", "type": "str"},
        "publisher": {"key": "publisher", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        product: Optional[str] = None,
        promotion_code: Optional[str] = None,
        publisher: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword name: The plan ID.
        :paramtype name: str
        :keyword product: Specifies the product of the image from the marketplace. This is the same
         value as Offer under the imageReference element.
        :paramtype product: str
        :keyword promotion_code: The promotion code.
        :paramtype promotion_code: str
        :keyword publisher: The plan ID.
        :paramtype publisher: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.product = product
        self.promotion_code = promotion_code
        self.publisher = publisher


class TagsObject(_serialization.Model):
    """Tags object for patch operations.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, tags: Optional[Dict[str, str]] = None, **kwargs):
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.tags = tags
