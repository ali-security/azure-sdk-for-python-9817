# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .chaos_event import ChaosEvent


class StartedChaosEvent(ChaosEvent):
    """Describes a Chaos event that gets generated when Chaos is started.

    :param time_stamp_utc: The UTC timestamp when this Chaos event was
     generated.
    :type time_stamp_utc: datetime
    :param kind: Constant filled by server.
    :type kind: str
    :param chaos_parameters: Defines all the parameters to configure a Chaos
     run.
    :type chaos_parameters: ~servicefabric.models.ChaosParameters
    """

    _validation = {
        'time_stamp_utc': {'required': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'time_stamp_utc': {'key': 'TimeStampUtc', 'type': 'iso-8601'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'chaos_parameters': {'key': 'ChaosParameters', 'type': 'ChaosParameters'},
    }

    def __init__(self, time_stamp_utc, chaos_parameters=None):
        super(StartedChaosEvent, self).__init__(time_stamp_utc=time_stamp_utc)
        self.chaos_parameters = chaos_parameters
        self.kind = 'Started'
