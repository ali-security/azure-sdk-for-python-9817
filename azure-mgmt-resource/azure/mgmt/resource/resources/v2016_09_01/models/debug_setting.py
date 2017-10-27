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


class DebugSetting(Model):
    """DebugSetting.

    :param detail_level: Specifies the type of information to log for
     debugging. The permitted values are none, requestContent, responseContent,
     or both requestContent and responseContent separated by a comma. The
     default is none. When setting this value, carefully consider the type of
     information you are passing in during deployment. By logging information
     about the request or response, you could potentially expose sensitive data
     that is retrieved through the deployment operations.
    :type detail_level: str
    """

    _attribute_map = {
        'detail_level': {'key': 'detailLevel', 'type': 'str'},
    }

    def __init__(self, detail_level=None):
        self.detail_level = detail_level
