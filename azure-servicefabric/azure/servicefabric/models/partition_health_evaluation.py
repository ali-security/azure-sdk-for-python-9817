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

from .health_evaluation import HealthEvaluation


class PartitionHealthEvaluation(HealthEvaluation):
    """Represents health evaluation for a partition, containing information about
    the data and the algorithm used by health store to evaluate health. The
    evaluation is returned only when the aggregated health state is either
    Error or Warning.

    All required parameters must be populated in order to send to Azure.

    :param aggregated_health_state: The health state of a Service Fabric
     entity such as Cluster, Node, Application, Service, Partition, Replica
     etc. Possible values include: 'Invalid', 'Ok', 'Warning', 'Error',
     'Unknown'
    :type aggregated_health_state: str or
     ~azure.servicefabric.models.HealthState
    :param description: Description of the health evaluation, which represents
     a summary of the evaluation process.
    :type description: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param partition_id: Id of the partition whose health evaluation is
     described by this object.
    :type partition_id: str
    :param unhealthy_evaluations: List of unhealthy evaluations that led to
     the current aggregated health state of the partition. The types of the
     unhealthy evaluations can be ReplicasHealthEvaluation or
     EventHealthEvaluation.
    :type unhealthy_evaluations:
     list[~azure.servicefabric.models.HealthEvaluationWrapper]
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
    }

    def __init__(self, **kwargs):
        super(PartitionHealthEvaluation, self).__init__(**kwargs)
        self.partition_id = kwargs.get('partition_id', None)
        self.unhealthy_evaluations = kwargs.get('unhealthy_evaluations', None)
        self.kind = 'Partition'
