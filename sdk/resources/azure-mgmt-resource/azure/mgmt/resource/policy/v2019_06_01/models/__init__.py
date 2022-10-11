# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ErrorResponse
from ._models_py3 import Identity
from ._models_py3 import PolicyAssignment
from ._models_py3 import PolicyAssignmentListResult
from ._models_py3 import PolicyDefinition
from ._models_py3 import PolicyDefinitionListResult
from ._models_py3 import PolicyDefinitionReference
from ._models_py3 import PolicySetDefinition
from ._models_py3 import PolicySetDefinitionListResult
from ._models_py3 import PolicySku

from ._policy_client_enums import EnforcementMode
from ._policy_client_enums import PolicyType
from ._policy_client_enums import ResourceIdentityType
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ErrorResponse",
    "Identity",
    "PolicyAssignment",
    "PolicyAssignmentListResult",
    "PolicyDefinition",
    "PolicyDefinitionListResult",
    "PolicyDefinitionReference",
    "PolicySetDefinition",
    "PolicySetDefinitionListResult",
    "PolicySku",
    "EnforcementMode",
    "PolicyType",
    "ResourceIdentityType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
