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

from msrest.serialization import Model


class CatalogItem(Model):
    """
    A Data Lake Analytics catalog item.

    :param compute_account_name: Gets or sets the name of the Data Lake
     Analytics account.
    :type compute_account_name: str
    :param version: Gets or sets the version of the catalog item.
    :type version: str
    """ 

    _attribute_map = {
        'compute_account_name': {'key': 'computeAccountName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, compute_account_name=None, version=None):
        self.compute_account_name = compute_account_name
        self.version = version
