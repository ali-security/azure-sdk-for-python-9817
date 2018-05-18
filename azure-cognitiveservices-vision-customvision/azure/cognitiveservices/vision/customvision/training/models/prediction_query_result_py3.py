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


class PredictionQueryResult(Model):
    """PredictionQueryResult.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar token:
    :vartype token:
     ~azure.cognitiveservices.vision.customvision.training.models.PredictionQueryToken
    :ivar results:
    :vartype results:
     list[~azure.cognitiveservices.vision.customvision.training.models.StoredImagePrediction]
    """

    _validation = {
        'token': {'readonly': True},
        'results': {'readonly': True},
    }

    _attribute_map = {
        'token': {'key': 'token', 'type': 'PredictionQueryToken'},
        'results': {'key': 'results', 'type': '[StoredImagePrediction]'},
    }

    def __init__(self, **kwargs) -> None:
        super(PredictionQueryResult, self).__init__(**kwargs)
        self.token = None
        self.results = None
