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


class InstanceViewStatus(Model):
    """
    Instance view status.

    :param code: Gets the status Code.
    :type code: str
    :param level: Gets or sets the level Code. Possible values include:
     'Info', 'Warning', 'Error'
    :type level: str or :class:`StatusLevelTypes
     <azure.mgmt.compute.models.StatusLevelTypes>`
    :param display_status: Gets or sets the short localizable label for the
     status.
    :type display_status: str
    :param message: Gets or sets the detailed Message, including for alerts
     and error messages.
    :type message: str
    :param time: Gets or sets the time of the status.
    :type time: datetime
    """ 

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'level': {'key': 'level', 'type': 'StatusLevelTypes'},
        'display_status': {'key': 'displayStatus', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'time': {'key': 'time', 'type': 'iso-8601'},
    }

    def __init__(self, code=None, level=None, display_status=None, message=None, time=None):
        self.code = code
        self.level = level
        self.display_status = display_status
        self.message = message
        self.time = time
