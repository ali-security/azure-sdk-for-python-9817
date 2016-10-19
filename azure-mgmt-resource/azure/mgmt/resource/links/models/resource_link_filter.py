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


class ResourceLinkFilter(Model):
    """Resource link filter.

    :param target_id: The target Id of the resource.
    :type target_id: str
    """ 

    _validation = {
        'target_id': {'required': True},
    }

    _attribute_map = {
        'target_id': {'key': 'targetId', 'type': 'str'},
    }

    def __init__(self, target_id):
        self.target_id = target_id
