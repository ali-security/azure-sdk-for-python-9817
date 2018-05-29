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


class Settings(Model):
    """Common settings field for backup management.

    :param time_zone: TimeZone optional input as string. For example: TimeZone
     = "Pacific Standard Time".
    :type time_zone: str
    :param issqlcompression: SQL compression flag
    :type issqlcompression: bool
    """

    _attribute_map = {
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'issqlcompression': {'key': 'issqlcompression', 'type': 'bool'},
    }

    def __init__(self, *, time_zone: str=None, issqlcompression: bool=None, **kwargs) -> None:
        super(Settings, self).__init__(**kwargs)
        self.time_zone = time_zone
        self.issqlcompression = issqlcompression
