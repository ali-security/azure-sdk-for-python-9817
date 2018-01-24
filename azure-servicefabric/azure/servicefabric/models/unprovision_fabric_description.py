# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UnprovisionFabricDescription(Model):
    """Describes the parameters for unprovisioning a cluster.

    :param code_version: The cluster code package version.
    :type code_version: str
    :param config_version: The cluster manifest version.
    :type config_version: str
    """

    _attribute_map = {
        'code_version': {'key': 'CodeVersion', 'type': 'str'},
        'config_version': {'key': 'ConfigVersion', 'type': 'str'},
    }

    def __init__(self, code_version=None, config_version=None):
        super(UnprovisionFabricDescription, self).__init__()
        self.code_version = code_version
        self.config_version = config_version
