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


class LinuxUserConfiguration(Model):
    """Properties used to create a Linux-specific user on an Azure Batch node.

    :param uid: The user ID of the user account. The uid and gid properties
     must be specified together or not at all. If not specified the underlying
     operating system picks the uid.
    :type uid: int
    :param gid: The group ID for the user account. The uid and gid properties
     must be specified together or not at all. If not specified the underlying
     operating system picks the gid.
    :type gid: int
    :param ssh_private_key: The SSH private key for the user account. The SSH
     private key establishes password-less SSH between nodes in a Linux pool
     when the pool's enableInterNodeCommunication property is true. If not
     specified, password-less SSH is not established between nodes.
    :type ssh_private_key: str
    """

    _attribute_map = {
        'uid': {'key': 'uid', 'type': 'int'},
        'gid': {'key': 'gid', 'type': 'int'},
        'ssh_private_key': {'key': 'sshPrivateKey', 'type': 'str'},
    }

    def __init__(self, uid=None, gid=None, ssh_private_key=None):
        self.uid = uid
        self.gid = gid
        self.ssh_private_key = ssh_private_key
