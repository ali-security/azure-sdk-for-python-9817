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


class ValidateCustomDomainOutput(Model):
    """Output of custom domain validation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar custom_domain_validated: Indicates whether the custom domain is
     valid or not.
    :vartype custom_domain_validated: bool
    :ivar reason: The reason why the custom domain is not valid.
    :vartype reason: str
    :ivar message: Error message describing why the custom domain is not
     valid.
    :vartype message: str
    """

    _validation = {
        'custom_domain_validated': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'custom_domain_validated': {'key': 'customDomainValidated', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self):
        super(ValidateCustomDomainOutput, self).__init__()
        self.custom_domain_validated = None
        self.reason = None
        self.message = None
