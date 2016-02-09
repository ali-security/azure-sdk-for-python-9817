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

from .resource import Resource


class GeoRegion(Resource):
    """
    Geographical region

    :param str id: Resource Id
    :param str name: Resource Name
    :param str location: Resource Location
    :param str type: Resource type
    :param dict tags: Resource tags
    :param str geo_region_name: Region name
    :param str description: Region description
    :param str display_name: Display name for region
    """

    _required = []

    _attribute_map = {
        'geo_region_name': {'key': 'properties.name', 'type': 'str', 'flatten': True},
        'description': {'key': 'properties.description', 'type': 'str', 'flatten': True},
        'display_name': {'key': 'properties.displayName', 'type': 'str', 'flatten': True},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, geo_region_name=None, description=None, display_name=None):
        super(GeoRegion, self).__init__(id=id, name=name, location=location, type=type, tags=tags)
        self.geo_region_name = geo_region_name
        self.description = description
        self.display_name = display_name
