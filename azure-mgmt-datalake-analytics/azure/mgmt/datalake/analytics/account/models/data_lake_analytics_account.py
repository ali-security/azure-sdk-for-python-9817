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


class DataLakeAnalyticsAccount(Resource):
    """A Data Lake Analytics account object, containing all information associated
    with the named Data Lake Analytics account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :ivar provisioning_state: the provisioning status of the Data Lake
     Analytics account. Possible values include: 'Failed', 'Creating',
     'Running', 'Succeeded', 'Patching', 'Suspending', 'Resuming', 'Deleting',
     'Deleted'
    :vartype provisioning_state: str or :class:`DataLakeAnalyticsAccountStatus
     <azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountStatus>`
    :ivar state: the state of the Data Lake Analytics account. Possible values
     include: 'Active', 'Suspended'
    :vartype state: str or :class:`DataLakeAnalyticsAccountState
     <azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountState>`
    :param default_data_lake_store_account: the default data lake storage
     account associated with this Data Lake Analytics account.
    :type default_data_lake_store_account: str
    :param max_degree_of_parallelism: the maximum supported degree of
     parallelism for this account. Default value: 30 .
    :type max_degree_of_parallelism: int
    :param query_store_retention: the number of days that job metadata is
     retained. Default value: 30 .
    :type query_store_retention: int
    :param max_job_count: the maximum supported jobs running under the account
     at the same time. Default value: 3 .
    :type max_job_count: int
    :ivar system_max_degree_of_parallelism: the system defined maximum
     supported degree of parallelism for this account, which restricts the
     maximum value of parallelism the user can set for the account..
    :vartype system_max_degree_of_parallelism: int
    :ivar system_max_job_count: the system defined maximum supported jobs
     running under the account at the same time, which restricts the maximum
     number of running jobs the user can set for the account.
    :vartype system_max_job_count: int
    :param data_lake_store_accounts: the list of Data Lake storage accounts
     associated with this account.
    :type data_lake_store_accounts: list of :class:`DataLakeStoreAccountInfo
     <azure.mgmt.datalake.analytics.account.models.DataLakeStoreAccountInfo>`
    :param storage_accounts: the list of Azure Blob storage accounts
     associated with this account.
    :type storage_accounts: list of :class:`StorageAccountInfo
     <azure.mgmt.datalake.analytics.account.models.StorageAccountInfo>`
    :ivar creation_time: the account creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: the account last modified time.
    :vartype last_modified_time: datetime
    :ivar endpoint: the full CName endpoint for this account.
    :vartype endpoint: str
    :param new_tier: the billing tier to use for next month. Possible values
     include: 'Consumption', 'Commitment_100AUHours', 'Commitment_500AUHours',
     'Commitment_1000AUHours', 'Commitment_5000AUHours',
     'Commitment_10000AUHours', 'Commitment_50000AUHours',
     'Commitment_100000AUHours', 'Commitment_500000AUHours'
    :type new_tier: str or :class:`PricingTierType
     <azure.mgmt.datalake.analytics.account.models.PricingTierType>`
    :ivar current_tier: the billing tier in use for the current month.
     Possible values include: 'Consumption', 'Commitment_100AUHours',
     'Commitment_500AUHours', 'Commitment_1000AUHours',
     'Commitment_5000AUHours', 'Commitment_10000AUHours',
     'Commitment_50000AUHours', 'Commitment_100000AUHours',
     'Commitment_500000AUHours'
    :vartype current_tier: str or :class:`PricingTierType
     <azure.mgmt.datalake.analytics.account.models.PricingTierType>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'state': {'readonly': True},
        'default_data_lake_store_account': {'required': True},
        'max_degree_of_parallelism': {'minimum': 1},
        'query_store_retention': {'maximum': 180, 'minimum': 1},
        'max_job_count': {'minimum': 1},
        'system_max_degree_of_parallelism': {'readonly': True},
        'system_max_job_count': {'readonly': True},
        'data_lake_store_accounts': {'required': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'endpoint': {'readonly': True},
        'current_tier': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'DataLakeAnalyticsAccountStatus'},
        'state': {'key': 'properties.state', 'type': 'DataLakeAnalyticsAccountState'},
        'default_data_lake_store_account': {'key': 'properties.defaultDataLakeStoreAccount', 'type': 'str'},
        'max_degree_of_parallelism': {'key': 'properties.maxDegreeOfParallelism', 'type': 'int'},
        'query_store_retention': {'key': 'properties.queryStoreRetention', 'type': 'int'},
        'max_job_count': {'key': 'properties.maxJobCount', 'type': 'int'},
        'system_max_degree_of_parallelism': {'key': 'properties.systemMaxDegreeOfParallelism', 'type': 'int'},
        'system_max_job_count': {'key': 'properties.systemMaxJobCount', 'type': 'int'},
        'data_lake_store_accounts': {'key': 'properties.dataLakeStoreAccounts', 'type': '[DataLakeStoreAccountInfo]'},
        'storage_accounts': {'key': 'properties.storageAccounts', 'type': '[StorageAccountInfo]'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
        'new_tier': {'key': 'properties.newTier', 'type': 'PricingTierType'},
        'current_tier': {'key': 'properties.currentTier', 'type': 'PricingTierType'},
    }

    def __init__(self, location, default_data_lake_store_account, data_lake_store_accounts, tags=None, max_degree_of_parallelism=30, query_store_retention=30, max_job_count=3, storage_accounts=None, new_tier=None):
        super(DataLakeAnalyticsAccount, self).__init__(location=location, tags=tags)
        self.provisioning_state = None
        self.state = None
        self.default_data_lake_store_account = default_data_lake_store_account
        self.max_degree_of_parallelism = max_degree_of_parallelism
        self.query_store_retention = query_store_retention
        self.max_job_count = max_job_count
        self.system_max_degree_of_parallelism = None
        self.system_max_job_count = None
        self.data_lake_store_accounts = data_lake_store_accounts
        self.storage_accounts = storage_accounts
        self.creation_time = None
        self.last_modified_time = None
        self.endpoint = None
        self.new_tier = new_tier
        self.current_tier = None
