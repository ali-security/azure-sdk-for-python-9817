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


class ContainerEvent(Model):
    """A container event.

    :param count: The count of the event.
    :type count: int
    :param first_timestamp: Date/time of the first event.
    :type first_timestamp: datetime
    :param last_timestamp: Date/time of the last event.
    :type last_timestamp: datetime
    :param message: The event message
    :type message: str
    :param type: The event type.
    :type type: str
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'first_timestamp': {'key': 'firstTimestamp', 'type': 'iso-8601'},
        'last_timestamp': {'key': 'lastTimestamp', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, count=None, first_timestamp=None, last_timestamp=None, message=None, type=None):
        self.count = count
        self.first_timestamp = first_timestamp
        self.last_timestamp = last_timestamp
        self.message = message
        self.type = type
