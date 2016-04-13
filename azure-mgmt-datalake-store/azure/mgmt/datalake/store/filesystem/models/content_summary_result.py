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


class ContentSummaryResult(Model):
    """
    Data Lake Store filesystem content summary information response.

    :param content_summary: Gets the content summary for the specified path
    :type content_summary: :class:`ContentSummary
     <azure.mgmt.datalake.store.filesystem.models.ContentSummary>`
    """ 

    _attribute_map = {
        'content_summary': {'key': 'ContentSummary', 'type': 'ContentSummary'},
    }

    def __init__(self, content_summary=None):
        self.content_summary = content_summary
