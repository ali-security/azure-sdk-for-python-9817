# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SourceControlSyncJobStreamsOperations(object):
    """SourceControlSyncJobStreamsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.automation.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_sync_job(
        self,
        resource_group_name,  # type: str
        automation_account_name,  # type: str
        source_control_name,  # type: str
        source_control_sync_job_id,  # type: str
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.SourceControlSyncJobStreamsListBySyncJob"]
        """Retrieve a list of sync job streams identified by sync job id.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param source_control_name: The source control name.
        :type source_control_name: str
        :param source_control_sync_job_id: The source control sync job id.
        :type source_control_sync_job_id: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SourceControlSyncJobStreamsListBySyncJob or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.automation.models.SourceControlSyncJobStreamsListBySyncJob]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SourceControlSyncJobStreamsListBySyncJob"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2017-05-15-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_sync_job.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
                    'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
                    'sourceControlName': self._serialize.url("source_control_name", source_control_name, 'str'),
                    'sourceControlSyncJobId': self._serialize.url("source_control_sync_job_id", source_control_sync_job_id, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('SourceControlSyncJobStreamsListBySyncJob', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_sync_job.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}/streams'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        automation_account_name,  # type: str
        source_control_name,  # type: str
        source_control_sync_job_id,  # type: str
        stream_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SourceControlSyncJobStreamById"
        """Retrieve a sync job stream identified by stream id.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param source_control_name: The source control name.
        :type source_control_name: str
        :param source_control_sync_job_id: The source control sync job id.
        :type source_control_sync_job_id: str
        :param stream_id: The id of the sync job stream.
        :type stream_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SourceControlSyncJobStreamById, or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.SourceControlSyncJobStreamById
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SourceControlSyncJobStreamById"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2017-05-15-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
            'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
            'sourceControlName': self._serialize.url("source_control_name", source_control_name, 'str'),
            'sourceControlSyncJobId': self._serialize.url("source_control_sync_job_id", source_control_sync_job_id, 'str'),
            'streamId': self._serialize.url("stream_id", stream_id, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SourceControlSyncJobStreamById', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}/streams/{streamId}'}  # type: ignore
