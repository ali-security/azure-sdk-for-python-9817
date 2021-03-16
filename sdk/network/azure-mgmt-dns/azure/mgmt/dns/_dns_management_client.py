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

from azure.mgmt.core import ARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import DnsManagementClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class DnsManagementClient(MultiApiClientMixin, _SDKClient):
    """The DNS Management Client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Specifies the Azure subscription ID, which uniquely identifies the Microsoft Azure subscription.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2018-05-01'
    _PROFILE_TAG = "azure.mgmt.dns.DnsManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DnsManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(DnsManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-04-01: :mod:`v2016_04_01.models<azure.mgmt.dns.v2016_04_01.models>`
           * 2018-03-01-preview: :mod:`v2018_03_01_preview.models<azure.mgmt.dns.v2018_03_01_preview.models>`
           * 2018-05-01: :mod:`v2018_05_01.models<azure.mgmt.dns.v2018_05_01.models>`
        """
        if api_version == '2016-04-01':
            from .v2016_04_01 import models
            return models
        elif api_version == '2018-03-01-preview':
            from .v2018_03_01_preview import models
            return models
        elif api_version == '2018-05-01':
            from .v2018_05_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def dns_resource_reference(self):
        """Instance depends on the API version:

           * 2018-05-01: :class:`DnsResourceReferenceOperations<azure.mgmt.dns.v2018_05_01.operations.DnsResourceReferenceOperations>`
        """
        api_version = self._get_api_version('dns_resource_reference')
        if api_version == '2018-05-01':
            from .v2018_05_01.operations import DnsResourceReferenceOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'dns_resource_reference'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def record_sets(self):
        """Instance depends on the API version:

           * 2016-04-01: :class:`RecordSetsOperations<azure.mgmt.dns.v2016_04_01.operations.RecordSetsOperations>`
           * 2018-03-01-preview: :class:`RecordSetsOperations<azure.mgmt.dns.v2018_03_01_preview.operations.RecordSetsOperations>`
           * 2018-05-01: :class:`RecordSetsOperations<azure.mgmt.dns.v2018_05_01.operations.RecordSetsOperations>`
        """
        api_version = self._get_api_version('record_sets')
        if api_version == '2016-04-01':
            from .v2016_04_01.operations import RecordSetsOperations as OperationClass
        elif api_version == '2018-03-01-preview':
            from .v2018_03_01_preview.operations import RecordSetsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import RecordSetsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'record_sets'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def zones(self):
        """Instance depends on the API version:

           * 2016-04-01: :class:`ZonesOperations<azure.mgmt.dns.v2016_04_01.operations.ZonesOperations>`
           * 2018-03-01-preview: :class:`ZonesOperations<azure.mgmt.dns.v2018_03_01_preview.operations.ZonesOperations>`
           * 2018-05-01: :class:`ZonesOperations<azure.mgmt.dns.v2018_05_01.operations.ZonesOperations>`
        """
        api_version = self._get_api_version('zones')
        if api_version == '2016-04-01':
            from .v2016_04_01.operations import ZonesOperations as OperationClass
        elif api_version == '2018-03-01-preview':
            from .v2018_03_01_preview.operations import ZonesOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import ZonesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'zones'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
