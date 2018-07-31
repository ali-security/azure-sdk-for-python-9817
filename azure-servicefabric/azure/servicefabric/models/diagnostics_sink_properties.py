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


class DiagnosticsSinkProperties(Model):
    """Properties of a DiagnosticsSink.

    All required parameters must be populated in order to send to Azure.

    :param name: Name of the sink. This value is referenced by
     DiagnosticsReferenceDescription
    :type name: str
    :param description: A description of the sink.
    :type description: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DiagnosticsSinkProperties, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.kind = None
