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

from .secondary_replicator_status_py3 import SecondaryReplicatorStatus


class SecondaryIdleReplicatorStatus(SecondaryReplicatorStatus):
    """Status of the secondary replicator when it is in idle mode and is being
    built by the primary.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    :param replication_queue_status: Details about the replication queue on
     the secondary replicator.
    :type replication_queue_status:
     ~azure.servicefabric.models.ReplicatorQueueStatus
    :param last_replication_operation_received_time_utc: The last time-stamp
     (UTC) at which a replication operation was received from the primary.
     UTC 0 represents an invalid value, indicating that a replication operation
     message was never received.
    :type last_replication_operation_received_time_utc: datetime
    :param is_in_build: Value that indicates whether the replica is currently
     being built.
    :type is_in_build: bool
    :param copy_queue_status: Details about the copy queue on the secondary
     replicator.
    :type copy_queue_status: ~azure.servicefabric.models.ReplicatorQueueStatus
    :param last_copy_operation_received_time_utc: The last time-stamp (UTC) at
     which a copy operation was received from the primary.
     UTC 0 represents an invalid value, indicating that a copy operation
     message was never received.
    :type last_copy_operation_received_time_utc: datetime
    :param last_acknowledgement_sent_time_utc: The last time-stamp (UTC) at
     which an acknowledgment was sent to the primary replicator.
     UTC 0 represents an invalid value, indicating that an acknowledgment
     message was never sent.
    :type last_acknowledgement_sent_time_utc: datetime
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
        'replication_queue_status': {'key': 'ReplicationQueueStatus', 'type': 'ReplicatorQueueStatus'},
        'last_replication_operation_received_time_utc': {'key': 'LastReplicationOperationReceivedTimeUtc', 'type': 'iso-8601'},
        'is_in_build': {'key': 'IsInBuild', 'type': 'bool'},
        'copy_queue_status': {'key': 'CopyQueueStatus', 'type': 'ReplicatorQueueStatus'},
        'last_copy_operation_received_time_utc': {'key': 'LastCopyOperationReceivedTimeUtc', 'type': 'iso-8601'},
        'last_acknowledgement_sent_time_utc': {'key': 'LastAcknowledgementSentTimeUtc', 'type': 'iso-8601'},
    }

    def __init__(self, *, replication_queue_status=None, last_replication_operation_received_time_utc=None, is_in_build: bool=None, copy_queue_status=None, last_copy_operation_received_time_utc=None, last_acknowledgement_sent_time_utc=None, **kwargs) -> None:
        super(SecondaryIdleReplicatorStatus, self).__init__(replication_queue_status=replication_queue_status, last_replication_operation_received_time_utc=last_replication_operation_received_time_utc, is_in_build=is_in_build, copy_queue_status=copy_queue_status, last_copy_operation_received_time_utc=last_copy_operation_received_time_utc, last_acknowledgement_sent_time_utc=last_acknowledgement_sent_time_utc, **kwargs)
        self.kind = 'IdleSecondary'
