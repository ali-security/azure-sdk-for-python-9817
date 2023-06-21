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

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import ContainerServiceFleetMgmtClientConfiguration
from ._serialization import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class ContainerServiceFleetMgmtClient(MultiApiClientMixin, _SDKClient):
    """Azure Kubernetes Fleet Manager api client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2023-03-15-preview'
    _PROFILE_TAG = "azure.mgmt.containerservicefleet.ContainerServiceFleetMgmtClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        api_version: Optional[str]=None,
        base_url: str = "https://management.azure.com",
        profile: KnownProfiles=KnownProfiles.default,
        **kwargs: Any
    ):
        self._config = ContainerServiceFleetMgmtClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(ContainerServiceFleetMgmtClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2022-09-02-preview: :mod:`v2022_06_02_preview.models<azure.mgmt.containerservicefleet.v2022_06_02_preview.models>`
           * 2022-07-02-preview: :mod:`v2022_07_02_preview.models<azure.mgmt.containerservicefleet.v2022_07_02_preview.models>`
           * 2022-06-02-preview: :mod:`v2022_09_02_preview.models<azure.mgmt.containerservicefleet.v2022_09_02_preview.models>`
           * 2023-03-15-preview: :mod:`v2023_03_15_preview.models<azure.mgmt.containerservicefleet.v2023_03_15_preview.models>`
        """
        if api_version == '2022-09-02-preview':
            from .v2022_06_02_preview import models
            return models
        elif api_version == '2022-07-02-preview':
            from .v2022_07_02_preview import models
            return models
        elif api_version == '2022-06-02-preview':
            from .v2022_09_02_preview import models
            return models
        elif api_version == '2023-03-15-preview':
            from .v2023_03_15_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def fleet_members(self):
        """Instance depends on the API version:

           * 2022-09-02-preview: :class:`FleetMembersOperations<azure.mgmt.containerservicefleet.v2022_06_02_preview.operations.FleetMembersOperations>`
           * 2022-07-02-preview: :class:`FleetMembersOperations<azure.mgmt.containerservicefleet.v2022_07_02_preview.operations.FleetMembersOperations>`
           * 2022-06-02-preview: :class:`FleetMembersOperations<azure.mgmt.containerservicefleet.v2022_09_02_preview.operations.FleetMembersOperations>`
           * 2023-03-15-preview: :class:`FleetMembersOperations<azure.mgmt.containerservicefleet.v2023_03_15_preview.operations.FleetMembersOperations>`
        """
        api_version = self._get_api_version('fleet_members')
        if api_version == '2022-09-02-preview':
            from .v2022_06_02_preview.operations import FleetMembersOperations as OperationClass
        elif api_version == '2022-07-02-preview':
            from .v2022_07_02_preview.operations import FleetMembersOperations as OperationClass
        elif api_version == '2022-06-02-preview':
            from .v2022_09_02_preview.operations import FleetMembersOperations as OperationClass
        elif api_version == '2023-03-15-preview':
            from .v2023_03_15_preview.operations import FleetMembersOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'fleet_members'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def fleets(self):
        """Instance depends on the API version:

           * 2022-09-02-preview: :class:`FleetsOperations<azure.mgmt.containerservicefleet.v2022_06_02_preview.operations.FleetsOperations>`
           * 2022-07-02-preview: :class:`FleetsOperations<azure.mgmt.containerservicefleet.v2022_07_02_preview.operations.FleetsOperations>`
           * 2022-06-02-preview: :class:`FleetsOperations<azure.mgmt.containerservicefleet.v2022_09_02_preview.operations.FleetsOperations>`
           * 2023-03-15-preview: :class:`FleetsOperations<azure.mgmt.containerservicefleet.v2023_03_15_preview.operations.FleetsOperations>`
        """
        api_version = self._get_api_version('fleets')
        if api_version == '2022-09-02-preview':
            from .v2022_06_02_preview.operations import FleetsOperations as OperationClass
        elif api_version == '2022-07-02-preview':
            from .v2022_07_02_preview.operations import FleetsOperations as OperationClass
        elif api_version == '2022-06-02-preview':
            from .v2022_09_02_preview.operations import FleetsOperations as OperationClass
        elif api_version == '2023-03-15-preview':
            from .v2023_03_15_preview.operations import FleetsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'fleets'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2022-09-02-preview: :class:`Operations<azure.mgmt.containerservicefleet.v2022_06_02_preview.operations.Operations>`
           * 2023-03-15-preview: :class:`Operations<azure.mgmt.containerservicefleet.v2023_03_15_preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2022-09-02-preview':
            from .v2022_06_02_preview.operations import Operations as OperationClass
        elif api_version == '2023-03-15-preview':
            from .v2023_03_15_preview.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def update_runs(self):
        """Instance depends on the API version:

           * 2023-03-15-preview: :class:`UpdateRunsOperations<azure.mgmt.containerservicefleet.v2023_03_15_preview.operations.UpdateRunsOperations>`
        """
        api_version = self._get_api_version('update_runs')
        if api_version == '2023-03-15-preview':
            from .v2023_03_15_preview.operations import UpdateRunsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'update_runs'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
