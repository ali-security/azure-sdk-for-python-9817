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


class ApplicationUpgradeDescription(Model):
    """Describes the parameters for an application upgrade. Please note that
    upgrade description replaces the existing application description. This
    means that if the parameters are not specified, the existing parameters on
    the applications will be overwritten with the empty parameters list. This
    would results in application using the default value of the parameters from
    the application manifest. If you do not want to change any existing
    parameter values, please get the application parameters first using the
    GetApplicationInfo query and then supply those values as Parameters in this
    ApplicationUpgradeDescription.

    :param name:
    :type name: str
    :param target_application_type_version:
    :type target_application_type_version: str
    :param parameters:
    :type parameters: list of :class:`ApplicationParameter
     <azure.servicefabric.models.ApplicationParameter>`
    :param upgrade_kind: Possible values include: 'Invalid', 'Rolling'.
     Default value: "Rolling" .
    :type upgrade_kind: str or :class:`enum <azure.servicefabric.models.enum>`
    :param rolling_upgrade_mode: Possible values include: 'Invalid',
     'UnmonitoredAuto', 'UnmonitoredManual', 'Monitored'. Default value:
     "UnmonitoredAuto" .
    :type rolling_upgrade_mode: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param upgrade_replica_set_check_timeout_in_seconds:
    :type upgrade_replica_set_check_timeout_in_seconds: long
    :param force_restart:
    :type force_restart: bool
    :param monitoring_policy:
    :type monitoring_policy: :class:`MonitoringPolicyDescription
     <azure.servicefabric.models.MonitoringPolicyDescription>`
    :param application_health_policy:
    :type application_health_policy: :class:`ApplicationHealthPolicy
     <azure.servicefabric.models.ApplicationHealthPolicy>`
    """

    _validation = {
        'name': {'required': True},
        'target_application_type_version': {'required': True},
        'parameters': {'required': True},
        'upgrade_kind': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'target_application_type_version': {'key': 'TargetApplicationTypeVersion', 'type': 'str'},
        'parameters': {'key': 'Parameters', 'type': '[ApplicationParameter]'},
        'upgrade_kind': {'key': 'UpgradeKind', 'type': 'str'},
        'rolling_upgrade_mode': {'key': 'RollingUpgradeMode', 'type': 'str'},
        'upgrade_replica_set_check_timeout_in_seconds': {'key': 'UpgradeReplicaSetCheckTimeoutInSeconds', 'type': 'long'},
        'force_restart': {'key': 'ForceRestart', 'type': 'bool'},
        'monitoring_policy': {'key': 'MonitoringPolicy', 'type': 'MonitoringPolicyDescription'},
        'application_health_policy': {'key': 'ApplicationHealthPolicy', 'type': 'ApplicationHealthPolicy'},
    }

    def __init__(self, name, target_application_type_version, parameters, upgrade_kind="Rolling", rolling_upgrade_mode="UnmonitoredAuto", upgrade_replica_set_check_timeout_in_seconds=None, force_restart=None, monitoring_policy=None, application_health_policy=None):
        self.name = name
        self.target_application_type_version = target_application_type_version
        self.parameters = parameters
        self.upgrade_kind = upgrade_kind
        self.rolling_upgrade_mode = rolling_upgrade_mode
        self.upgrade_replica_set_check_timeout_in_seconds = upgrade_replica_set_check_timeout_in_seconds
        self.force_restart = force_restart
        self.monitoring_policy = monitoring_policy
        self.application_health_policy = application_health_policy
