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


class DetectedLanguage(Model):
    """DetectedLanguage.

    :param name: Long name of a detected language (e.g. English, French).
    :type name: str
    :param iso6391_name: A two letter representation of the detected language
     according to the ISO 639-1 standard (e.g. en, fr).
    :type iso6391_name: str
    :param score: A confidence score between 0 and 1. Scores close to 1
     indicate 100% certainty that the identified language is true.
    :type score: float
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'iso6391_name': {'key': 'iso6391Name', 'type': 'str'},
        'score': {'key': 'score', 'type': 'float'},
    }

    def __init__(self, name=None, iso6391_name=None, score=None):
        super(DetectedLanguage, self).__init__()
        self.name = name
        self.iso6391_name = iso6391_name
        self.score = score
