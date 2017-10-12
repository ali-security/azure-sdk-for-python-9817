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

from .server_properties_for_create import ServerPropertiesForCreate


class ServerPropertiesForDefaultCreate(ServerPropertiesForCreate):
    """The properties used to create a new server.

    :param storage_mb: The maximum storage allowed for a server.
    :type storage_mb: long
    :param version: Server version. Possible values include: '9.5', '9.6'
    :type version: str or ~azure.mgmt.rdbms.postgresql.models.ServerVersion
    :param ssl_enforcement: Enable ssl enforcement or not when connect to
     server. Possible values include: 'Enabled', 'Disabled'
    :type ssl_enforcement: str or
     ~azure.mgmt.rdbms.postgresql.models.SslEnforcementEnum
    :param create_mode: Constant filled by server.
    :type create_mode: str
    :param administrator_login: The administrator's login name of a server.
     Can only be specified when the server is being created (and is required
     for creation).
    :type administrator_login: str
    :param administrator_login_password: The password of the administrator
     login.
    :type administrator_login_password: str
    """

    _validation = {
        'storage_mb': {'minimum': 1024},
        'create_mode': {'required': True},
        'administrator_login': {'required': True},
        'administrator_login_password': {'required': True},
    }

    _attribute_map = {
        'storage_mb': {'key': 'storageMB', 'type': 'long'},
        'version': {'key': 'version', 'type': 'str'},
        'ssl_enforcement': {'key': 'sslEnforcement', 'type': 'SslEnforcementEnum'},
        'create_mode': {'key': 'createMode', 'type': 'str'},
        'administrator_login': {'key': 'administratorLogin', 'type': 'str'},
        'administrator_login_password': {'key': 'administratorLoginPassword', 'type': 'str'},
    }

    def __init__(self, administrator_login, administrator_login_password, storage_mb=None, version=None, ssl_enforcement=None):
        super(ServerPropertiesForDefaultCreate, self).__init__(storage_mb=storage_mb, version=version, ssl_enforcement=ssl_enforcement)
        self.administrator_login = administrator_login
        self.administrator_login_password = administrator_login_password
        self.create_mode = 'Default'
