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


class OptionalClaim(Model):
    """Specifying the claims to be included in a token.

    :param name: Claim name.
    :type name: str
    :param source: Claim source.
    :type source: str
    :param essential: Is this a requied claim.
    :type essential: bool
    :param additional_properties:
    :type additional_properties: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'essential': {'key': 'essential', 'type': 'bool'},
        'additional_properties': {'key': 'additionalProperties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(OptionalClaim, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.source = kwargs.get('source', None)
        self.essential = kwargs.get('essential', None)
        self.additional_properties = kwargs.get('additional_properties', None)
