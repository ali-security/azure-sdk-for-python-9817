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

from .resource import Resource


class HybridConnectionKey(Resource):
    """Hybrid Connection key contract. This has the send key name and value for a
    Hybrid Connection.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :param name: Resource Name.
    :type name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :param type: Resource type.
    :type type: str
    :param tags: Resource tags.
    :type tags: dict
    :ivar send_key_name: The name of the send key.
    :vartype send_key_name: str
    :ivar send_key_value: The value of the send key.
    :vartype send_key_value: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'location': {'required': True},
        'send_key_name': {'readonly': True},
        'send_key_value': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'send_key_name': {'key': 'properties.sendKeyName', 'type': 'str'},
        'send_key_value': {'key': 'properties.sendKeyValue', 'type': 'str'},
    }

    def __init__(self, name, location, kind=None, type=None, tags=None):
        super(HybridConnectionKey, self).__init__(name=name, kind=kind, location=location, type=type, tags=tags)
        self.send_key_name = None
        self.send_key_value = None
