# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._relay_api_enums import *


class AccessKeys(msrest.serialization.Model):
    """Namespace/Relay Connection String.

    :param primary_connection_string: Primary connection string of the created namespace
     authorization rule.
    :type primary_connection_string: str
    :param secondary_connection_string: Secondary connection string of the created namespace
     authorization rule.
    :type secondary_connection_string: str
    :param primary_key: A base64-encoded 256-bit primary key for signing and validating the SAS
     token.
    :type primary_key: str
    :param secondary_key: A base64-encoded 256-bit secondary key for signing and validating the SAS
     token.
    :type secondary_key: str
    :param key_name: A string that describes the authorization rule.
    :type key_name: str
    """

    _attribute_map = {
        'primary_connection_string': {'key': 'primaryConnectionString', 'type': 'str'},
        'secondary_connection_string': {'key': 'secondaryConnectionString', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        primary_connection_string: Optional[str] = None,
        secondary_connection_string: Optional[str] = None,
        primary_key: Optional[str] = None,
        secondary_key: Optional[str] = None,
        key_name: Optional[str] = None,
        **kwargs
    ):
        super(AccessKeys, self).__init__(**kwargs)
        self.primary_connection_string = primary_connection_string
        self.secondary_connection_string = secondary_connection_string
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.key_name = key_name


class Resource(msrest.serialization.Model):
    """The resource definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AuthorizationRule(Resource):
    """Description of a namespace authorization rule.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param rights: Required. The rights associated with the rule.
    :type rights: list[str or ~azure.mgmt.relay.models.AccessRights]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'rights': {'required': True, 'unique': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'rights': {'key': 'properties.rights', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        rights: List[Union[str, "AccessRights"]],
        **kwargs
    ):
        super(AuthorizationRule, self).__init__(**kwargs)
        self.rights = rights


class AuthorizationRuleListResult(msrest.serialization.Model):
    """The response from the list namespace operation.

    :param value: Result of the list authorization rules operation.
    :type value: list[~azure.mgmt.relay.models.AuthorizationRule]
    :param next_link: Link to the next set of results. Not empty if value contains incomplete list
     of authorization rules.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[AuthorizationRule]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["AuthorizationRule"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(AuthorizationRuleListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class CheckNameAvailability(msrest.serialization.Model):
    """Description of the check name availability request properties.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The namespace name to check for availability. The namespace name can
     contain only letters, numbers, and hyphens. The namespace must start with a letter, and it must
     end with a letter or number.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        super(CheckNameAvailability, self).__init__(**kwargs)
        self.name = name


class CheckNameAvailabilityResult(msrest.serialization.Model):
    """Description of the check name availability request properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar message: The detailed info regarding the reason associated with the namespace.
    :vartype message: str
    :param name_available: Value indicating namespace is available. Returns true if the namespace
     is available; otherwise, false.
    :type name_available: bool
    :param reason: The reason for unavailability of a namespace. Possible values include: "None",
     "InvalidName", "SubscriptionIsDisabled", "NameInUse", "NameInLockdown",
     "TooManyNamespaceInCurrentSubscription".
    :type reason: str or ~azure.mgmt.relay.models.UnavailableReason
    """

    _validation = {
        'message': {'readonly': True},
    }

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name_available: Optional[bool] = None,
        reason: Optional[Union[str, "UnavailableReason"]] = None,
        **kwargs
    ):
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.message = None
        self.name_available = name_available
        self.reason = reason


class ErrorResponse(msrest.serialization.Model):
    """Error reponse indicates Relay service is not able to process the incoming request. The reason is provided in the error message.

    :param code: Error code.
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class HybridConnection(Resource):
    """Description of hybrid connection resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar created_at: The time the hybrid connection was created.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: The time the namespace was updated.
    :vartype updated_at: ~datetime.datetime
    :ivar listener_count: The number of listeners for this hybrid connection. Note that min : 1 and
     max:25 are supported.
    :vartype listener_count: int
    :param requires_client_authorization: Returns true if client authorization is needed for this
     hybrid connection; otherwise, false.
    :type requires_client_authorization: bool
    :param user_metadata: The usermetadata is a placeholder to store user-defined string data for
     the hybrid connection endpoint. For example, it can be used to store descriptive data, such as
     a list of teams and their contact information. Also, user-defined configuration settings can be
     stored.
    :type user_metadata: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
        'listener_count': {'readonly': True, 'maximum': 25, 'minimum': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'listener_count': {'key': 'properties.listenerCount', 'type': 'int'},
        'requires_client_authorization': {'key': 'properties.requiresClientAuthorization', 'type': 'bool'},
        'user_metadata': {'key': 'properties.userMetadata', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        requires_client_authorization: Optional[bool] = None,
        user_metadata: Optional[str] = None,
        **kwargs
    ):
        super(HybridConnection, self).__init__(**kwargs)
        self.created_at = None
        self.updated_at = None
        self.listener_count = None
        self.requires_client_authorization = requires_client_authorization
        self.user_metadata = user_metadata


class HybridConnectionListResult(msrest.serialization.Model):
    """The response of the list hybrid connection operation.

    :param value: Result of the list hybrid connections.
    :type value: list[~azure.mgmt.relay.models.HybridConnection]
    :param next_link: Link to the next set of results. Not empty if value contains incomplete list
     hybrid connection operation.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[HybridConnection]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["HybridConnection"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(HybridConnectionListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class Operation(msrest.serialization.Model):
    """A Relay REST API operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Operation name: {provider}/{resource}/{operation}.
    :vartype name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.relay.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: Service provider: Relay.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed: Invoice, etc.
    :vartype resource: str
    :ivar operation: Operation type: Read, write, delete, etc.
    :vartype operation: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Relay operations. It contains a list of operations and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of Relay operations supported by resource provider.
    :vartype value: list[~azure.mgmt.relay.models.Operation]
    :ivar next_link: URL to get the next set of operation list results if there are any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class RegenerateAccessKeyParameters(msrest.serialization.Model):
    """Parameters supplied to the regenerate authorization rule operation, specifies which key neeeds to be reset.

    All required parameters must be populated in order to send to Azure.

    :param key_type: Required. The access key to regenerate. Possible values include: "PrimaryKey",
     "SecondaryKey".
    :type key_type: str or ~azure.mgmt.relay.models.KeyType
    :param key: Optional. If the key value is provided, this is set to key type, or autogenerated
     key value set for key type.
    :type key: str
    """

    _validation = {
        'key_type': {'required': True},
    }

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        key_type: Union[str, "KeyType"],
        key: Optional[str] = None,
        **kwargs
    ):
        super(RegenerateAccessKeyParameters, self).__init__(**kwargs)
        self.key_type = key_type
        self.key = key


class TrackedResource(Resource):
    """Definition of resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.location = location
        self.tags = tags


class RelayNamespace(TrackedResource):
    """Description of a namespace resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param sku: SKU of the namespace.
    :type sku: ~azure.mgmt.relay.models.Sku
    :ivar provisioning_state:  Possible values include: "Created", "Succeeded", "Deleted",
     "Failed", "Updating", "Unknown".
    :vartype provisioning_state: str or ~azure.mgmt.relay.models.ProvisioningStateEnum
    :ivar created_at: The time the namespace was created.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: The time the namespace was updated.
    :vartype updated_at: ~datetime.datetime
    :ivar service_bus_endpoint: Endpoint you can use to perform Service Bus operations.
    :vartype service_bus_endpoint: str
    :ivar metric_id: Identifier for Azure Insights metrics.
    :vartype metric_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
        'service_bus_endpoint': {'readonly': True},
        'metric_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'service_bus_endpoint': {'key': 'properties.serviceBusEndpoint', 'type': 'str'},
        'metric_id': {'key': 'properties.metricId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["Sku"] = None,
        **kwargs
    ):
        super(RelayNamespace, self).__init__(location=location, tags=tags, **kwargs)
        self.sku = sku
        self.provisioning_state = None
        self.created_at = None
        self.updated_at = None
        self.service_bus_endpoint = None
        self.metric_id = None


class RelayNamespaceListResult(msrest.serialization.Model):
    """The response from the list namespace operation.

    :param value: Result of the list namespace operation.
    :type value: list[~azure.mgmt.relay.models.RelayNamespace]
    :param next_link: Link to the next set of results. Not empty if value contains incomplete list
     of namespaces.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[RelayNamespace]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["RelayNamespace"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(RelayNamespaceListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ResourceNamespacePatch(Resource):
    """Definition of resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(ResourceNamespacePatch, self).__init__(**kwargs)
        self.tags = tags


class RelayUpdateParameters(ResourceNamespacePatch):
    """Description of a namespace resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param sku: SKU of the namespace.
    :type sku: ~azure.mgmt.relay.models.Sku
    :ivar provisioning_state:  Possible values include: "Created", "Succeeded", "Deleted",
     "Failed", "Updating", "Unknown".
    :vartype provisioning_state: str or ~azure.mgmt.relay.models.ProvisioningStateEnum
    :ivar created_at: The time the namespace was created.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: The time the namespace was updated.
    :vartype updated_at: ~datetime.datetime
    :ivar service_bus_endpoint: Endpoint you can use to perform Service Bus operations.
    :vartype service_bus_endpoint: str
    :ivar metric_id: Identifier for Azure Insights metrics.
    :vartype metric_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
        'service_bus_endpoint': {'readonly': True},
        'metric_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'service_bus_endpoint': {'key': 'properties.serviceBusEndpoint', 'type': 'str'},
        'metric_id': {'key': 'properties.metricId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["Sku"] = None,
        **kwargs
    ):
        super(RelayUpdateParameters, self).__init__(tags=tags, **kwargs)
        self.sku = sku
        self.provisioning_state = None
        self.created_at = None
        self.updated_at = None
        self.service_bus_endpoint = None
        self.metric_id = None


class Sku(msrest.serialization.Model):
    """SKU of the namespace.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Name of this SKU. Has constant value: "Standard".
    :vartype name: str
    :param tier: The tier of this SKU. The only acceptable values to pass in are None and
     "Standard". The default value is None.
    :type tier: str
    """

    _validation = {
        'name': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    name = "Standard"

    def __init__(
        self,
        *,
        tier: Optional[str] = None,
        **kwargs
    ):
        super(Sku, self).__init__(**kwargs)
        self.tier = tier


class WcfRelay(Resource):
    """Description of the WCF relay resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar is_dynamic: Returns true if the relay is dynamic; otherwise, false.
    :vartype is_dynamic: bool
    :ivar created_at: The time the WCF relay was created.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: The time the namespace was updated.
    :vartype updated_at: ~datetime.datetime
    :ivar listener_count: The number of listeners for this relay. Note that min :1 and max:25 are
     supported.
    :vartype listener_count: int
    :param relay_type: WCF relay type. Possible values include: "NetTcp", "Http".
    :type relay_type: str or ~azure.mgmt.relay.models.Relaytype
    :param requires_client_authorization: Returns true if client authorization is needed for this
     relay; otherwise, false.
    :type requires_client_authorization: bool
    :param requires_transport_security: Returns true if transport security is needed for this
     relay; otherwise, false.
    :type requires_transport_security: bool
    :param user_metadata: The usermetadata is a placeholder to store user-defined string data for
     the WCF Relay endpoint. For example, it can be used to store descriptive data, such as list of
     teams and their contact information. Also, user-defined configuration settings can be stored.
    :type user_metadata: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'is_dynamic': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
        'listener_count': {'readonly': True, 'maximum': 25, 'minimum': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'is_dynamic': {'key': 'properties.isDynamic', 'type': 'bool'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'listener_count': {'key': 'properties.listenerCount', 'type': 'int'},
        'relay_type': {'key': 'properties.relayType', 'type': 'str'},
        'requires_client_authorization': {'key': 'properties.requiresClientAuthorization', 'type': 'bool'},
        'requires_transport_security': {'key': 'properties.requiresTransportSecurity', 'type': 'bool'},
        'user_metadata': {'key': 'properties.userMetadata', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        relay_type: Optional[Union[str, "Relaytype"]] = None,
        requires_client_authorization: Optional[bool] = None,
        requires_transport_security: Optional[bool] = None,
        user_metadata: Optional[str] = None,
        **kwargs
    ):
        super(WcfRelay, self).__init__(**kwargs)
        self.is_dynamic = None
        self.created_at = None
        self.updated_at = None
        self.listener_count = None
        self.relay_type = relay_type
        self.requires_client_authorization = requires_client_authorization
        self.requires_transport_security = requires_transport_security
        self.user_metadata = user_metadata


class WcfRelaysListResult(msrest.serialization.Model):
    """The response of the list WCF relay operation.

    :param value: Result of the list WCF relay operation.
    :type value: list[~azure.mgmt.relay.models.WcfRelay]
    :param next_link: Link to the next set of results. Not empty if value contains incomplete list
     of WCF relays.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[WcfRelay]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["WcfRelay"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(WcfRelaysListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
