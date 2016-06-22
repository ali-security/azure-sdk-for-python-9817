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


class SiteProperties(Model):
    """SiteProperties.

    :param metadata:
    :type metadata: list of :class:`NameValuePair
     <azure.mgmt.web.models.NameValuePair>`
    :param properties:
    :type properties: list of :class:`NameValuePair
     <azure.mgmt.web.models.NameValuePair>`
    :param app_settings:
    :type app_settings: list of :class:`NameValuePair
     <azure.mgmt.web.models.NameValuePair>`
    """ 

    _attribute_map = {
        'metadata': {'key': 'metadata', 'type': '[NameValuePair]'},
        'properties': {'key': 'properties', 'type': '[NameValuePair]'},
        'app_settings': {'key': 'appSettings', 'type': '[NameValuePair]'},
    }

    def __init__(self, metadata=None, properties=None, app_settings=None):
        self.metadata = metadata
        self.properties = properties
        self.app_settings = app_settings
