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

from .tracked_resource import TrackedResource


class Database(TrackedResource):
    """A database resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. Resource location.
    :type location: str
    :param sku: The name and tier of the SKU.
    :type sku: ~azure.mgmt.sql.models.Sku
    :ivar kind: Kind of database. This is metadata used for the Azure portal
     experience.
    :vartype kind: str
    :ivar managed_by: Resource that manages the database.
    :vartype managed_by: str
    :param create_mode: Specifies the mode of database creation.
     Default: regular database creation.
     Copy: creates a database as a copy of an existing database.
     sourceDatabaseId must be specified as the resource ID of the source
     database.
     Secondary: creates a database as a secondary replica of an existing
     database. sourceDatabaseId must be specified as the resource ID of the
     existing primary database.
     PointInTimeRestore: Creates a database by restoring a point in time backup
     of an existing database. sourceDatabaseId must be specified as the
     resource ID of the existing database, and restorePointInTime must be
     specified.
     Recovery: Creates a database by restoring a geo-replicated backup.
     sourceDatabaseId must be specified as the recoverable database resource ID
     to restore.
     Restore: Creates a database by restoring a backup of a deleted database.
     sourceDatabaseId must be specified. If sourceDatabaseId is the database's
     original resource ID, then sourceDatabaseDeletionDate must be specified.
     Otherwise sourceDatabaseId must be the restorable dropped database
     resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime
     may also be specified to restore from an earlier point in time.
     RestoreLongTermRetentionBackup: Creates a database by restoring from a
     long term retention vault. recoveryServicesRecoveryPointResourceId must be
     specified as the recovery point resource ID.
     Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for
     DataWarehouse edition. Possible values include: 'Default', 'Copy',
     'Secondary', 'PointInTimeRestore', 'Restore', 'Recovery',
     'RestoreExternalBackup', 'RestoreExternalBackupSecondary',
     'RestoreLongTermRetentionBackup', 'OnlineSecondary'
    :type create_mode: str or ~azure.mgmt.sql.models.CreateMode
    :param collation: The collation of the database.
    :type collation: str
    :param max_size_bytes: The max size of the database expressed in bytes.
    :type max_size_bytes: long
    :param sample_name: The name of the sample schema to apply when creating
     this database. Possible values include: 'AdventureWorksLT',
     'WideWorldImportersStd', 'WideWorldImportersFull'
    :type sample_name: str or ~azure.mgmt.sql.models.SampleName
    :param elastic_pool_id: The resource identifier of the elastic pool
     containing this database.
    :type elastic_pool_id: str
    :param source_database_id: The resource identifier of the source database
     associated with create operation of this database.
    :type source_database_id: str
    :ivar status: The status of the database. Possible values include:
     'Online', 'Restoring', 'RecoveryPending', 'Recovering', 'Suspect',
     'Offline', 'Standby', 'Shutdown', 'EmergencyMode', 'AutoClosed',
     'Copying', 'Creating', 'Inaccessible', 'OfflineSecondary', 'Pausing',
     'Paused', 'Resuming', 'Scaling'
    :vartype status: str or ~azure.mgmt.sql.models.DatabaseStatus
    :ivar database_id: The ID of the database.
    :vartype database_id: str
    :ivar creation_date: The creation date of the database (ISO8601 format).
    :vartype creation_date: datetime
    :ivar current_service_objective_name: The current service level objective
     name of the database.
    :vartype current_service_objective_name: str
    :ivar requested_service_objective_name: The requested service level
     objective name of the database.
    :vartype requested_service_objective_name: str
    :ivar default_secondary_location: The default secondary region for this
     database.
    :vartype default_secondary_location: str
    :ivar failover_group_id: Failover Group resource identifier that this
     database belongs to.
    :vartype failover_group_id: str
    :param restore_point_in_time: Specifies the point in time (ISO8601 format)
     of the source database that will be restored to create the new database.
    :type restore_point_in_time: datetime
    :param source_database_deletion_date: Specifies the time that the database
     was deleted.
    :type source_database_deletion_date: datetime
    :param recovery_services_recovery_point_id: The resource identifier of the
     recovery point associated with create operation of this database.
    :type recovery_services_recovery_point_id: str
    :param long_term_retention_backup_resource_id: The resource identifier of
     the long term retention backup associated with create operation of this
     database.
    :type long_term_retention_backup_resource_id: str
    :param recoverable_database_id: The resource identifier of the recoverable
     database associated with create operation of this database.
    :type recoverable_database_id: str
    :param restorable_dropped_database_id: The resource identifier of the
     restorable dropped database associated with create operation of this
     database.
    :type restorable_dropped_database_id: str
    :param catalog_collation: Collation of the metadata catalog. Possible
     values include: 'DATABASE_DEFAULT', 'SQL_Latin1_General_CP1_CI_AS'
    :type catalog_collation: str or
     ~azure.mgmt.sql.models.CatalogCollationType
    :param zone_redundant: Whether or not this database is zone redundant,
     which means the replicas of this database will be spread across multiple
     availability zones.
    :type zone_redundant: bool
    :param license_type: The license type to apply for this database. Possible
     values include: 'LicenseIncluded', 'BasePrice'
    :type license_type: str or ~azure.mgmt.sql.models.DatabaseLicenseType
    :ivar max_log_size_bytes: The max log size for this database.
    :vartype max_log_size_bytes: long
    :ivar earliest_restore_date: This records the earliest start date and time
     that restore is available for this database (ISO8601 format).
    :vartype earliest_restore_date: datetime
    :param read_scale: The state of read-only routing. If enabled, connections
     that have application intent set to readonly in their connection string
     may be routed to a readonly secondary replica in the same region. Possible
     values include: 'Enabled', 'Disabled'
    :type read_scale: str or ~azure.mgmt.sql.models.DatabaseReadScale
    :ivar current_sku: The name and tier of the SKU.
    :vartype current_sku: ~azure.mgmt.sql.models.Sku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'kind': {'readonly': True},
        'managed_by': {'readonly': True},
        'status': {'readonly': True},
        'database_id': {'readonly': True},
        'creation_date': {'readonly': True},
        'current_service_objective_name': {'readonly': True},
        'requested_service_objective_name': {'readonly': True},
        'default_secondary_location': {'readonly': True},
        'failover_group_id': {'readonly': True},
        'max_log_size_bytes': {'readonly': True},
        'earliest_restore_date': {'readonly': True},
        'current_sku': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'kind': {'key': 'kind', 'type': 'str'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'create_mode': {'key': 'properties.createMode', 'type': 'str'},
        'collation': {'key': 'properties.collation', 'type': 'str'},
        'max_size_bytes': {'key': 'properties.maxSizeBytes', 'type': 'long'},
        'sample_name': {'key': 'properties.sampleName', 'type': 'str'},
        'elastic_pool_id': {'key': 'properties.elasticPoolId', 'type': 'str'},
        'source_database_id': {'key': 'properties.sourceDatabaseId', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'database_id': {'key': 'properties.databaseId', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'current_service_objective_name': {'key': 'properties.currentServiceObjectiveName', 'type': 'str'},
        'requested_service_objective_name': {'key': 'properties.requestedServiceObjectiveName', 'type': 'str'},
        'default_secondary_location': {'key': 'properties.defaultSecondaryLocation', 'type': 'str'},
        'failover_group_id': {'key': 'properties.failoverGroupId', 'type': 'str'},
        'restore_point_in_time': {'key': 'properties.restorePointInTime', 'type': 'iso-8601'},
        'source_database_deletion_date': {'key': 'properties.sourceDatabaseDeletionDate', 'type': 'iso-8601'},
        'recovery_services_recovery_point_id': {'key': 'properties.recoveryServicesRecoveryPointId', 'type': 'str'},
        'long_term_retention_backup_resource_id': {'key': 'properties.longTermRetentionBackupResourceId', 'type': 'str'},
        'recoverable_database_id': {'key': 'properties.recoverableDatabaseId', 'type': 'str'},
        'restorable_dropped_database_id': {'key': 'properties.restorableDroppedDatabaseId', 'type': 'str'},
        'catalog_collation': {'key': 'properties.catalogCollation', 'type': 'str'},
        'zone_redundant': {'key': 'properties.zoneRedundant', 'type': 'bool'},
        'license_type': {'key': 'properties.licenseType', 'type': 'str'},
        'max_log_size_bytes': {'key': 'properties.maxLogSizeBytes', 'type': 'long'},
        'earliest_restore_date': {'key': 'properties.earliestRestoreDate', 'type': 'iso-8601'},
        'read_scale': {'key': 'properties.readScale', 'type': 'str'},
        'current_sku': {'key': 'properties.currentSku', 'type': 'Sku'},
    }

    def __init__(self, *, location: str, tags=None, sku=None, create_mode=None, collation: str=None, max_size_bytes: int=None, sample_name=None, elastic_pool_id: str=None, source_database_id: str=None, restore_point_in_time=None, source_database_deletion_date=None, recovery_services_recovery_point_id: str=None, long_term_retention_backup_resource_id: str=None, recoverable_database_id: str=None, restorable_dropped_database_id: str=None, catalog_collation=None, zone_redundant: bool=None, license_type=None, read_scale=None, **kwargs) -> None:
        super(Database, self).__init__(tags=tags, location=location, **kwargs)
        self.sku = sku
        self.kind = None
        self.managed_by = None
        self.create_mode = create_mode
        self.collation = collation
        self.max_size_bytes = max_size_bytes
        self.sample_name = sample_name
        self.elastic_pool_id = elastic_pool_id
        self.source_database_id = source_database_id
        self.status = None
        self.database_id = None
        self.creation_date = None
        self.current_service_objective_name = None
        self.requested_service_objective_name = None
        self.default_secondary_location = None
        self.failover_group_id = None
        self.restore_point_in_time = restore_point_in_time
        self.source_database_deletion_date = source_database_deletion_date
        self.recovery_services_recovery_point_id = recovery_services_recovery_point_id
        self.long_term_retention_backup_resource_id = long_term_retention_backup_resource_id
        self.recoverable_database_id = recoverable_database_id
        self.restorable_dropped_database_id = restorable_dropped_database_id
        self.catalog_collation = catalog_collation
        self.zone_redundant = zone_redundant
        self.license_type = license_type
        self.max_log_size_bytes = None
        self.earliest_restore_date = None
        self.read_scale = read_scale
        self.current_sku = None
