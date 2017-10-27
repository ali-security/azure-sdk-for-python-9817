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

from .proxy_resource import ProxyResource


class SyncGroup(ProxyResource):
    """An Azure SQL Database sync group.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param interval: Sync interval of the sync group.
    :type interval: int
    :ivar last_sync_time: Last sync time of the sync group.
    :vartype last_sync_time: datetime
    :param conflict_resolution_policy: Conflict resolution policy of the sync
     group. Possible values include: 'HubWin', 'MemberWin'
    :type conflict_resolution_policy: str or
     ~azure.mgmt.sql.models.SyncConflictResolutionPolicy
    :param sync_database_id: ARM resource id of the sync database in the sync
     group.
    :type sync_database_id: str
    :param hub_database_user_name: User name for the sync group hub database
     credential.
    :type hub_database_user_name: str
    :param hub_database_password: Password for the sync group hub database
     credential.
    :type hub_database_password: str
    :ivar sync_state: Sync state of the sync group. Possible values include:
     'NotReady', 'Error', 'Warning', 'Progressing', 'Good'
    :vartype sync_state: str or ~azure.mgmt.sql.models.SyncGroupState
    :param schema: Sync schema of the sync group.
    :type schema: ~azure.mgmt.sql.models.SyncGroupSchema
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'last_sync_time': {'readonly': True},
        'sync_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'interval': {'key': 'properties.interval', 'type': 'int'},
        'last_sync_time': {'key': 'properties.lastSyncTime', 'type': 'iso-8601'},
        'conflict_resolution_policy': {'key': 'properties.conflictResolutionPolicy', 'type': 'str'},
        'sync_database_id': {'key': 'properties.syncDatabaseId', 'type': 'str'},
        'hub_database_user_name': {'key': 'properties.hubDatabaseUserName', 'type': 'str'},
        'hub_database_password': {'key': 'properties.hubDatabasePassword', 'type': 'str'},
        'sync_state': {'key': 'properties.syncState', 'type': 'str'},
        'schema': {'key': 'properties.schema', 'type': 'SyncGroupSchema'},
    }

    def __init__(self, interval=None, conflict_resolution_policy=None, sync_database_id=None, hub_database_user_name=None, hub_database_password=None, schema=None):
        super(SyncGroup, self).__init__()
        self.interval = interval
        self.last_sync_time = None
        self.conflict_resolution_policy = conflict_resolution_policy
        self.sync_database_id = sync_database_id
        self.hub_database_user_name = hub_database_user_name
        self.hub_database_password = hub_database_password
        self.sync_state = None
        self.schema = schema
