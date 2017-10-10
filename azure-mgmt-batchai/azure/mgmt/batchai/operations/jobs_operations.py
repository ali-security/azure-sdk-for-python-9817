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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_operation import AzureOperationPoller

from .. import models


class JobsOperations(object):
    """JobsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: Specifies the version of API used for this request. Constant value: "2017-09-01-preview".
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2017-09-01-preview"

        self.config = config

    def create(
            self, resource_group_name, job_name, parameters, custom_headers=None, raw=False, **operation_config):
        """Adds a Job that gets executed on a cluster.

        :param resource_group_name: Name of the resource group to which the
         resource belongs.
        :type resource_group_name: str
        :param job_name: The name of the job within the specified resource
         group. Job names can only contain a combination of alphanumeric
         characters along with dash (-) and underscore (_). The name must be
         from 1 through 64 characters long.
        :type job_name: str
        :param parameters: The parameters to provide for job creation.
        :type parameters: :class:`JobCreateParameters
         <azure.mgmt.batchai.models.JobCreateParameters>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`Job <azure.mgmt.batchai.models.Job>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         or :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BatchAI/jobs/{jobName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[-\w\._]+$'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'JobCreateParameters')

        # Construct and send request
        def long_running_send():

            request = self._client.put(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            deserialized = None

            if response.status_code == 200:
                deserialized = self._deserialize('Job', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def delete(
            self, resource_group_name, job_name, custom_headers=None, raw=False, **operation_config):
        """Deletes the specified Batch AI job.

        :param resource_group_name: Name of the resource group to which the
         resource belongs.
        :type resource_group_name: str
        :param job_name: The name of the job within the specified resource
         group. Job names can only contain a combination of alphanumeric
         characters along with dash (-) and underscore (_). The name must be
         from 1 through 64 characters long.
        :type job_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         or :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BatchAI/jobs/{jobName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[-\w\._]+$'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        def long_running_send():

            request = self._client.delete(url, query_parameters)
            return self._client.send(request, header_parameters, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202, 204]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def get(
            self, resource_group_name, job_name, custom_headers=None, raw=False, **operation_config):
        """Gets information about the specified Batch AI job.

        :param resource_group_name: Name of the resource group to which the
         resource belongs.
        :type resource_group_name: str
        :param job_name: The name of the job within the specified resource
         group. Job names can only contain a combination of alphanumeric
         characters along with dash (-) and underscore (_). The name must be
         from 1 through 64 characters long.
        :type job_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: :class:`Job <azure.mgmt.batchai.models.Job>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: :class:`Job <azure.mgmt.batchai.models.Job>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BatchAI/jobs/{jobName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[-\w\._]+$'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Job', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def list_remote_login_information(
            self, resource_group_name, job_name, custom_headers=None, raw=False, **operation_config):
        """Gets the IP address and port information of all the compute nodes which
        are used for job execution.

        :param resource_group_name: Name of the resource group to which the
         resource belongs.
        :type resource_group_name: str
        :param job_name: The name of the job within the specified resource
         group. Job names can only contain a combination of alphanumeric
         characters along with dash (-) and underscore (_). The name must be
         from 1 through 64 characters long.
        :type job_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`RemoteLoginInformation
         <azure.mgmt.batchai.models.RemoteLoginInformation>`
        :rtype: :class:`RemoteLoginInformationPaged
         <azure.mgmt.batchai.models.RemoteLoginInformationPaged>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BatchAI/jobs/{jobName}/listRemoteLoginInformation'
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[-\w\._]+$'),
                    'jobName': self._serialize.url("job_name", job_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._]+$'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.post(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.RemoteLoginInformationPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.RemoteLoginInformationPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def terminate(
            self, resource_group_name, job_name, custom_headers=None, raw=False, **operation_config):
        """Terminates a job.

        :param resource_group_name: Name of the resource group to which the
         resource belongs.
        :type resource_group_name: str
        :param job_name: The name of the job within the specified resource
         group. Job names can only contain a combination of alphanumeric
         characters along with dash (-) and underscore (_). The name must be
         from 1 through 64 characters long.
        :type job_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         or :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BatchAI/jobs/{jobName}/terminate'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[-\w\._]+$'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        def long_running_send():

            request = self._client.post(url, query_parameters)
            return self._client.send(request, header_parameters, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def list(
            self, jobs_list_options=None, custom_headers=None, raw=False, **operation_config):
        """Gets information about the jobs associated with the subscription.

        :param jobs_list_options: Additional parameters for the operation
        :type jobs_list_options: :class:`JobsListOptions
         <azure.mgmt.batchai.models.JobsListOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`Job
         <azure.mgmt.batchai.models.Job>`
        :rtype: :class:`JobPaged <azure.mgmt.batchai.models.JobPaged>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        filter = None
        if jobs_list_options is not None:
            filter = jobs_list_options.filter
        select = None
        if jobs_list_options is not None:
            select = jobs_list_options.select
        max_results = None
        if jobs_list_options is not None:
            max_results = jobs_list_options.max_results

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/providers/Microsoft.BatchAI/jobs'
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, 'str')
                if max_results is not None:
                    query_parameters['maxresults'] = self._serialize.query("max_results", max_results, 'int', maximum=1000, minimum=1)

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.JobPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.JobPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def list_by_resource_group(
            self, resource_group_name, jobs_list_by_resource_group_options=None, custom_headers=None, raw=False, **operation_config):
        """Gets information about the Batch AI jobs associated within the
        specified resource group.

        :param resource_group_name: Name of the resource group to which the
         resource belongs.
        :type resource_group_name: str
        :param jobs_list_by_resource_group_options: Additional parameters for
         the operation
        :type jobs_list_by_resource_group_options:
         :class:`JobsListByResourceGroupOptions
         <azure.mgmt.batchai.models.JobsListByResourceGroupOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`Job
         <azure.mgmt.batchai.models.Job>`
        :rtype: :class:`JobPaged <azure.mgmt.batchai.models.JobPaged>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        filter = None
        if jobs_list_by_resource_group_options is not None:
            filter = jobs_list_by_resource_group_options.filter
        select = None
        if jobs_list_by_resource_group_options is not None:
            select = jobs_list_by_resource_group_options.select
        max_results = None
        if jobs_list_by_resource_group_options is not None:
            max_results = jobs_list_by_resource_group_options.max_results

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BatchAI/jobs'
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[-\w\._]+$'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, 'str')
                if max_results is not None:
                    query_parameters['maxresults'] = self._serialize.query("max_results", max_results, 'int', maximum=1000, minimum=1)

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.JobPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.JobPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def list_output_files(
            self, resource_group_name, job_name, jobs_list_output_files_options, custom_headers=None, raw=False, **operation_config):
        """List all files inside the given output directory (Only if the output
        directory is on Azure File Share or Azure Storage container).

        :param resource_group_name: Name of the resource group to which the
         resource belongs.
        :type resource_group_name: str
        :param job_name: The name of the job within the specified resource
         group. Job names can only contain a combination of alphanumeric
         characters along with dash (-) and underscore (_). The name must be
         from 1 through 64 characters long.
        :type job_name: str
        :param jobs_list_output_files_options: Additional parameters for the
         operation
        :type jobs_list_output_files_options:
         :class:`JobsListOutputFilesOptions
         <azure.mgmt.batchai.models.JobsListOutputFilesOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`File
         <azure.mgmt.batchai.models.File>`
        :rtype: :class:`FilePaged <azure.mgmt.batchai.models.FilePaged>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        outputdirectoryid = None
        if jobs_list_output_files_options is not None:
            outputdirectoryid = jobs_list_output_files_options.outputdirectoryid
        linkexpiryinminutes = None
        if jobs_list_output_files_options is not None:
            linkexpiryinminutes = jobs_list_output_files_options.linkexpiryinminutes
        max_results = None
        if jobs_list_output_files_options is not None:
            max_results = jobs_list_output_files_options.max_results

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BatchAI/jobs/{jobName}/listOutputFiles'
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[-\w\._]+$'),
                    'jobName': self._serialize.url("job_name", job_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._]+$'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                query_parameters['outputdirectoryid'] = self._serialize.query("outputdirectoryid", outputdirectoryid, 'str')
                if linkexpiryinminutes is not None:
                    query_parameters['linkexpiryinminutes'] = self._serialize.query("linkexpiryinminutes", linkexpiryinminutes, 'int', maximum=600, minimum=5)
                if max_results is not None:
                    query_parameters['maxresults'] = self._serialize.query("max_results", max_results, 'int', maximum=1000, minimum=1)

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.post(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.FilePaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.FilePaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
