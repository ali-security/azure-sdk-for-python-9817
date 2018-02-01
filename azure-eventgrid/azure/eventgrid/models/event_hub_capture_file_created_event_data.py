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


class EventHubCaptureFileCreatedEventData(Model):
    """Schema of the Data property of an EventGridEvent for an
    Microsoft.EventHub.CaptureFileCreated event.

    :param fileurl: The path to the capture file.
    :type fileurl: str
    :param file_type: The file type of the capture file.
    :type file_type: str
    :param partition_id: The shard ID.
    :type partition_id: str
    :param size_in_bytes: The file size.
    :type size_in_bytes: int
    :param event_count: The number of events in the file.
    :type event_count: int
    :param first_sequence_number: The smallest sequence number from the queue.
    :type first_sequence_number: int
    :param last_sequence_number: The last sequence number from the queue.
    :type last_sequence_number: int
    :param first_enqueue_time: The first time from the queue.
    :type first_enqueue_time: datetime
    :param last_enqueue_time: The last time from the queue.
    :type last_enqueue_time: datetime
    """

    _attribute_map = {
        'fileurl': {'key': 'fileurl', 'type': 'str'},
        'file_type': {'key': 'fileType', 'type': 'str'},
        'partition_id': {'key': 'partitionId', 'type': 'str'},
        'size_in_bytes': {'key': 'sizeInBytes', 'type': 'int'},
        'event_count': {'key': 'eventCount', 'type': 'int'},
        'first_sequence_number': {'key': 'firstSequenceNumber', 'type': 'int'},
        'last_sequence_number': {'key': 'lastSequenceNumber', 'type': 'int'},
        'first_enqueue_time': {'key': 'firstEnqueueTime', 'type': 'iso-8601'},
        'last_enqueue_time': {'key': 'lastEnqueueTime', 'type': 'iso-8601'},
    }

    def __init__(self, fileurl=None, file_type=None, partition_id=None, size_in_bytes=None, event_count=None, first_sequence_number=None, last_sequence_number=None, first_enqueue_time=None, last_enqueue_time=None):
        super(EventHubCaptureFileCreatedEventData, self).__init__()
        self.fileurl = fileurl
        self.file_type = file_type
        self.partition_id = partition_id
        self.size_in_bytes = size_in_bytes
        self.event_count = event_count
        self.first_sequence_number = first_sequence_number
        self.last_sequence_number = last_sequence_number
        self.first_enqueue_time = first_enqueue_time
        self.last_enqueue_time = last_enqueue_time
