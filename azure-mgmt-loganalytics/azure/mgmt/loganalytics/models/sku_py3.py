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


class Sku(Model):
    """The SKU (tier) of a workspace.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU. Possible values include:
     'Free', 'Standard', 'Premium', 'Unlimited', 'PerNode', 'PerGB2018',
     'Standalone'
    :type name: str or ~azure.mgmt.loganalytics.models.SkuNameEnum
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, name, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
