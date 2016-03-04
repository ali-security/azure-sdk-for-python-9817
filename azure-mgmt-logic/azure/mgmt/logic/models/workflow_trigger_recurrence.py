# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WorkflowTriggerRecurrence(Model):
    """WorkflowTriggerRecurrence

    :param str frequency: Gets or sets the frequency. Possible values
     include: 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year'
    :param int interval: Gets or sets the interval.
    :param datetime start_time: Gets or sets the start time.
    :param str time_zone: Gets or sets the time zone.
    """ 

    _attribute_map = {
        'frequency': {'key': 'frequency', 'type': 'RecurrenceFrequency'},
        'interval': {'key': 'interval', 'type': 'int'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'time_zone': {'key': 'timeZone', 'type': 'str'},
    }

    def __init__(self, frequency=None, interval=None, start_time=None, time_zone=None, **kwargs):
        self.frequency = frequency
        self.interval = interval
        self.start_time = start_time
        self.time_zone = time_zone
