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


class NodeAgentSku(Model):
    """
    Information about supported node agent SKU.

    :param id: Gets or sets the node agent SKU id.
    :type id: str
    :param verified_image_references: Gets the list of images verified to be
     compatible with the node agent SKU. This collection is not exhaustive;
     the node agent SKU may be compatible with other images.
    :type verified_image_references: list of :class:`ImageReference
     <azure.batch.models.ImageReference>`
    :param os_type: Gets or sets the type of OS that the node Agent SKU is
     targeted against. Possible values include: 'linux', 'windows', 'unmapped'
    :type os_type: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'verified_image_references': {'key': 'verifiedImageReferences', 'type': '[ImageReference]'},
        'os_type': {'key': 'osType', 'type': 'OSType'},
    }

    def __init__(self, id=None, verified_image_references=None, os_type=None):
        self.id = id
        self.verified_image_references = verified_image_references
        self.os_type = os_type
