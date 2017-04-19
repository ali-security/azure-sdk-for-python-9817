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

from .rule_condition import RuleCondition


class ManagementEventRuleCondition(RuleCondition):
    """A management event rule condition.

    :param data_source: the resource from which the rule collects its data.
     For this type dataSource will always be of type RuleMetricDataSource.
    :type data_source: :class:`RuleDataSource
     <azure.mgmt.monitor.models.RuleDataSource>`
    :param odatatype: Polymorphic Discriminator
    :type odatatype: str
    :param aggregation: How the data that is collected should be combined over
     time and when the alert is activated. Note that for management event
     alerts aggregation is optional – if it is not provided then any event will
     cause the alert to activate.
    :type aggregation: :class:`ManagementEventAggregationCondition
     <azure.mgmt.monitor.models.ManagementEventAggregationCondition>`
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'data_source': {'key': 'dataSource', 'type': 'RuleDataSource'},
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'aggregation': {'key': 'aggregation', 'type': 'ManagementEventAggregationCondition'},
    }

    def __init__(self, data_source=None, aggregation=None):
        super(ManagementEventRuleCondition, self).__init__(data_source=data_source)
        self.aggregation = aggregation
        self.odatatype = 'Microsoft.Azure.Management.Insights.Models.ManagementEventRuleCondition'
