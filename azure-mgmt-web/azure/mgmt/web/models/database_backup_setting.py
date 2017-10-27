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


class DatabaseBackupSetting(Model):
    """Database backup settings.

    :param database_type: Database type (e.g. SqlAzure / MySql). Possible
     values include: 'SqlAzure', 'MySql', 'LocalMySql', 'PostgreSql'
    :type database_type: str or ~azure.mgmt.web.models.DatabaseType
    :param name:
    :type name: str
    :param connection_string_name: Contains a connection string name that is
     linked to the SiteConfig.ConnectionStrings.
     This is used during restore with overwrite connection strings options.
    :type connection_string_name: str
    :param connection_string: Contains a connection string to a database which
     is being backed up or restored. If the restore should happen to a new
     database, the database name inside is the new one.
    :type connection_string: str
    """

    _validation = {
        'database_type': {'required': True},
    }

    _attribute_map = {
        'database_type': {'key': 'databaseType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'connection_string_name': {'key': 'connectionStringName', 'type': 'str'},
        'connection_string': {'key': 'connectionString', 'type': 'str'},
    }

    def __init__(self, database_type, name=None, connection_string_name=None, connection_string=None):
        self.database_type = database_type
        self.name = name
        self.connection_string_name = connection_string_name
        self.connection_string = connection_string
