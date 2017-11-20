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

from .answer import Answer


class SpellCheck(Answer):
    """SpellCheck.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param _type: Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :param flagged_tokens:
    :type flagged_tokens:
     list[~azure.cognitiveservices.language.spellcheck.models.SpellingFlaggedToken]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'flagged_tokens': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'flagged_tokens': {'key': 'flaggedTokens', 'type': '[SpellingFlaggedToken]'},
    }

    def __init__(self, flagged_tokens):
        super(SpellCheck, self).__init__()
        self.flagged_tokens = flagged_tokens
        self._type = 'SpellCheck'
