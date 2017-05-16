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


class PartitionHealthStateChunkList(Model):
    """The list of partition health state chunks that respect the input filters
    in the chunk query description.
    Returned by get cluster health state chunks query as part of the parent
    application hierarchy.
    .

    :param items: The list of partition health state chunks that respect the
     input filters in the chunk query.
    :type items: list of :class:`PartitionHealthStateChunk
     <azure.servicefabric.models.PartitionHealthStateChunk>`
    """ 

    _attribute_map = {
        'items': {'key': 'Items', 'type': '[PartitionHealthStateChunk]'},
    }

    def __init__(self, items=None):
        self.items = items
