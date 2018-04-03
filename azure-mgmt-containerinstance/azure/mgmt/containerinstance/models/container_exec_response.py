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


class ContainerExecResponse(Model):
    """The information for the container exec command.

    :param web_socket_uri: The uri for the exec websocket.
    :type web_socket_uri: str
    :param password: The password to start the exec command.
    :type password: str
    """

    _attribute_map = {
        'web_socket_uri': {'key': 'webSocketUri', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, web_socket_uri=None, password=None):
        super(ContainerExecResponse, self).__init__()
        self.web_socket_uri = web_socket_uri
        self.password = password
