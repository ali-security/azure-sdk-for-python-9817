# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Action(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A string property that indicates the action to be performed on the Flink job. It can have one
    of the following enum values => NEW, UPDATE, STATELESS_UPDATE, STOP, START, CANCEL, SAVEPOINT,
    LIST_SAVEPOINT, or DELETE.
    """

    NEW = "NEW"
    UPDATE = "UPDATE"
    STATELESS_UPDATE = "STATELESS_UPDATE"
    STOP = "STOP"
    START = "START"
    CANCEL = "CANCEL"
    SAVEPOINT = "SAVEPOINT"
    LIST_SAVEPOINT = "LIST_SAVEPOINT"
    DELETE = "DELETE"


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class AutoscaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """User to specify which type of Autoscale to be implemented - Scheduled Based or Load Based."""

    SCHEDULE_BASED = "ScheduleBased"
    LOAD_BASED = "LoadBased"


class ComparisonOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The comparison operator."""

    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL = "greaterThanOrEqual"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL = "lessThanOrEqual"


class ContentEncoding(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This property indicates if the content is encoded and is case-insensitive. Please set the value
    to base64 if the content is base64 encoded. Set it to none or skip it if the content is plain
    text.
    """

    BASE64 = "Base64"
    NONE = "None"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class JobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of cluster job."""

    FLINK_JOB = "FlinkJob"


class KeyVaultObjectType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of key vault object: secret, key or certificate."""

    KEY = "Key"
    SECRET = "Secret"
    CERTIFICATE = "Certificate"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class ProvisioningStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the resource."""

    ACCEPTED = "Accepted"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"


class ScaleActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action type."""

    SCALEUP = "scaleup"
    SCALEDOWN = "scaledown"


class ScheduleDay(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ScheduleDay."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
