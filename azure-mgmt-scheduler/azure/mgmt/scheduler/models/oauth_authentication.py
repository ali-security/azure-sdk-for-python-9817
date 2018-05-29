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

from .http_authentication import HttpAuthentication


class OAuthAuthentication(HttpAuthentication):
    """OAuthAuthentication.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param secret: Gets or sets the secret, return value will always be empty.
    :type secret: str
    :param tenant: Gets or sets the tenant.
    :type tenant: str
    :param audience: Gets or sets the audience.
    :type audience: str
    :param client_id: Gets or sets the client identifier.
    :type client_id: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'secret': {'key': 'secret', 'type': 'str'},
        'tenant': {'key': 'tenant', 'type': 'str'},
        'audience': {'key': 'audience', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OAuthAuthentication, self).__init__(**kwargs)
        self.secret = kwargs.get('secret', None)
        self.tenant = kwargs.get('tenant', None)
        self.audience = kwargs.get('audience', None)
        self.client_id = kwargs.get('client_id', None)
        self.type = 'ActiveDirectoryOAuth'
