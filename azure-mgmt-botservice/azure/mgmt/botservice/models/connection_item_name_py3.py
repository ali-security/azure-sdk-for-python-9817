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


class ConnectionItemName(Model):
    """The display name of a connection Item Setting registered with the Bot.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Connection Item name that has been added in the API
    :vartype name: str
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ConnectionItemName, self).__init__(**kwargs)
        self.name = None
