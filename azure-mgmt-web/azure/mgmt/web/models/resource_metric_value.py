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


class ResourceMetricValue(Model):
    """Value of resource metric.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar timestamp: Value timestamp.
    :vartype timestamp: str
    :ivar average: Value average.
    :vartype average: float
    :ivar minimum: Value minimum.
    :vartype minimum: float
    :ivar maximum: Value maximum.
    :vartype maximum: float
    :ivar total: Value total.
    :vartype total: float
    :ivar count: Value count.
    :vartype count: float
    :ivar properties: Properties.
    :vartype properties: list[~azure.mgmt.web.models.ResourceMetricProperty]
    """

    _validation = {
        'timestamp': {'readonly': True},
        'average': {'readonly': True},
        'minimum': {'readonly': True},
        'maximum': {'readonly': True},
        'total': {'readonly': True},
        'count': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'timestamp': {'key': 'timestamp', 'type': 'str'},
        'average': {'key': 'average', 'type': 'float'},
        'minimum': {'key': 'minimum', 'type': 'float'},
        'maximum': {'key': 'maximum', 'type': 'float'},
        'total': {'key': 'total', 'type': 'float'},
        'count': {'key': 'count', 'type': 'float'},
        'properties': {'key': 'properties', 'type': '[ResourceMetricProperty]'},
    }

    def __init__(self):
        self.timestamp = None
        self.average = None
        self.minimum = None
        self.maximum = None
        self.total = None
        self.count = None
        self.properties = None
