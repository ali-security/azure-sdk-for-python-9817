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


class CsmSiteRecoveryEntity(Model):
    """
    Class containting details about site recovery operation.

    :param snapshot_time: Point in time in which the site recover should be
     attempted.
    :type snapshot_time: datetime
    :param site_name: [Optional] Destination web app name into which web app
     should be recovered. This is case when new web app should be created
     instead.
    :type site_name: str
    :param slot_name: [Optional] Destination web app slot name into which web
     app should be recovered
    :type slot_name: str
    """ 

    _attribute_map = {
        'snapshot_time': {'key': 'snapshotTime', 'type': 'iso-8601'},
        'site_name': {'key': 'siteName', 'type': 'str'},
        'slot_name': {'key': 'slotName', 'type': 'str'},
    }

    def __init__(self, snapshot_time=None, site_name=None, slot_name=None):
        self.snapshot_time = snapshot_time
        self.site_name = site_name
        self.slot_name = slot_name
