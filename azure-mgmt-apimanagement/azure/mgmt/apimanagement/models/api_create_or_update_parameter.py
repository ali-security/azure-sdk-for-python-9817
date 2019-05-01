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


class ApiCreateOrUpdateParameter(Model):
    """API Create or Update Parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param description: Description of the API. May include HTML formatting
     tags.
    :type description: str
    :param authentication_settings: Collection of authentication settings
     included into this API.
    :type authentication_settings:
     ~azure.mgmt.apimanagement.models.AuthenticationSettingsContract
    :param subscription_key_parameter_names: Protocols over which API is made
     available.
    :type subscription_key_parameter_names:
     ~azure.mgmt.apimanagement.models.SubscriptionKeyParameterNamesContract
    :param api_type: Type of API. Possible values include: 'http', 'soap'
    :type api_type: str or ~azure.mgmt.apimanagement.models.ApiType
    :param api_revision: Describes the Revision of the Api. If no value is
     provided, default revision 1 is created
    :type api_revision: str
    :param api_version: Indicates the Version identifier of the API if the API
     is versioned
    :type api_version: str
    :param is_current: Indicates if API revision is current api revision.
    :type is_current: bool
    :ivar is_online: Indicates if API revision is accessible via the gateway.
    :vartype is_online: bool
    :param api_revision_description: Description of the Api Revision.
    :type api_revision_description: str
    :param api_version_description: Description of the Api Version.
    :type api_version_description: str
    :param api_version_set_id: A resource identifier for the related
     ApiVersionSet.
    :type api_version_set_id: str
    :param subscription_required: Specifies whether an API or Product
     subscription is required for accessing the API.
    :type subscription_required: bool
    :param source_api_id: API identifier of the source API.
    :type source_api_id: str
    :param display_name: API name. Must be 1 to 300 characters long.
    :type display_name: str
    :param service_url: Absolute URL of the backend service implementing this
     API. Cannot be more than 2000 characters long.
    :type service_url: str
    :param path: Required. Relative URL uniquely identifying this API and all
     of its resource paths within the API Management service instance. It is
     appended to the API endpoint base URL specified during the service
     instance creation to form a public URL for this API.
    :type path: str
    :param protocols: Describes on which protocols the operations in this API
     can be invoked.
    :type protocols: list[str or ~azure.mgmt.apimanagement.models.Protocol]
    :param api_version_set: Version set details
    :type api_version_set:
     ~azure.mgmt.apimanagement.models.ApiVersionSetContractDetails
    :param value: Content value when Importing an API.
    :type value: str
    :param format: Format of the Content in which the API is getting imported.
     Possible values include: 'wadl-xml', 'wadl-link-json', 'swagger-json',
     'swagger-link-json', 'wsdl', 'wsdl-link', 'openapi', 'openapi+json',
     'openapi-link'
    :type format: str or ~azure.mgmt.apimanagement.models.ContentFormat
    :param wsdl_selector: Criteria to limit import of WSDL to a subset of the
     document.
    :type wsdl_selector:
     ~azure.mgmt.apimanagement.models.ApiCreateOrUpdatePropertiesWsdlSelector
    :param soap_api_type: Type of Api to create.
     * `http` creates a SOAP to REST API
     * `soap` creates a SOAP pass-through API. Possible values include:
     'SoapToRest', 'SoapPassThrough'
    :type soap_api_type: str or ~azure.mgmt.apimanagement.models.SoapApiType
    """

    _validation = {
        'api_revision': {'max_length': 100, 'min_length': 1},
        'api_version': {'max_length': 100},
        'is_online': {'readonly': True},
        'api_revision_description': {'max_length': 256},
        'api_version_description': {'max_length': 256},
        'display_name': {'max_length': 300, 'min_length': 1},
        'service_url': {'max_length': 2000, 'min_length': 0},
        'path': {'required': True, 'max_length': 400, 'min_length': 0},
    }

    _attribute_map = {
        'description': {'key': 'properties.description', 'type': 'str'},
        'authentication_settings': {'key': 'properties.authenticationSettings', 'type': 'AuthenticationSettingsContract'},
        'subscription_key_parameter_names': {'key': 'properties.subscriptionKeyParameterNames', 'type': 'SubscriptionKeyParameterNamesContract'},
        'api_type': {'key': 'properties.type', 'type': 'str'},
        'api_revision': {'key': 'properties.apiRevision', 'type': 'str'},
        'api_version': {'key': 'properties.apiVersion', 'type': 'str'},
        'is_current': {'key': 'properties.isCurrent', 'type': 'bool'},
        'is_online': {'key': 'properties.isOnline', 'type': 'bool'},
        'api_revision_description': {'key': 'properties.apiRevisionDescription', 'type': 'str'},
        'api_version_description': {'key': 'properties.apiVersionDescription', 'type': 'str'},
        'api_version_set_id': {'key': 'properties.apiVersionSetId', 'type': 'str'},
        'subscription_required': {'key': 'properties.subscriptionRequired', 'type': 'bool'},
        'source_api_id': {'key': 'properties.sourceApiId', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'service_url': {'key': 'properties.serviceUrl', 'type': 'str'},
        'path': {'key': 'properties.path', 'type': 'str'},
        'protocols': {'key': 'properties.protocols', 'type': '[Protocol]'},
        'api_version_set': {'key': 'properties.apiVersionSet', 'type': 'ApiVersionSetContractDetails'},
        'value': {'key': 'properties.value', 'type': 'str'},
        'format': {'key': 'properties.format', 'type': 'str'},
        'wsdl_selector': {'key': 'properties.wsdlSelector', 'type': 'ApiCreateOrUpdatePropertiesWsdlSelector'},
        'soap_api_type': {'key': 'properties.apiType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApiCreateOrUpdateParameter, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.authentication_settings = kwargs.get('authentication_settings', None)
        self.subscription_key_parameter_names = kwargs.get('subscription_key_parameter_names', None)
        self.api_type = kwargs.get('api_type', None)
        self.api_revision = kwargs.get('api_revision', None)
        self.api_version = kwargs.get('api_version', None)
        self.is_current = kwargs.get('is_current', None)
        self.is_online = None
        self.api_revision_description = kwargs.get('api_revision_description', None)
        self.api_version_description = kwargs.get('api_version_description', None)
        self.api_version_set_id = kwargs.get('api_version_set_id', None)
        self.subscription_required = kwargs.get('subscription_required', None)
        self.source_api_id = kwargs.get('source_api_id', None)
        self.display_name = kwargs.get('display_name', None)
        self.service_url = kwargs.get('service_url', None)
        self.path = kwargs.get('path', None)
        self.protocols = kwargs.get('protocols', None)
        self.api_version_set = kwargs.get('api_version_set', None)
        self.value = kwargs.get('value', None)
        self.format = kwargs.get('format', None)
        self.wsdl_selector = kwargs.get('wsdl_selector', None)
        self.soap_api_type = kwargs.get('soap_api_type', None)
