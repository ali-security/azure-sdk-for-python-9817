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


class RefreshIndex(Model):
    """Refresh Index Response.

    :param content_source_id: Content source Id.
    :type content_source_id: str
    :param is_update_success: Update success status.
    :type is_update_success: bool
    :param advanced_info: Advanced info list.
    :type advanced_info:
     list[~azure.cognitiveservices.vision.contentmoderator.models.RefreshIndexAdvancedInfoItem]
    :param status: Refresh index status.
    :type status:
     ~azure.cognitiveservices.vision.contentmoderator.models.Status
    :param tracking_id: Tracking Id.
    :type tracking_id: str
    """

    _attribute_map = {
        'content_source_id': {'key': 'contentSourceId', 'type': 'str'},
        'is_update_success': {'key': 'isUpdateSuccess', 'type': 'bool'},
        'advanced_info': {'key': 'advancedInfo', 'type': '[RefreshIndexAdvancedInfoItem]'},
        'status': {'key': 'status', 'type': 'Status'},
        'tracking_id': {'key': 'trackingId', 'type': 'str'},
    }

    def __init__(self, content_source_id=None, is_update_success=None, advanced_info=None, status=None, tracking_id=None):
        self.content_source_id = content_source_id
        self.is_update_success = is_update_success
        self.advanced_info = advanced_info
        self.status = status
        self.tracking_id = tracking_id
