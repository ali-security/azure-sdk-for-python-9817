# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .health_evaluation import HealthEvaluation


class DeployedApplicationHealthEvaluation(HealthEvaluation):
    """Represents health evaluation for a deployed application, containing
    information about the data and the algorithm used by the health store to
    evaluate health.
    .

    :param aggregated_health_state: The health state of a Service Fabric
     entity such as Cluster, Node, Application, Service, Partition, Replica
     etc. Possible values include: 'Invalid', 'Ok', 'Warning', 'Error',
     'Unknown'
    :type aggregated_health_state: str or ~servicefabric.models.HealthState
    :param description: Description of the health evaluation, which represents
     a summary of the evaluation process.
    :type description: str
    :param kind: Constant filled by server.
    :type kind: str
    :param node_name: Name of the node where the application is deployed to.
    :type node_name: str
    :param application_name: The name of the application, including the
     'fabric:' URI scheme.
    :type application_name: str
    :param unhealthy_evaluations: List of  unhealthy evaluations that led to
     the current aggregated health state of the deployed application.
     The types of the unhealthy evaluations can be
     DeployedServicePackagesHealthEvaluation or EventHealthEvaluation.
    :type unhealthy_evaluations:
     list[~servicefabric.models.HealthEvaluationWrapper]
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
    }

    def __init__(self, aggregated_health_state=None, description=None, node_name=None, application_name=None, unhealthy_evaluations=None):
        super(DeployedApplicationHealthEvaluation, self).__init__(aggregated_health_state=aggregated_health_state, description=description)
        self.node_name = node_name
        self.application_name = application_name
        self.unhealthy_evaluations = unhealthy_evaluations
        self.kind = 'DeployedApplication'
