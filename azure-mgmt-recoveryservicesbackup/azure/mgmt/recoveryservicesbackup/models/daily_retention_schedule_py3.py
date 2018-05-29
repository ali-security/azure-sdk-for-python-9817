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


class DailyRetentionSchedule(Model):
    """Daily retention schedule.

    :param retention_times: Retention times of retention policy.
    :type retention_times: list[datetime]
    :param retention_duration: Retention duration of retention Policy.
    :type retention_duration:
     ~azure.mgmt.recoveryservicesbackup.models.RetentionDuration
    """

    _attribute_map = {
        'retention_times': {'key': 'retentionTimes', 'type': '[iso-8601]'},
        'retention_duration': {'key': 'retentionDuration', 'type': 'RetentionDuration'},
    }

    def __init__(self, *, retention_times=None, retention_duration=None, **kwargs) -> None:
        super(DailyRetentionSchedule, self).__init__(**kwargs)
        self.retention_times = retention_times
        self.retention_duration = retention_duration
