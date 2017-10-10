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


class EventHealthEvaluation(HealthEvaluation):
    """Represents health evaluation of a HealthEvent that was reported on the
    entity.
    The health evaluation is returned when evaluating health of an entity
    results in Error or Warning.
    .

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param description: Description of the health evaluation, which represents
     a summary of the evaluation process.
    :type description: str
    :param kind: Polymorphic Discriminator
    :type kind: str
    :param consider_warning_as_error: Indicates whether warnings are treated
     with the same severity as errors. The field is specified in the health
     policy used to evaluate the entity.
    :type consider_warning_as_error: bool
    :param unhealthy_event:
    :type unhealthy_event: :class:`HealthEvent
     <azure.servicefabric.models.HealthEvent>`
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'consider_warning_as_error': {'key': 'ConsiderWarningAsError', 'type': 'bool'},
        'unhealthy_event': {'key': 'UnhealthyEvent', 'type': 'HealthEvent'},
    }

    def __init__(self, aggregated_health_state=None, description=None, consider_warning_as_error=None, unhealthy_event=None):
        super(EventHealthEvaluation, self).__init__(aggregated_health_state=aggregated_health_state, description=description)
        self.consider_warning_as_error = consider_warning_as_error
        self.unhealthy_event = unhealthy_event
        self.kind = 'Event'
