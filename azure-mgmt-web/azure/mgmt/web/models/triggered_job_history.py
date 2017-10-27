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

from .proxy_only_resource import ProxyOnlyResource


class TriggeredJobHistory(ProxyOnlyResource):
    """Triggered Web Job History. List of Triggered Web Job Run Information
    elements.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param triggered_job_runs: List of triggered web job runs.
    :type triggered_job_runs: list[~azure.mgmt.web.models.TriggeredJobRun]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'triggered_job_runs': {'key': 'properties.triggeredJobRuns', 'type': '[TriggeredJobRun]'},
    }

    def __init__(self, kind=None, triggered_job_runs=None):
        super(TriggeredJobHistory, self).__init__(kind=kind)
        self.triggered_job_runs = triggered_job_runs
