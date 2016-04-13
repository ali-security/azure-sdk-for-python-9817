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


class BlobContainerProperties(Model):
    """
    Azure Storage blob container properties information.

    :param last_modified_time: Gets or sets the last modified time of the
     blob container.
    :type last_modified_time: datetime
    """ 

    _attribute_map = {
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
    }

    def __init__(self, last_modified_time=None):
        self.last_modified_time = last_modified_time
