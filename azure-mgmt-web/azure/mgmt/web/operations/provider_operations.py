# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
import uuid

from .. import models


class ProviderOperations(object):
    """ProviderOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_source_controls(
            self, custom_headers={}, raw=False, **operation_config):
        """
        Gets the source controls available for Azure websites

        :param dict custom_headers: headers that will be added to the request
        :param boolean raw: returns the direct response alongside the
         deserialized response
        :rtype: SourceControlCollection
        :rtype: msrest.pipeline.ClientRawResponse if raw=True
        """
        # Construct URL
        url = '/providers/Microsoft.Web/sourcecontrols'

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

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
            deserialized = self._deserialize('SourceControlCollection', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get_source_control(
            self, source_control_type, custom_headers={}, raw=False, **operation_config):
        """
        Gets source control token

        :param source_control_type: Type of source control
        :type source_control_type: str
        :param dict custom_headers: headers that will be added to the request
        :param boolean raw: returns the direct response alongside the
         deserialized response
        :rtype: SourceControl
        :rtype: msrest.pipeline.ClientRawResponse if raw=True
        """
        # Construct URL
        url = '/providers/Microsoft.Web/sourcecontrols/{sourceControlType}'
        path_format_arguments = {
            'sourceControlType': self._serialize.url("source_control_type", source_control_type, 'str')
        }
        url = url.format(**path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

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
            deserialized = self._deserialize('SourceControl', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def update_source_control(
            self, source_control_type, request_message, custom_headers={}, raw=False, **operation_config):
        """
        Updates source control token

        :param source_control_type: Type of source control
        :type source_control_type: str
        :param request_message: Source control token information
        :type request_message: SourceControl
        :param dict custom_headers: headers that will be added to the request
        :param boolean raw: returns the direct response alongside the
         deserialized response
        :rtype: SourceControl
        :rtype: msrest.pipeline.ClientRawResponse if raw=True
        """
        # Construct URL
        url = '/providers/Microsoft.Web/sourcecontrols/{sourceControlType}'
        path_format_arguments = {
            'sourceControlType': self._serialize.url("source_control_type", source_control_type, 'str')
        }
        url = url.format(**path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

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
        body_content = self._serialize.body(request_message, 'SourceControl')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SourceControl', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get_publishing_user(
            self, custom_headers={}, raw=False, **operation_config):
        """
        Gets publishing user

        :param dict custom_headers: headers that will be added to the request
        :param boolean raw: returns the direct response alongside the
         deserialized response
        :rtype: User
        :rtype: msrest.pipeline.ClientRawResponse if raw=True
        """
        # Construct URL
        url = '/providers/Microsoft.Web/publishingUsers/web'

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

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
            deserialized = self._deserialize('User', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def update_publishing_user(
            self, request_message, custom_headers={}, raw=False, **operation_config):
        """
        Updates publishing user

        :param request_message: Details of publishing user
        :type request_message: User
        :param dict custom_headers: headers that will be added to the request
        :param boolean raw: returns the direct response alongside the
         deserialized response
        :rtype: User
        :rtype: msrest.pipeline.ClientRawResponse if raw=True
        """
        # Construct URL
        url = '/providers/Microsoft.Web/publishingUsers/web'

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

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
        body_content = self._serialize.body(request_message, 'User')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('User', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
