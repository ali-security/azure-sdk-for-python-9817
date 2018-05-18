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


class ProjectTaskProperties(Model):
    """Base class for all types of DMS task properties. If task is not supported
    by current client, this object is returned.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ValidateMigrationInputSqlServerSqlMITaskProperties,
    MigrateSqlServerSqlDbTaskProperties, MigrateSqlServerSqlMITaskProperties,
    GetUserTablesSqlTaskProperties, ConnectToTargetSqlDbTaskProperties,
    ConnectToTargetSqlMITaskProperties, ConnectToSourceSqlServerTaskProperties

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar errors: Array of errors. This is ignored if submitted.
    :vartype errors: list[~azure.mgmt.datamigration.models.ODataError]
    :ivar state: The state of the task. This is ignored if submitted. Possible
     values include: 'Unknown', 'Queued', 'Running', 'Canceled', 'Succeeded',
     'Failed', 'FailedInputValidation', 'Faulted'
    :vartype state: str or ~azure.mgmt.datamigration.models.TaskState
    :param task_type: Required. Constant filled by server.
    :type task_type: str
    """

    _validation = {
        'errors': {'readonly': True},
        'state': {'readonly': True},
        'task_type': {'required': True},
    }

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[ODataError]'},
        'state': {'key': 'state', 'type': 'str'},
        'task_type': {'key': 'taskType', 'type': 'str'},
    }

    _subtype_map = {
        'task_type': {'ValidateMigrationInput.SqlServer.AzureSqlDbMI': 'ValidateMigrationInputSqlServerSqlMITaskProperties', 'Migrate.SqlServer.SqlDb': 'MigrateSqlServerSqlDbTaskProperties', 'Migrate.SqlServer.AzureSqlDbMI': 'MigrateSqlServerSqlMITaskProperties', 'GetUserTables.Sql': 'GetUserTablesSqlTaskProperties', 'ConnectToTarget.SqlDb': 'ConnectToTargetSqlDbTaskProperties', 'ConnectToTarget.AzureSqlDbMI': 'ConnectToTargetSqlMITaskProperties', 'ConnectToSource.SqlServer': 'ConnectToSourceSqlServerTaskProperties'}
    }

    def __init__(self, **kwargs):
        super(ProjectTaskProperties, self).__init__(**kwargs)
        self.errors = None
        self.state = None
        self.task_type = None
