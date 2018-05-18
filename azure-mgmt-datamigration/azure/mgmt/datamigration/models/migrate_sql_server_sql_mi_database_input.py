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


class MigrateSqlServerSqlMIDatabaseInput(Model):
    """Database specific information for SQL to Azure SQL DB Managed Instance
    migration task inputs.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the database
    :type name: str
    :param restore_database_name: Required. Name of the database at
     destination
    :type restore_database_name: str
    :param backup_file_share: Backup file share information for backing up
     this database.
    :type backup_file_share: ~azure.mgmt.datamigration.models.FileShare
    """

    _validation = {
        'name': {'required': True},
        'restore_database_name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'restore_database_name': {'key': 'restoreDatabaseName', 'type': 'str'},
        'backup_file_share': {'key': 'backupFileShare', 'type': 'FileShare'},
    }

    def __init__(self, **kwargs):
        super(MigrateSqlServerSqlMIDatabaseInput, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.restore_database_name = kwargs.get('restore_database_name', None)
        self.backup_file_share = kwargs.get('backup_file_share', None)
