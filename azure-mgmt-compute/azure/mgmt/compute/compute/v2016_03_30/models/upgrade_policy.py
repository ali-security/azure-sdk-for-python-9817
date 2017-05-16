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


class UpgradePolicy(Model):
    """Describes an upgrade policy - automatic or manual.

    :param mode: The upgrade mode. Possible values include: 'Automatic',
     'Manual'
    :type mode: str or :class:`UpgradeMode
     <azure.mgmt.compute.compute.v2016_03_30.models.UpgradeMode>`
    """

    _attribute_map = {
        'mode': {'key': 'mode', 'type': 'UpgradeMode'},
    }

    def __init__(self, mode=None):
        self.mode = mode
