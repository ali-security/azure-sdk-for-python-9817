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

from .service_description import ServiceDescription


class StatefulServiceDescription(ServiceDescription):
    """Describes a stateful service.

    :param application_name:
    :type application_name: str
    :param service_name:
    :type service_name: str
    :param service_type_name:
    :type service_type_name: str
    :param initialization_data:
    :type initialization_data: list of int
    :param partition_description:
    :type partition_description: :class:`PartitionSchemeDescription
     <azure.servicefabric.models.PartitionSchemeDescription>`
    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and allow
     for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme:
    :type correlation_scheme: list of :class:`ServiceCorrelationDescription
     <azure.servicefabric.models.ServiceCorrelationDescription>`
    :param service_load_metrics:
    :type service_load_metrics: list of :class:`ServiceLoadMetricDescription
     <azure.servicefabric.models.ServiceLoadMetricDescription>`
    :param service_placement_policies:
    :type service_placement_policies: list of
     :class:`ServicePlacementPolicyDescription
     <azure.servicefabric.models.ServicePlacementPolicyDescription>`
    :param default_move_cost: Possible values include: 'Zero', 'Low',
     'Medium', 'High'
    :type default_move_cost: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param is_default_move_cost_specified: Indicates if the DefaultMoveCost
     property is specified.
    :type is_default_move_cost_specified: bool
    :param service_package_activation_mode: Possible values include:
     'SharedProcess', 'ExclusiveProcess'
    :type service_package_activation_mode: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param service_dns_name: The DNS name of the service. It requires the DNS
     system service to be enabled in Service Fabric cluster.
    :type service_dns_name: str
    :param service_kind: Polymorphic Discriminator
    :type service_kind: str
    :param target_replica_set_size: The target replica set size as a number.
    :type target_replica_set_size: int
    :param min_replica_set_size: The minimum replica set size as a number.
    :type min_replica_set_size: int
    :param has_persisted_state: A flag indicating whether this is a persistent
     service which stores states on the local disk. If it is then the value of
     this property is true, if not it is false.
    :type has_persisted_state: bool
    :param flags: Flags indicating whether other properties are set. Each of
     the associated properties corresponds to a flag, specified below, which,
     if set, indicate that the property is specified.
     This property can be a combination of those flags obtained using bitwise
     'OR' operator.
     For example, if the provided value is 6 then the flags for
     QuorumLossWaitDuration (2) and StandByReplicaKeepDuration(4) are set.
     - None - Does not indicate any other properties are set. The value is
     zero.
     - ReplicaRestartWaitDuration - Indicates the ReplicaRestartWaitDuration
     property is set. The value is 1.
     - QuorumLossWaitDuration - Indicates the QuorumLossWaitDuration property
     is set. The value is 2.
     - StandByReplicaKeepDuration - Indicates the StandByReplicaKeepDuration
     property is set. The value is 4.
    :type flags: int
    :param replica_restart_wait_duration_seconds: The duration, in seconds,
     between when a replica goes down and when a new replica is created.
    :type replica_restart_wait_duration_seconds: long
    :param quorum_loss_wait_duration_seconds: The maximum duration, in
     seconds, for which a partition is allowed to be in a state of quorum loss.
    :type quorum_loss_wait_duration_seconds: long
    :param stand_by_replica_keep_duration_seconds: The definition on how long
     StandBy replicas should be maintained before being removed.
    :type stand_by_replica_keep_duration_seconds: long
    """

    _validation = {
        'service_name': {'required': True},
        'service_type_name': {'required': True},
        'partition_description': {'required': True},
        'service_kind': {'required': True},
        'target_replica_set_size': {'required': True, 'minimum': 1},
        'min_replica_set_size': {'required': True, 'minimum': 1},
        'has_persisted_state': {'required': True},
        'replica_restart_wait_duration_seconds': {'maximum': 4294967295, 'minimum': 0},
        'quorum_loss_wait_duration_seconds': {'maximum': 4294967295, 'minimum': 0},
        'stand_by_replica_keep_duration_seconds': {'maximum': 4294967295, 'minimum': 0},
    }

    _attribute_map = {
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'service_type_name': {'key': 'ServiceTypeName', 'type': 'str'},
        'initialization_data': {'key': 'InitializationData', 'type': '[int]'},
        'partition_description': {'key': 'PartitionDescription', 'type': 'PartitionSchemeDescription'},
        'placement_constraints': {'key': 'PlacementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'CorrelationScheme', 'type': '[ServiceCorrelationDescription]'},
        'service_load_metrics': {'key': 'ServiceLoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'ServicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'DefaultMoveCost', 'type': 'str'},
        'is_default_move_cost_specified': {'key': 'IsDefaultMoveCostSpecified', 'type': 'bool'},
        'service_package_activation_mode': {'key': 'ServicePackageActivationMode', 'type': 'str'},
        'service_dns_name': {'key': 'ServiceDnsName', 'type': 'str'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'target_replica_set_size': {'key': 'TargetReplicaSetSize', 'type': 'int'},
        'min_replica_set_size': {'key': 'MinReplicaSetSize', 'type': 'int'},
        'has_persisted_state': {'key': 'HasPersistedState', 'type': 'bool'},
        'flags': {'key': 'Flags', 'type': 'int'},
        'replica_restart_wait_duration_seconds': {'key': 'ReplicaRestartWaitDurationSeconds', 'type': 'long'},
        'quorum_loss_wait_duration_seconds': {'key': 'QuorumLossWaitDurationSeconds', 'type': 'long'},
        'stand_by_replica_keep_duration_seconds': {'key': 'StandByReplicaKeepDurationSeconds', 'type': 'long'},
    }

    def __init__(self, service_name, service_type_name, partition_description, target_replica_set_size, min_replica_set_size, has_persisted_state, application_name=None, initialization_data=None, placement_constraints=None, correlation_scheme=None, service_load_metrics=None, service_placement_policies=None, default_move_cost=None, is_default_move_cost_specified=None, service_package_activation_mode=None, service_dns_name=None, flags=None, replica_restart_wait_duration_seconds=None, quorum_loss_wait_duration_seconds=None, stand_by_replica_keep_duration_seconds=None):
        super(StatefulServiceDescription, self).__init__(application_name=application_name, service_name=service_name, service_type_name=service_type_name, initialization_data=initialization_data, partition_description=partition_description, placement_constraints=placement_constraints, correlation_scheme=correlation_scheme, service_load_metrics=service_load_metrics, service_placement_policies=service_placement_policies, default_move_cost=default_move_cost, is_default_move_cost_specified=is_default_move_cost_specified, service_package_activation_mode=service_package_activation_mode, service_dns_name=service_dns_name)
        self.target_replica_set_size = target_replica_set_size
        self.min_replica_set_size = min_replica_set_size
        self.has_persisted_state = has_persisted_state
        self.flags = flags
        self.replica_restart_wait_duration_seconds = replica_restart_wait_duration_seconds
        self.quorum_loss_wait_duration_seconds = quorum_loss_wait_duration_seconds
        self.stand_by_replica_keep_duration_seconds = stand_by_replica_keep_duration_seconds
        self.service_kind = 'Stateful'
