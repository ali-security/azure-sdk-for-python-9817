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

from .entity_health_state_chunk_list import EntityHealthStateChunkList


class NodeHealthStateChunkList(EntityHealthStateChunkList):
    """The list of node health state chunks in the cluster that respect the input
    filters in the chunk query. Returned by get cluster health state chunks
    query.
    .

    :param total_count: Total number of entity health state objects that match
     the specified filters from the cluster health chunk query description.
    :type total_count: long
    :param items: The list of node health state chunks that respect the input
     filters in the chunk query.
    :type items: list[~azure.servicefabric.models.NodeHealthStateChunk]
    """

    _attribute_map = {
        'total_count': {'key': 'TotalCount', 'type': 'long'},
        'items': {'key': 'Items', 'type': '[NodeHealthStateChunk]'},
    }

    def __init__(self, total_count=None, items=None):
        super(NodeHealthStateChunkList, self).__init__(total_count=total_count)
        self.items = items
