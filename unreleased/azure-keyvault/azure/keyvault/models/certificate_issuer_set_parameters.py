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


class CertificateIssuerSetParameters(Model):
    """The certificate issuer set parameters.

    :param provider: The issuer provider.
    :type provider: str
    :param credentials: The credentials to be used for the issuer.
    :type credentials: :class:`IssuerCredentials
     <azure.keyvault.models.IssuerCredentials>`
    :param organization_details: Details of the organization as provided to
     the issuer.
    :type organization_details: :class:`OrganizationDetails
     <azure.keyvault.models.OrganizationDetails>`
    :param attributes: Attributes of the issuer object.
    :type attributes: :class:`IssuerAttributes
     <azure.keyvault.models.IssuerAttributes>`
    """ 

    _validation = {
        'provider': {'required': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'credentials': {'key': 'credentials', 'type': 'IssuerCredentials'},
        'organization_details': {'key': 'org_details', 'type': 'OrganizationDetails'},
        'attributes': {'key': 'attributes', 'type': 'IssuerAttributes'},
    }

    def __init__(self, provider, credentials=None, organization_details=None, attributes=None):
        self.provider = provider
        self.credentials = credentials
        self.organization_details = organization_details
        self.attributes = attributes
