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

from msrest.serialization import Model


class AzureReachabilityReportParameters(Model):
    """Geographic and time constraints for Azure reachability report.

    All required parameters must be populated in order to send to Azure.

    :param provider_location: Required.
    :type provider_location:
     ~azure.mgmt.network.v2017_10_01.models.AzureReachabilityReportLocation
    :param providers: List of Internet service providers.
    :type providers: list[str]
    :param azure_locations: Optional Azure regions to scope the query to.
    :type azure_locations: list[str]
    :param start_time: Required. The start time for the Azure reachability
     report.
    :type start_time: datetime
    :param end_time: Required. The end time for the Azure reachability report.
    :type end_time: datetime
    """

    _validation = {
        'provider_location': {'required': True},
        'start_time': {'required': True},
        'end_time': {'required': True},
    }

    _attribute_map = {
        'provider_location': {'key': 'providerLocation', 'type': 'AzureReachabilityReportLocation'},
        'providers': {'key': 'providers', 'type': '[str]'},
        'azure_locations': {'key': 'azureLocations', 'type': '[str]'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
    }

    def __init__(self, *, provider_location, start_time, end_time, providers=None, azure_locations=None, **kwargs) -> None:
        super(AzureReachabilityReportParameters, self).__init__(**kwargs)
        self.provider_location = provider_location
        self.providers = providers
        self.azure_locations = azure_locations
        self.start_time = start_time
        self.end_time = end_time
