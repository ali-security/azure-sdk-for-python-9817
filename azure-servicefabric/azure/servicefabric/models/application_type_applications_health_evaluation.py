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


class ApplicationTypeApplicationsHealthEvaluation(HealthEvaluation):
    """Represents health evaluation for applications of a particular application
    type. The application type applications evaluation can be returned when
    cluster health evaluation returns unhealthy aggregated health state, either
    Error or Warning. It contains health evaluations for each unhealthy
    application of the included application type that impacted current
    aggregated health state.

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str or ~azure.servicefabric.models.enum
    :param description: Description of the health evaluation, which represents
     a summary of the evaluation process.
    :type description: str
    :param kind: Constant filled by server.
    :type kind: str
    :param application_type_name:
    :type application_type_name: str
    :param max_percent_unhealthy_applications: Maximum allowed percentage of
     unhealthy applications for the application type, specified as an entry in
     ApplicationTypeHealthPolicyMap.
    :type max_percent_unhealthy_applications: int
    :param total_count: Total number of applications of the application type
     found in the health store.
    :type total_count: long
    :param unhealthy_evaluations:
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
        'application_type_name': {'key': 'ApplicationTypeName', 'type': 'str'},
        'max_percent_unhealthy_applications': {'key': 'MaxPercentUnhealthyApplications', 'type': 'int'},
        'total_count': {'key': 'TotalCount', 'type': 'long'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
    }

    def __init__(self, aggregated_health_state=None, description=None, application_type_name=None, max_percent_unhealthy_applications=None, total_count=None, unhealthy_evaluations=None):
        super(ApplicationTypeApplicationsHealthEvaluation, self).__init__(aggregated_health_state=aggregated_health_state, description=description)
        self.application_type_name = application_type_name
        self.max_percent_unhealthy_applications = max_percent_unhealthy_applications
        self.total_count = total_count
        self.unhealthy_evaluations = unhealthy_evaluations
        self.kind = 'ApplicationTypeApplications'
