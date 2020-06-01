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

from enum import Enum


class Reason(str, Enum):

    account_name_invalid = "AccountNameInvalid"
    already_exists = "AlreadyExists"


class SkuName(str, Enum):

    standard_lrs = "Standard_LRS"
    standard_grs = "Standard_GRS"
    standard_ragrs = "Standard_RAGRS"
    standard_zrs = "Standard_ZRS"
    premium_lrs = "Premium_LRS"


class SkuTier(str, Enum):

    standard = "Standard"
    premium = "Premium"


class AccessTier(str, Enum):

    hot = "Hot"
    cool = "Cool"


class Kind(str, Enum):

    storage = "Storage"
    blob_storage = "BlobStorage"


class ProvisioningState(str, Enum):

    creating = "Creating"
    resolving_dns = "ResolvingDNS"
    succeeded = "Succeeded"


class AccountStatus(str, Enum):

    available = "available"
    unavailable = "unavailable"


class KeyPermission(str, Enum):

    read = "Read"
    full = "Full"


class UsageUnit(str, Enum):

    count = "Count"
    bytes = "Bytes"
    seconds = "Seconds"
    percent = "Percent"
    counts_per_second = "CountsPerSecond"
    bytes_per_second = "BytesPerSecond"


class HttpProtocol(str, Enum):

    httpshttp = "https,http"
    https = "https"


class SignedResource(str, Enum):

    b = "b"
    c = "c"
    f = "f"
    s = "s"


class Permissions(str, Enum):

    r = "r"
    d = "d"
    w = "w"
    l = "l"
    a = "a"
    c = "c"
    u = "u"
    p = "p"
