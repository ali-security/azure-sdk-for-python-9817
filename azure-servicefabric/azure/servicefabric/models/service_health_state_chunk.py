# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .entity_health_state_chunk import EntityHealthStateChunk


class ServiceHealthStateChunk(EntityHealthStateChunk):
    """Represents the health state chunk of a service, which contains the service
    name, its aggregated health state and any partitions that respect the
    filters in the cluster health chunk query description.
    .

    :param health_state: The health state of a Service Fabric entity such as
     Cluster, Node, Application, Service, Partition, Replica etc. Possible
     values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~servicefabric.models.HealthState
    :param service_name: The name of the service whose health state chunk is
     provided in this object.
    :type service_name: str
    :param partition_health_state_chunks: The list of partition health state
     chunks belonging to the service that respect the filters in the cluster
     health chunk query description.
    :type partition_health_state_chunks:
     ~servicefabric.models.PartitionHealthStateChunkList
    """

    _attribute_map = {
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'partition_health_state_chunks': {'key': 'PartitionHealthStateChunks', 'type': 'PartitionHealthStateChunkList'},
    }

    def __init__(self, health_state=None, service_name=None, partition_health_state_chunks=None):
        super(ServiceHealthStateChunk, self).__init__(health_state=health_state)
        self.service_name = service_name
        self.partition_health_state_chunks = partition_health_state_chunks
