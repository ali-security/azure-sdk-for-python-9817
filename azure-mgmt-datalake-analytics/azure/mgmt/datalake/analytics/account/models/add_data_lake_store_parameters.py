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


class AddDataLakeStoreParameters(Model):
    """Additional Data Lake Store parameters.

    :param suffix: the optional suffix for the Data Lake Store account.
    :type suffix: str
    """ 

    _attribute_map = {
        'suffix': {'key': 'properties.suffix', 'type': 'str'},
    }

    def __init__(self, suffix=None):
        self.suffix = suffix
