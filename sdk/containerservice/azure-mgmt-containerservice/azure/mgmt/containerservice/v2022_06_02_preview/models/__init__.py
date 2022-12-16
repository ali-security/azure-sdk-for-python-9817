# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AgentPool
from ._models_py3 import AgentPoolAvailableVersions
from ._models_py3 import AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem
from ._models_py3 import AgentPoolListResult
from ._models_py3 import AgentPoolUpgradeProfile
from ._models_py3 import AgentPoolUpgradeProfilePropertiesUpgradesItem
from ._models_py3 import AgentPoolUpgradeSettings
from ._models_py3 import AzureEntityResource
from ._models_py3 import AzureKeyVaultKms
from ._models_py3 import CloudErrorBody
from ._models_py3 import ContainerServiceDiagnosticsProfile
from ._models_py3 import ContainerServiceLinuxProfile
from ._models_py3 import ContainerServiceMasterProfile
from ._models_py3 import ContainerServiceNetworkProfile
from ._models_py3 import ContainerServiceSshConfiguration
from ._models_py3 import ContainerServiceSshPublicKey
from ._models_py3 import ContainerServiceVMDiagnostics
from ._models_py3 import CreationData
from ._models_py3 import CredentialResult
from ._models_py3 import CredentialResults
from ._models_py3 import EndpointDependency
from ._models_py3 import EndpointDetail
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ExtendedLocation
from ._models_py3 import Fleet
from ._models_py3 import FleetCredentialResult
from ._models_py3 import FleetCredentialResults
from ._models_py3 import FleetHubProfile
from ._models_py3 import FleetListResult
from ._models_py3 import FleetMember
from ._models_py3 import FleetMembersListResult
from ._models_py3 import FleetPatch
from ._models_py3 import KubeletConfig
from ._models_py3 import LinuxOSConfig
from ._models_py3 import MaintenanceConfiguration
from ._models_py3 import MaintenanceConfigurationListResult
from ._models_py3 import ManagedCluster
from ._models_py3 import ManagedClusterAADProfile
from ._models_py3 import ManagedClusterAPIServerAccessProfile
from ._models_py3 import ManagedClusterAccessProfile
from ._models_py3 import ManagedClusterAddonProfile
from ._models_py3 import ManagedClusterAddonProfileIdentity
from ._models_py3 import ManagedClusterAgentPoolProfile
from ._models_py3 import ManagedClusterAgentPoolProfileProperties
from ._models_py3 import ManagedClusterAutoUpgradeProfile
from ._models_py3 import ManagedClusterHTTPProxyConfig
from ._models_py3 import ManagedClusterIdentity
from ._models_py3 import ManagedClusterIngressProfile
from ._models_py3 import ManagedClusterIngressProfileWebAppRouting
from ._models_py3 import ManagedClusterListResult
from ._models_py3 import ManagedClusterLoadBalancerProfile
from ._models_py3 import ManagedClusterLoadBalancerProfileManagedOutboundIPs
from ._models_py3 import ManagedClusterLoadBalancerProfileOutboundIPPrefixes
from ._models_py3 import ManagedClusterLoadBalancerProfileOutboundIPs
from ._models_py3 import ManagedClusterManagedOutboundIPProfile
from ._models_py3 import ManagedClusterNATGatewayProfile
from ._models_py3 import ManagedClusterOIDCIssuerProfile
from ._models_py3 import ManagedClusterPodIdentity
from ._models_py3 import ManagedClusterPodIdentityException
from ._models_py3 import ManagedClusterPodIdentityProfile
from ._models_py3 import ManagedClusterPodIdentityProvisioningError
from ._models_py3 import ManagedClusterPodIdentityProvisioningErrorBody
from ._models_py3 import ManagedClusterPodIdentityProvisioningInfo
from ._models_py3 import ManagedClusterPoolUpgradeProfile
from ._models_py3 import ManagedClusterPoolUpgradeProfileUpgradesItem
from ._models_py3 import ManagedClusterPropertiesAutoScalerProfile
from ._models_py3 import ManagedClusterPropertiesForSnapshot
from ._models_py3 import ManagedClusterSKU
from ._models_py3 import ManagedClusterSecurityProfile
from ._models_py3 import ManagedClusterSecurityProfileDefender
from ._models_py3 import ManagedClusterSecurityProfileDefenderSecurityMonitoring
from ._models_py3 import ManagedClusterSecurityProfileNodeRestriction
from ._models_py3 import ManagedClusterSecurityProfileWorkloadIdentity
from ._models_py3 import ManagedClusterServicePrincipalProfile
from ._models_py3 import ManagedClusterSnapshot
from ._models_py3 import ManagedClusterSnapshotListResult
from ._models_py3 import ManagedClusterStorageProfile
from ._models_py3 import ManagedClusterStorageProfileBlobCSIDriver
from ._models_py3 import ManagedClusterStorageProfileDiskCSIDriver
from ._models_py3 import ManagedClusterStorageProfileFileCSIDriver
from ._models_py3 import ManagedClusterStorageProfileSnapshotController
from ._models_py3 import ManagedClusterUpgradeProfile
from ._models_py3 import ManagedClusterWindowsProfile
from ._models_py3 import ManagedClusterWorkloadAutoScalerProfile
from ._models_py3 import ManagedClusterWorkloadAutoScalerProfileKeda
from ._models_py3 import ManagedServiceIdentityUserAssignedIdentitiesValue
from ._models_py3 import NetworkProfileForSnapshot
from ._models_py3 import OSOptionProfile
from ._models_py3 import OSOptionProperty
from ._models_py3 import OperationListResult
from ._models_py3 import OperationValue
from ._models_py3 import OutboundEnvironmentEndpoint
from ._models_py3 import OutboundEnvironmentEndpointCollection
from ._models_py3 import PowerState
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourcesListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import Resource
from ._models_py3 import ResourceReference
from ._models_py3 import RunCommandRequest
from ._models_py3 import RunCommandResult
from ._models_py3 import Snapshot
from ._models_py3 import SnapshotListResult
from ._models_py3 import SubResource
from ._models_py3 import SysctlConfig
from ._models_py3 import SystemData
from ._models_py3 import TagsObject
from ._models_py3 import TimeInWeek
from ._models_py3 import TimeSpan
from ._models_py3 import TrackedResource
from ._models_py3 import TrustedAccessRole
from ._models_py3 import TrustedAccessRoleBinding
from ._models_py3 import TrustedAccessRoleBindingListResult
from ._models_py3 import TrustedAccessRoleListResult
from ._models_py3 import TrustedAccessRoleRule
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import WindowsGmsaProfile

from ._container_service_client_enums import AgentPoolMode
from ._container_service_client_enums import AgentPoolType
from ._container_service_client_enums import Code
from ._container_service_client_enums import ConnectionStatus
from ._container_service_client_enums import ContainerServiceStorageProfileTypes
from ._container_service_client_enums import ContainerServiceVMSizeTypes
from ._container_service_client_enums import Count
from ._container_service_client_enums import CreatedByType
from ._container_service_client_enums import Expander
from ._container_service_client_enums import ExtendedLocationTypes
from ._container_service_client_enums import FleetMemberProvisioningState
from ._container_service_client_enums import FleetProvisioningState
from ._container_service_client_enums import Format
from ._container_service_client_enums import GPUInstanceProfile
from ._container_service_client_enums import IpFamily
from ._container_service_client_enums import KeyVaultNetworkAccessTypes
from ._container_service_client_enums import KubeletDiskType
from ._container_service_client_enums import LicenseType
from ._container_service_client_enums import LoadBalancerSku
from ._container_service_client_enums import ManagedClusterPodIdentityProvisioningState
from ._container_service_client_enums import ManagedClusterSKUName
from ._container_service_client_enums import ManagedClusterSKUTier
from ._container_service_client_enums import NetworkMode
from ._container_service_client_enums import NetworkPlugin
from ._container_service_client_enums import NetworkPluginMode
from ._container_service_client_enums import NetworkPolicy
from ._container_service_client_enums import OSDiskType
from ._container_service_client_enums import OSSKU
from ._container_service_client_enums import OSType
from ._container_service_client_enums import OutboundType
from ._container_service_client_enums import PrivateEndpointConnectionProvisioningState
from ._container_service_client_enums import PublicNetworkAccess
from ._container_service_client_enums import ResourceIdentityType
from ._container_service_client_enums import ScaleDownMode
from ._container_service_client_enums import ScaleSetEvictionPolicy
from ._container_service_client_enums import ScaleSetPriority
from ._container_service_client_enums import SnapshotType
from ._container_service_client_enums import TrustedAccessRoleBindingProvisioningState
from ._container_service_client_enums import UpgradeChannel
from ._container_service_client_enums import WeekDay
from ._container_service_client_enums import WorkloadRuntime
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AgentPool",
    "AgentPoolAvailableVersions",
    "AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem",
    "AgentPoolListResult",
    "AgentPoolUpgradeProfile",
    "AgentPoolUpgradeProfilePropertiesUpgradesItem",
    "AgentPoolUpgradeSettings",
    "AzureEntityResource",
    "AzureKeyVaultKms",
    "CloudErrorBody",
    "ContainerServiceDiagnosticsProfile",
    "ContainerServiceLinuxProfile",
    "ContainerServiceMasterProfile",
    "ContainerServiceNetworkProfile",
    "ContainerServiceSshConfiguration",
    "ContainerServiceSshPublicKey",
    "ContainerServiceVMDiagnostics",
    "CreationData",
    "CredentialResult",
    "CredentialResults",
    "EndpointDependency",
    "EndpointDetail",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExtendedLocation",
    "Fleet",
    "FleetCredentialResult",
    "FleetCredentialResults",
    "FleetHubProfile",
    "FleetListResult",
    "FleetMember",
    "FleetMembersListResult",
    "FleetPatch",
    "KubeletConfig",
    "LinuxOSConfig",
    "MaintenanceConfiguration",
    "MaintenanceConfigurationListResult",
    "ManagedCluster",
    "ManagedClusterAADProfile",
    "ManagedClusterAPIServerAccessProfile",
    "ManagedClusterAccessProfile",
    "ManagedClusterAddonProfile",
    "ManagedClusterAddonProfileIdentity",
    "ManagedClusterAgentPoolProfile",
    "ManagedClusterAgentPoolProfileProperties",
    "ManagedClusterAutoUpgradeProfile",
    "ManagedClusterHTTPProxyConfig",
    "ManagedClusterIdentity",
    "ManagedClusterIngressProfile",
    "ManagedClusterIngressProfileWebAppRouting",
    "ManagedClusterListResult",
    "ManagedClusterLoadBalancerProfile",
    "ManagedClusterLoadBalancerProfileManagedOutboundIPs",
    "ManagedClusterLoadBalancerProfileOutboundIPPrefixes",
    "ManagedClusterLoadBalancerProfileOutboundIPs",
    "ManagedClusterManagedOutboundIPProfile",
    "ManagedClusterNATGatewayProfile",
    "ManagedClusterOIDCIssuerProfile",
    "ManagedClusterPodIdentity",
    "ManagedClusterPodIdentityException",
    "ManagedClusterPodIdentityProfile",
    "ManagedClusterPodIdentityProvisioningError",
    "ManagedClusterPodIdentityProvisioningErrorBody",
    "ManagedClusterPodIdentityProvisioningInfo",
    "ManagedClusterPoolUpgradeProfile",
    "ManagedClusterPoolUpgradeProfileUpgradesItem",
    "ManagedClusterPropertiesAutoScalerProfile",
    "ManagedClusterPropertiesForSnapshot",
    "ManagedClusterSKU",
    "ManagedClusterSecurityProfile",
    "ManagedClusterSecurityProfileDefender",
    "ManagedClusterSecurityProfileDefenderSecurityMonitoring",
    "ManagedClusterSecurityProfileNodeRestriction",
    "ManagedClusterSecurityProfileWorkloadIdentity",
    "ManagedClusterServicePrincipalProfile",
    "ManagedClusterSnapshot",
    "ManagedClusterSnapshotListResult",
    "ManagedClusterStorageProfile",
    "ManagedClusterStorageProfileBlobCSIDriver",
    "ManagedClusterStorageProfileDiskCSIDriver",
    "ManagedClusterStorageProfileFileCSIDriver",
    "ManagedClusterStorageProfileSnapshotController",
    "ManagedClusterUpgradeProfile",
    "ManagedClusterWindowsProfile",
    "ManagedClusterWorkloadAutoScalerProfile",
    "ManagedClusterWorkloadAutoScalerProfileKeda",
    "ManagedServiceIdentityUserAssignedIdentitiesValue",
    "NetworkProfileForSnapshot",
    "OSOptionProfile",
    "OSOptionProperty",
    "OperationListResult",
    "OperationValue",
    "OutboundEnvironmentEndpoint",
    "OutboundEnvironmentEndpointCollection",
    "PowerState",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourcesListResult",
    "PrivateLinkServiceConnectionState",
    "Resource",
    "ResourceReference",
    "RunCommandRequest",
    "RunCommandResult",
    "Snapshot",
    "SnapshotListResult",
    "SubResource",
    "SysctlConfig",
    "SystemData",
    "TagsObject",
    "TimeInWeek",
    "TimeSpan",
    "TrackedResource",
    "TrustedAccessRole",
    "TrustedAccessRoleBinding",
    "TrustedAccessRoleBindingListResult",
    "TrustedAccessRoleListResult",
    "TrustedAccessRoleRule",
    "UserAssignedIdentity",
    "WindowsGmsaProfile",
    "AgentPoolMode",
    "AgentPoolType",
    "Code",
    "ConnectionStatus",
    "ContainerServiceStorageProfileTypes",
    "ContainerServiceVMSizeTypes",
    "Count",
    "CreatedByType",
    "Expander",
    "ExtendedLocationTypes",
    "FleetMemberProvisioningState",
    "FleetProvisioningState",
    "Format",
    "GPUInstanceProfile",
    "IpFamily",
    "KeyVaultNetworkAccessTypes",
    "KubeletDiskType",
    "LicenseType",
    "LoadBalancerSku",
    "ManagedClusterPodIdentityProvisioningState",
    "ManagedClusterSKUName",
    "ManagedClusterSKUTier",
    "NetworkMode",
    "NetworkPlugin",
    "NetworkPluginMode",
    "NetworkPolicy",
    "OSDiskType",
    "OSSKU",
    "OSType",
    "OutboundType",
    "PrivateEndpointConnectionProvisioningState",
    "PublicNetworkAccess",
    "ResourceIdentityType",
    "ScaleDownMode",
    "ScaleSetEvictionPolicy",
    "ScaleSetPriority",
    "SnapshotType",
    "TrustedAccessRoleBindingProvisioningState",
    "UpgradeChannel",
    "WeekDay",
    "WorkloadRuntime",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
