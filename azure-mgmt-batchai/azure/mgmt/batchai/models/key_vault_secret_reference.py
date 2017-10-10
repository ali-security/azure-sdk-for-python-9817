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


class KeyVaultSecretReference(Model):
    """Describes a reference to Key Vault Secret.

    :param source_vault: Fully qualified resource Id for the Key Vault.
    :type source_vault: :class:`ResourceId
     <azure.mgmt.batchai.models.ResourceId>`
    :param secret_url: The URL referencing a secret in a Key Vault.
    :type secret_url: str
    """

    _validation = {
        'source_vault': {'required': True},
        'secret_url': {'required': True},
    }

    _attribute_map = {
        'source_vault': {'key': 'sourceVault', 'type': 'ResourceId'},
        'secret_url': {'key': 'secretUrl', 'type': 'str'},
    }

    def __init__(self, source_vault, secret_url):
        self.source_vault = source_vault
        self.secret_url = secret_url
