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

from msrest.serialization import Model


class VirtualMachineScaleSetVMInstanceView(Model):
    """The instance view of a virtual machine scale set VM.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param platform_update_domain: The Update Domain count.
    :type platform_update_domain: int
    :param platform_fault_domain: The Fault Domain count.
    :type platform_fault_domain: int
    :param rdp_thumb_print: The Remote desktop certificate thumbprint.
    :type rdp_thumb_print: str
    :param vm_agent: The VM Agent running on the virtual machine.
    :type vm_agent:
     ~azure.mgmt.compute.v2017_12_01.models.VirtualMachineAgentInstanceView
    :param maintenance_redeploy_status: The Maintenance Operation status on
     the virtual machine.
    :type maintenance_redeploy_status:
     ~azure.mgmt.compute.v2017_12_01.models.MaintenanceRedeployStatus
    :param disks: The disks information.
    :type disks: list[~azure.mgmt.compute.v2017_12_01.models.DiskInstanceView]
    :param extensions: The extensions information.
    :type extensions:
     list[~azure.mgmt.compute.v2017_12_01.models.VirtualMachineExtensionInstanceView]
    :ivar vm_health: The health status for the VM.
    :vartype vm_health:
     ~azure.mgmt.compute.v2017_12_01.models.VirtualMachineHealthStatus
    :param boot_diagnostics: Boot Diagnostics is a debugging feature which
     allows you to view Console Output and Screenshot to diagnose VM status.
     <br><br> For Linux Virtual Machines, you can easily view the output of
     your console log. <br><br> For both Windows and Linux virtual machines,
     Azure also enables you to see a screenshot of the VM from the hypervisor.
    :type boot_diagnostics:
     ~azure.mgmt.compute.v2017_12_01.models.BootDiagnosticsInstanceView
    :param statuses: The resource status information.
    :type statuses:
     list[~azure.mgmt.compute.v2017_12_01.models.InstanceViewStatus]
    :param placement_group_id: The placement group in which the VM is running.
     If the VM is deallocated it will not have a placementGroupId.
    :type placement_group_id: str
    """

    _validation = {
        'vm_health': {'readonly': True},
    }

    _attribute_map = {
        'platform_update_domain': {'key': 'platformUpdateDomain', 'type': 'int'},
        'platform_fault_domain': {'key': 'platformFaultDomain', 'type': 'int'},
        'rdp_thumb_print': {'key': 'rdpThumbPrint', 'type': 'str'},
        'vm_agent': {'key': 'vmAgent', 'type': 'VirtualMachineAgentInstanceView'},
        'maintenance_redeploy_status': {'key': 'maintenanceRedeployStatus', 'type': 'MaintenanceRedeployStatus'},
        'disks': {'key': 'disks', 'type': '[DiskInstanceView]'},
        'extensions': {'key': 'extensions', 'type': '[VirtualMachineExtensionInstanceView]'},
        'vm_health': {'key': 'vmHealth', 'type': 'VirtualMachineHealthStatus'},
        'boot_diagnostics': {'key': 'bootDiagnostics', 'type': 'BootDiagnosticsInstanceView'},
        'statuses': {'key': 'statuses', 'type': '[InstanceViewStatus]'},
        'placement_group_id': {'key': 'placementGroupId', 'type': 'str'},
    }

    def __init__(self, *, platform_update_domain: int=None, platform_fault_domain: int=None, rdp_thumb_print: str=None, vm_agent=None, maintenance_redeploy_status=None, disks=None, extensions=None, boot_diagnostics=None, statuses=None, placement_group_id: str=None, **kwargs) -> None:
        super(VirtualMachineScaleSetVMInstanceView, self).__init__(**kwargs)
        self.platform_update_domain = platform_update_domain
        self.platform_fault_domain = platform_fault_domain
        self.rdp_thumb_print = rdp_thumb_print
        self.vm_agent = vm_agent
        self.maintenance_redeploy_status = maintenance_redeploy_status
        self.disks = disks
        self.extensions = extensions
        self.vm_health = None
        self.boot_diagnostics = boot_diagnostics
        self.statuses = statuses
        self.placement_group_id = placement_group_id
