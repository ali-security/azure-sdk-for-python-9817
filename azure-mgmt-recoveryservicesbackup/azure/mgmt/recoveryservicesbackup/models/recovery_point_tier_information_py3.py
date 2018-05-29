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


class RecoveryPointTierInformation(Model):
    """Recovery point tier information.

    :param type: Recovery point tier type. Possible values include: 'Invalid',
     'InstantRP', 'HardenedRP'
    :type type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RecoveryPointTierType
    :param status: Recovery point tier status. Possible values include:
     'Invalid', 'Valid', 'Disabled', 'Deleted'
    :type status: str or
     ~azure.mgmt.recoveryservicesbackup.models.RecoveryPointTierStatus
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'RecoveryPointTierType'},
        'status': {'key': 'status', 'type': 'RecoveryPointTierStatus'},
    }

    def __init__(self, *, type=None, status=None, **kwargs) -> None:
        super(RecoveryPointTierInformation, self).__init__(**kwargs)
        self.type = type
        self.status = status
