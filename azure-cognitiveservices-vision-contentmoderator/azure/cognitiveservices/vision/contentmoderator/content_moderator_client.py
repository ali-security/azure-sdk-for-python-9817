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

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.image_moderation_operations import ImageModerationOperations
from .operations.text_moderation_operations import TextModerationOperations
from .operations.list_management_image_lists_operations import ListManagementImageListsOperations
from .operations.list_management_term_lists_operations import ListManagementTermListsOperations
from .operations.list_management_image_operations import ListManagementImageOperations
from .operations.list_management_term_operations import ListManagementTermOperations
from .operations.reviews_operations import ReviewsOperations
from . import models


class ContentModeratorClientConfiguration(Configuration):
    """Configuration for ContentModeratorClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param ocp_apim_subscription_key: The subscription key in header
    :type ocp_apim_subscription_key: str
    :param base_url: Supported Azure regions for Content Moderator endpoints.
     Possible values include: 'westus.api.cognitive.microsoft.com',
     'westus2.api.cognitive.microsoft.com',
     'eastus.api.cognitive.microsoft.com',
     'eastus2.api.cognitive.microsoft.com',
     'westcentralus.api.cognitive.microsoft.com',
     'southcentralus.api.cognitive.microsoft.com',
     'westeurope.api.cognitive.microsoft.com',
     'northeurope.api.cognitive.microsoft.com',
     'southeastasia.api.cognitive.microsoft.com',
     'eastasia.api.cognitive.microsoft.com',
     'australiaeast.api.cognitive.microsoft.com',
     'brazilsouth.api.cognitive.microsoft.com',
     'contentmoderatortest.azure-api.net'
    :type base_url: str or
     ~azure.cognitiveservices.vision.contentmoderator.models.AzureRegionBaseUrl
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, ocp_apim_subscription_key, base_url, credentials):

        if ocp_apim_subscription_key is None:
            raise ValueError("Parameter 'ocp_apim_subscription_key' must not be None.")
        if base_url is None:
            raise ValueError("Parameter 'base_url' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = 'https://{baseUrl}'

        super(ContentModeratorClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-vision-contentmoderator/{}'.format(VERSION))

        self.ocp_apim_subscription_key = ocp_apim_subscription_key
        self.base_url = base_url
        self.credentials = credentials


class ContentModeratorClient(object):
    """You use the API to scan your content as it is generated. Content Moderator then processes your content and sends the results along with relevant information either back to your systems or to the built-in review tool. You can use this information to take decisions e.g. take it down, send to human judge, etc.
    When using the API, images need to have a minimum of 128 pixels and a maximum file size of 4MB.
    Text can be at most 1024 characters long.
    If the content passed to the text API or the image API exceeds the size limits, the API will return an error code that informs about the issue.
    This API is currently available in:
    * West US - westus.api.cognitive.microsoft.com
    * East US 2 - eastus2.api.cognitive.microsoft.com
    * West Central US - westcentralus.api.cognitive.microsoft.com
    * West Europe - westeurope.api.cognitive.microsoft.com
    * Southeast Asia - southeastasia.api.cognitive.microsoft.com .

    :ivar config: Configuration for client.
    :vartype config: ContentModeratorClientConfiguration

    :ivar image_moderation: ImageModeration operations
    :vartype image_moderation: azure.cognitiveservices.vision.contentmoderator.operations.ImageModerationOperations
    :ivar text_moderation: TextModeration operations
    :vartype text_moderation: azure.cognitiveservices.vision.contentmoderator.operations.TextModerationOperations
    :ivar list_management_image_lists: ListManagementImageLists operations
    :vartype list_management_image_lists: azure.cognitiveservices.vision.contentmoderator.operations.ListManagementImageListsOperations
    :ivar list_management_term_lists: ListManagementTermLists operations
    :vartype list_management_term_lists: azure.cognitiveservices.vision.contentmoderator.operations.ListManagementTermListsOperations
    :ivar list_management_image: ListManagementImage operations
    :vartype list_management_image: azure.cognitiveservices.vision.contentmoderator.operations.ListManagementImageOperations
    :ivar list_management_term: ListManagementTerm operations
    :vartype list_management_term: azure.cognitiveservices.vision.contentmoderator.operations.ListManagementTermOperations
    :ivar reviews: Reviews operations
    :vartype reviews: azure.cognitiveservices.vision.contentmoderator.operations.ReviewsOperations

    :param ocp_apim_subscription_key: The subscription key in header
    :type ocp_apim_subscription_key: str
    :param base_url: Supported Azure regions for Content Moderator endpoints.
     Possible values include: 'westus.api.cognitive.microsoft.com',
     'westus2.api.cognitive.microsoft.com',
     'eastus.api.cognitive.microsoft.com',
     'eastus2.api.cognitive.microsoft.com',
     'westcentralus.api.cognitive.microsoft.com',
     'southcentralus.api.cognitive.microsoft.com',
     'westeurope.api.cognitive.microsoft.com',
     'northeurope.api.cognitive.microsoft.com',
     'southeastasia.api.cognitive.microsoft.com',
     'eastasia.api.cognitive.microsoft.com',
     'australiaeast.api.cognitive.microsoft.com',
     'brazilsouth.api.cognitive.microsoft.com',
     'contentmoderatortest.azure-api.net'
    :type base_url: str or
     ~azure.cognitiveservices.vision.contentmoderator.models.AzureRegionBaseUrl
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, ocp_apim_subscription_key, base_url, credentials):

        self.config = ContentModeratorClientConfiguration(ocp_apim_subscription_key, base_url, credentials)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.image_moderation = ImageModerationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.text_moderation = TextModerationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.list_management_image_lists = ListManagementImageListsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.list_management_term_lists = ListManagementTermListsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.list_management_image = ListManagementImageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.list_management_term = ListManagementTermOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.reviews = ReviewsOperations(
            self._client, self.config, self._serialize, self._deserialize)
