# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ClusterConfigurationUpgradeStatusInfo(Model):
    """Information about a standalone cluster configuration upgrade status.

    :param upgrade_state: The state of the upgrade domain. Possible values
     include: 'Invalid', 'RollingBackInProgress', 'RollingBackCompleted',
     'RollingForwardPending', 'RollingForwardInProgress',
     'RollingForwardCompleted', 'Failed'
    :type upgrade_state: str or ~servicefabric.models.UpgradeState
    :param progress_status: The cluster manifest version.
    :type progress_status: int
    :param config_version: The cluster configuration version.
    :type config_version: str
    :param details: The cluster upgrade status details.
    :type details: str
    """

    _attribute_map = {
        'upgrade_state': {'key': 'UpgradeState', 'type': 'str'},
        'progress_status': {'key': 'ProgressStatus', 'type': 'int'},
        'config_version': {'key': 'ConfigVersion', 'type': 'str'},
        'details': {'key': 'Details', 'type': 'str'},
    }

    def __init__(self, upgrade_state=None, progress_status=None, config_version=None, details=None):
        super(ClusterConfigurationUpgradeStatusInfo, self).__init__()
        self.upgrade_state = upgrade_state
        self.progress_status = progress_status
        self.config_version = config_version
        self.details = details
