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


class NodesHealthEvaluation(HealthEvaluation):
    """Represents health evaluation for nodes, containing health evaluations for
    each unhealthy node that impacted current aggregated health state. Can be
    returned when evaluating cluster health and the aggregated health state
    is either Error or Warning.

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str
    :param description: Description of the health evaluation, which
     represents a summary of the evaluation process.
    :type description: str
    :param Kind: Polymorphic Discriminator
    :type Kind: str
    :param max_percent_unhealthy_nodes: Maximum allowed percentage of
     unhealthy nodes from the ClusterHealthPolicy.
    :type max_percent_unhealthy_nodes: int
    :param total_count: Total number of nodes found in the health store.
    :type total_count: long
    :param unhealthy_evaluations:
    :type unhealthy_evaluations: list of :class:`HealthEvaluationWrapper
     <azure.servicefabric.models.HealthEvaluationWrapper>`
    """ 

    _validation = {
        'Kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'Kind': {'key': 'Kind', 'type': 'str'},
        'max_percent_unhealthy_nodes': {'key': 'MaxPercentUnhealthyNodes', 'type': 'int'},
        'total_count': {'key': 'TotalCount', 'type': 'long'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
    }

    def __init__(self, aggregated_health_state=None, description=None, max_percent_unhealthy_nodes=None, total_count=None, unhealthy_evaluations=None):
        super(NodesHealthEvaluation, self).__init__(aggregated_health_state=aggregated_health_state, description=description)
        self.max_percent_unhealthy_nodes = max_percent_unhealthy_nodes
        self.total_count = total_count
        self.unhealthy_evaluations = unhealthy_evaluations
        self.Kind = 'Nodes'
