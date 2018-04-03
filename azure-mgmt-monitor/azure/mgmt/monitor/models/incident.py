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


class Incident(Model):
    """An alert incident indicates the activation status of an alert rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Incident name.
    :vartype name: str
    :ivar rule_name: Rule name that is associated with the incident.
    :vartype rule_name: str
    :ivar is_active: A boolean to indicate whether the incident is active or
     resolved.
    :vartype is_active: bool
    :ivar activated_time: The time at which the incident was activated in
     ISO8601 format.
    :vartype activated_time: datetime
    :ivar resolved_time: The time at which the incident was resolved in
     ISO8601 format. If null, it means the incident is still active.
    :vartype resolved_time: datetime
    """

    _validation = {
        'name': {'readonly': True},
        'rule_name': {'readonly': True},
        'is_active': {'readonly': True},
        'activated_time': {'readonly': True},
        'resolved_time': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'rule_name': {'key': 'ruleName', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'activated_time': {'key': 'activatedTime', 'type': 'iso-8601'},
        'resolved_time': {'key': 'resolvedTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(Incident, self).__init__(**kwargs)
        self.name = None
        self.rule_name = None
        self.is_active = None
        self.activated_time = None
        self.resolved_time = None
