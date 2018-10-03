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

    All required parameters must be populated in order to send to Azure.

    :param secret_url: Required. The URL referencing a secret in a Key Vault.
    :type secret_url: str
    :param source_vault: Required. The relative URL of the Key Vault
     containing the secret.
    :type source_vault: ~azure.mgmt.compute.v2018_10_01.models.SubResource
    """

    _validation = {
        'secret_url': {'required': True},
        'source_vault': {'required': True},
    }

    _attribute_map = {
        'secret_url': {'key': 'secretUrl', 'type': 'str'},
        'source_vault': {'key': 'sourceVault', 'type': 'SubResource'},
    }

    def __init__(self, *, secret_url: str, source_vault, **kwargs) -> None:
        super(KeyVaultSecretReference, self).__init__(**kwargs)
        self.secret_url = secret_url
        self.source_vault = source_vault
