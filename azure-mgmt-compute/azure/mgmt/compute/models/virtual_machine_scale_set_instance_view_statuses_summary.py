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


class VirtualMachineScaleSetInstanceViewStatusesSummary(Model):
    """
    Instance view statuses summary for virtual machines of a virtual machine
    scale set.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar statuses_summary: Gets the extensions information.
    :vartype statuses_summary: list of :class:`VirtualMachineStatusCodeCount
     <azure.mgmt.compute.models.VirtualMachineStatusCodeCount>`
    """ 

    _validation = {
        'statuses_summary': {'readonly': True},
    }

    _attribute_map = {
        'statuses_summary': {'key': 'statusesSummary', 'type': '[VirtualMachineStatusCodeCount]'},
    }

    def __init__(self):
        self.statuses_summary = None
