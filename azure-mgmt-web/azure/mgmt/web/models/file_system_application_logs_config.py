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


class FileSystemApplicationLogsConfig(Model):
    """Application logs to file system configuration.

    :param level: Log level. Possible values include: 'Off', 'Verbose',
     'Information', 'Warning', 'Error'
    :type level: str or :class:`LogLevel <azure.mgmt.web.models.LogLevel>`
    """

    _attribute_map = {
        'level': {'key': 'level', 'type': 'LogLevel'},
    }

    def __init__(self, level=None):
        self.level = level
