# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .health_information import HealthInformation


class HealthEvent(HealthInformation):
    """Represents health information reported on a health entity, such as cluster,
    application or node, with additional metadata added by the Health Manager.
    .

    :param source_id: The source name which identifies the
     client/watchdog/system component which generated the health information.
    :type source_id: str
    :param property: The property of the health information. An entity can
     have health reports for different properties.
     The property is a string and not a fixed enumeration to allow the reporter
     flexibility to categorize the state condition that triggers the report.
     For example, a reporter with SourceId "LocalWatchdog" can monitor the
     state of the available disk on a node,
     so it can report "AvailableDisk" property on that node.
     The same reporter can monitor the node connectivity, so it can report a
     property "Connectivity" on the same node.
     In the health store, these reports are treated as separate health events
     for the specified node.
     Together with the SourceId, the property uniquely identifies the health
     information.
    :type property: str
    :param health_state: The health state of a Service Fabric entity such as
     Cluster, Node, Application, Service, Partition, Replica etc. Possible
     values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~servicefabric.models.HealthState
    :param time_to_live_in_milli_seconds: The duration for which this health
     report is valid. This field is using ISO8601 format for specifying the
     duration.
     When clients report periodically, they should send reports with higher
     frequency than time to live.
     If clients report on transition, they can set the time to live to
     infinite.
     When time to live expires, the health event that contains the health
     information
     is either removed from health store, if RemoveWhenExpired is true, or
     evaluated at error, if RemoveWhenExpired false.
     If not specified, time to live defaults to infinite value.
    :type time_to_live_in_milli_seconds: timedelta
    :param description: The description of the health information. It
     represents free text used to add human readable information about the
     report.
     The maximum string length for the description is 4096 characters.
     If the provided string is longer, it will be automatically truncated.
     When truncated, the last characters of the description contain a marker
     "[Truncated]", and total string size is 4096 characters.
     The presence of the marker indicates to users that truncation occurred.
     Note that when truncated, the description has less than 4096 characters
     from the original string.
    :type description: str
    :param sequence_number: The sequence number for this health report as a
     numeric string.
     The report sequence number is used by the health store to detect stale
     reports.
     If not specified, a sequence number is auto-generated by the health client
     when a report is added.
    :type sequence_number: str
    :param remove_when_expired: Value that indicates whether the report is
     removed from health store when it expires.
     If set to true, the report is removed from the health store after it
     expires.
     If set to false, the report is treated as an error when expired. The value
     of this property is false by default.
     When clients report periodically, they should set RemoveWhenExpired false
     (default).
     This way, is the reporter has issues (eg. deadlock) and can't report, the
     entity is evaluated at error when the health report expires.
     This flags the entity as being in Error health state.
    :type remove_when_expired: bool
    :param is_expired: Returns true if the health event is expired, otherwise
     false.
    :type is_expired: bool
    :param source_utc_timestamp: The date and time when the health report was
     sent by the source.
    :type source_utc_timestamp: datetime
    :param last_modified_utc_timestamp: The date and time when the health
     report was last modified by the health store.
    :type last_modified_utc_timestamp: datetime
    :param last_ok_transition_at: If the current health state is 'Ok', this
     property returns the time at which the health report was first reported
     with 'Ok'.
     For periodic reporting, many reports with the same state may have been
     generated.
     This property returns the date and time when the first 'Ok' health report
     was received.
     If the current health state is 'Error' or 'Warning', returns the date and
     time at which the health state was last in 'Ok', before transitioning to a
     different state.
     If the health state was never 'Ok', the value will be zero date-time.
    :type last_ok_transition_at: datetime
    :param last_warning_transition_at: If the current health state is
     'Warning', this property returns the time at which the health report was
     first reported with 'Warning'. For periodic reporting, many reports with
     the same state may have been generated however, this property returns only
     the date and time at the first 'Warning' health report was received.
     If the current health state is 'Ok' or 'Error', returns the date and time
     at which the health state was last in 'Warning', before transitioning to a
     different state.
     If the health state was never 'Warning', the value will be zero date-time.
    :type last_warning_transition_at: datetime
    :param last_error_transition_at: If the current health state is 'Error',
     this property returns the time at which the health report was first
     reported with 'Error'. For periodic reporting, many reports with the same
     state may have been generated however, this property returns only the date
     and time at the first 'Error' health report was received.
     If the current health state is 'Ok' or 'Warning', returns the date and
     time at which the health state was last in 'Error', before transitioning
     to a different state.
     If the health state was never 'Error', the value will be zero date-time.
    :type last_error_transition_at: datetime
    """

    _validation = {
        'source_id': {'required': True},
        'property': {'required': True},
        'health_state': {'required': True},
    }

    _attribute_map = {
        'source_id': {'key': 'SourceId', 'type': 'str'},
        'property': {'key': 'Property', 'type': 'str'},
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'time_to_live_in_milli_seconds': {'key': 'TimeToLiveInMilliSeconds', 'type': 'duration'},
        'description': {'key': 'Description', 'type': 'str'},
        'sequence_number': {'key': 'SequenceNumber', 'type': 'str'},
        'remove_when_expired': {'key': 'RemoveWhenExpired', 'type': 'bool'},
        'is_expired': {'key': 'IsExpired', 'type': 'bool'},
        'source_utc_timestamp': {'key': 'SourceUtcTimestamp', 'type': 'iso-8601'},
        'last_modified_utc_timestamp': {'key': 'LastModifiedUtcTimestamp', 'type': 'iso-8601'},
        'last_ok_transition_at': {'key': 'LastOkTransitionAt', 'type': 'iso-8601'},
        'last_warning_transition_at': {'key': 'LastWarningTransitionAt', 'type': 'iso-8601'},
        'last_error_transition_at': {'key': 'LastErrorTransitionAt', 'type': 'iso-8601'},
    }

    def __init__(self, source_id, property, health_state, time_to_live_in_milli_seconds=None, description=None, sequence_number=None, remove_when_expired=None, is_expired=None, source_utc_timestamp=None, last_modified_utc_timestamp=None, last_ok_transition_at=None, last_warning_transition_at=None, last_error_transition_at=None):
        super(HealthEvent, self).__init__(source_id=source_id, property=property, health_state=health_state, time_to_live_in_milli_seconds=time_to_live_in_milli_seconds, description=description, sequence_number=sequence_number, remove_when_expired=remove_when_expired)
        self.is_expired = is_expired
        self.source_utc_timestamp = source_utc_timestamp
        self.last_modified_utc_timestamp = last_modified_utc_timestamp
        self.last_ok_transition_at = last_ok_transition_at
        self.last_warning_transition_at = last_warning_transition_at
        self.last_error_transition_at = last_error_transition_at
