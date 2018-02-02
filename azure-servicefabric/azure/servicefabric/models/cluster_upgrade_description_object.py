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


class ClusterUpgradeDescriptionObject(Model):
    """Represents a ServiceFabric cluster upgrade.

    :param config_version:
    :type config_version: str
    :param code_version:
    :type code_version: str
    :param upgrade_kind: Possible values include: 'Invalid', 'Rolling'.
     Default value: "Rolling" .
    :type upgrade_kind: str or ~azure.servicefabric.models.enum
    :param rolling_upgrade_mode: Possible values include: 'Invalid',
     'UnmonitoredAuto', 'UnmonitoredManual', 'Monitored'. Default value:
     "UnmonitoredAuto" .
    :type rolling_upgrade_mode: str or ~azure.servicefabric.models.enum
    :param upgrade_replica_set_check_timeout_in_seconds:
    :type upgrade_replica_set_check_timeout_in_seconds: long
    :param force_restart:
    :type force_restart: bool
    :param enable_delta_health_evaluation:
    :type enable_delta_health_evaluation: bool
    :param monitoring_policy:
    :type monitoring_policy:
     ~azure.servicefabric.models.MonitoringPolicyDescription
    :param cluster_health_policy:
    :type cluster_health_policy:
     ~azure.servicefabric.models.ClusterHealthPolicy
    :param cluster_upgrade_health_policy:
    :type cluster_upgrade_health_policy:
     ~azure.servicefabric.models.ClusterUpgradeHealthPolicyObject
    :param application_health_policy_map:
    :type application_health_policy_map:
     list[~azure.servicefabric.models.ApplicationHealthPolicyMapItem]
    """

    _attribute_map = {
        'config_version': {'key': 'ConfigVersion', 'type': 'str'},
        'code_version': {'key': 'CodeVersion', 'type': 'str'},
        'upgrade_kind': {'key': 'UpgradeKind', 'type': 'str'},
        'rolling_upgrade_mode': {'key': 'RollingUpgradeMode', 'type': 'str'},
        'upgrade_replica_set_check_timeout_in_seconds': {'key': 'UpgradeReplicaSetCheckTimeoutInSeconds', 'type': 'long'},
        'force_restart': {'key': 'ForceRestart', 'type': 'bool'},
        'enable_delta_health_evaluation': {'key': 'EnableDeltaHealthEvaluation', 'type': 'bool'},
        'monitoring_policy': {'key': 'MonitoringPolicy', 'type': 'MonitoringPolicyDescription'},
        'cluster_health_policy': {'key': 'ClusterHealthPolicy', 'type': 'ClusterHealthPolicy'},
        'cluster_upgrade_health_policy': {'key': 'ClusterUpgradeHealthPolicy', 'type': 'ClusterUpgradeHealthPolicyObject'},
        'application_health_policy_map': {'key': 'ApplicationHealthPolicyMap', 'type': '[ApplicationHealthPolicyMapItem]'},
    }

    def __init__(self, config_version=None, code_version=None, upgrade_kind="Rolling", rolling_upgrade_mode="UnmonitoredAuto", upgrade_replica_set_check_timeout_in_seconds=None, force_restart=None, enable_delta_health_evaluation=None, monitoring_policy=None, cluster_health_policy=None, cluster_upgrade_health_policy=None, application_health_policy_map=None):
        super(ClusterUpgradeDescriptionObject, self).__init__()
        self.config_version = config_version
        self.code_version = code_version
        self.upgrade_kind = upgrade_kind
        self.rolling_upgrade_mode = rolling_upgrade_mode
        self.upgrade_replica_set_check_timeout_in_seconds = upgrade_replica_set_check_timeout_in_seconds
        self.force_restart = force_restart
        self.enable_delta_health_evaluation = enable_delta_health_evaluation
        self.monitoring_policy = monitoring_policy
        self.cluster_health_policy = cluster_health_policy
        self.cluster_upgrade_health_policy = cluster_upgrade_health_policy
        self.application_health_policy_map = application_health_policy_map
