# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class ApplicationGatewaySslCertificate(SubResource):
    """
    SSL certificates of application gateway

    :param str id: Resource Id
    :param str data: Gets or sets the certificate data
    :param str password: Gets or sets the certificate password
    :param str public_cert_data: Gets or sets the certificate public data
    :param str provisioning_state: Gets or sets Provisioning state of the ssl
     certificate resource Updating/Deleting/Failed
    :param str name: Gets name of the resource that is unique within a
     resource group. This name can be used to access the resource
    :param str etag: A unique read-only string that changes whenever the
     resource is updated
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'data': {'key': 'properties.data', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'public_cert_data': {'key': 'properties.publicCertData', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, data=None, password=None, public_cert_data=None, provisioning_state=None, name=None, etag=None, **kwargs):
        super(ApplicationGatewaySslCertificate, self).__init__(id=id, **kwargs)
        self.data = data
        self.password = password
        self.public_cert_data = public_cert_data
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
