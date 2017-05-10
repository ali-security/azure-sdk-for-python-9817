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

from .resource import Resource


class VirtualMachineScaleSet(Resource):
    """Describes a Virtual Machine Scale Set.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param sku: The virtual machine scale set sku.
    :type sku: :class:`Sku
     <azure.mgmt.compute.compute.v2016_03_30.models.Sku>`
    :param upgrade_policy: The upgrade policy.
    :type upgrade_policy: :class:`UpgradePolicy
     <azure.mgmt.compute.compute.v2016_03_30.models.UpgradePolicy>`
    :param virtual_machine_profile: The virtual machine profile.
    :type virtual_machine_profile: :class:`VirtualMachineScaleSetVMProfile
     <azure.mgmt.compute.compute.v2016_03_30.models.VirtualMachineScaleSetVMProfile>`
    :ivar provisioning_state: The provisioning state, which only appears in
     the response.
    :vartype provisioning_state: str
    :param overprovision: Specifies whether the Virtual Machine Scale Set
     should be overprovisioned.
    :type overprovision: bool
    :param identity: The identity of the virtual machine scale set, if
     configured.
    :type identity: :class:`VirtualMachineScaleSetIdentity
     <azure.mgmt.compute.compute.v2016_03_30.models.VirtualMachineScaleSetIdentity>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'upgrade_policy': {'key': 'properties.upgradePolicy', 'type': 'UpgradePolicy'},
        'virtual_machine_profile': {'key': 'properties.virtualMachineProfile', 'type': 'VirtualMachineScaleSetVMProfile'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'overprovision': {'key': 'properties.overprovision', 'type': 'bool'},
        'identity': {'key': 'identity', 'type': 'VirtualMachineScaleSetIdentity'},
    }

    def __init__(self, location, tags=None, sku=None, upgrade_policy=None, virtual_machine_profile=None, overprovision=None, identity=None):
        super(VirtualMachineScaleSet, self).__init__(location=location, tags=tags)
        self.sku = sku
        self.upgrade_policy = upgrade_policy
        self.virtual_machine_profile = virtual_machine_profile
        self.provisioning_state = None
        self.overprovision = overprovision
        self.identity = identity
