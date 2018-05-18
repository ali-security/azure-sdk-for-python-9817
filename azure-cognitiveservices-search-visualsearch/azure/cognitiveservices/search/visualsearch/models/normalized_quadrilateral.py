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

from .structured_value import StructuredValue


class NormalizedQuadrilateral(StructuredValue):
    """Defines a region of an image. The region is a convex quadrilateral defined
    by coordinates of its top left, top right, bottom left, and bottom right
    points. The coordinates are fractional values of the original image's width
    and height in the range 0.0 through 1.0.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource. To use the URL,
     append query parameters as appropriate and include the
     Ocp-Apim-Subscription-Key header.
    :vartype read_link: str
    :ivar web_search_url: The URL to Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image:
     ~azure.cognitiveservices.search.visualsearch.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :param top_left: Required. The top left corner coordinate.
    :type top_left:
     ~azure.cognitiveservices.search.visualsearch.models.Point2D
    :param top_right: Required. The top right corner coordinate.
    :type top_right:
     ~azure.cognitiveservices.search.visualsearch.models.Point2D
    :param bottom_right: Required. The bottom right corner coordinate.
    :type bottom_right:
     ~azure.cognitiveservices.search.visualsearch.models.Point2D
    :param bottom_left: Required. The bottom left corner coordinate.
    :type bottom_left:
     ~azure.cognitiveservices.search.visualsearch.models.Point2D
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'top_left': {'required': True},
        'top_right': {'required': True},
        'bottom_right': {'required': True},
        'bottom_left': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'top_left': {'key': 'topLeft', 'type': 'Point2D'},
        'top_right': {'key': 'topRight', 'type': 'Point2D'},
        'bottom_right': {'key': 'bottomRight', 'type': 'Point2D'},
        'bottom_left': {'key': 'bottomLeft', 'type': 'Point2D'},
    }

    def __init__(self, **kwargs):
        super(NormalizedQuadrilateral, self).__init__(**kwargs)
        self.top_left = kwargs.get('top_left', None)
        self.top_right = kwargs.get('top_right', None)
        self.bottom_right = kwargs.get('bottom_right', None)
        self.bottom_left = kwargs.get('bottom_left', None)
        self._type = 'NormalizedQuadrilateral'
