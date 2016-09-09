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


class StatusesDefault(Resource):
    """Default Statuses entity for the given tenant.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource Tags
    :type tags: dict
    :param location: Resource Location
    :type location: str
    :ivar deployed_policies:
    :vartype deployed_policies: int
    :ivar enrolled_users:
    :vartype enrolled_users: int
    :ivar flagged_users:
    :vartype flagged_users: int
    :ivar last_modified_time:
    :vartype last_modified_time: datetime
    :ivar policy_applied_users:
    :vartype policy_applied_users: int
    :ivar status:
    :vartype status: str
    :ivar wipe_failed_apps:
    :vartype wipe_failed_apps: int
    :ivar wipe_pending_apps:
    :vartype wipe_pending_apps: int
    :ivar wipe_succeeded_apps:
    :vartype wipe_succeeded_apps: int
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'deployed_policies': {'readonly': True},
        'enrolled_users': {'readonly': True},
        'flagged_users': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'policy_applied_users': {'readonly': True},
        'status': {'readonly': True},
        'wipe_failed_apps': {'readonly': True},
        'wipe_pending_apps': {'readonly': True},
        'wipe_succeeded_apps': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'deployed_policies': {'key': 'properties.deployedPolicies', 'type': 'int'},
        'enrolled_users': {'key': 'properties.enrolledUsers', 'type': 'int'},
        'flagged_users': {'key': 'properties.flaggedUsers', 'type': 'int'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'policy_applied_users': {'key': 'properties.policyAppliedUsers', 'type': 'int'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'wipe_failed_apps': {'key': 'properties.wipeFailedApps', 'type': 'int'},
        'wipe_pending_apps': {'key': 'properties.wipePendingApps', 'type': 'int'},
        'wipe_succeeded_apps': {'key': 'properties.wipeSucceededApps', 'type': 'int'},
    }

    def __init__(self, tags=None, location=None):
        super(StatusesDefault, self).__init__(tags=tags, location=location)
        self.deployed_policies = None
        self.enrolled_users = None
        self.flagged_users = None
        self.last_modified_time = None
        self.policy_applied_users = None
        self.status = None
        self.wipe_failed_apps = None
        self.wipe_pending_apps = None
        self.wipe_succeeded_apps = None
