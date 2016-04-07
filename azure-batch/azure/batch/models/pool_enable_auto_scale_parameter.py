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


class PoolEnableAutoScaleParameter(Model):
    """
    Parameters for a CloudPoolOperations.EnableAutoScale request.

    :param auto_scale_formula: Sets the formula for the desired number of
     compute nodes in the pool.
    :type auto_scale_formula: str
    :param auto_scale_evaluation_interval: Gets or sets a time interval for
     the desired autoscale evaluation period in the pool.
    :type auto_scale_evaluation_interval: timedelta
    """ 

    _attribute_map = {
        'auto_scale_formula': {'key': 'autoScaleFormula', 'type': 'str'},
        'auto_scale_evaluation_interval': {'key': 'autoScaleEvaluationInterval', 'type': 'duration'},
    }

    def __init__(self, auto_scale_formula=None, auto_scale_evaluation_interval=None):
        self.auto_scale_formula = auto_scale_formula
        self.auto_scale_evaluation_interval = auto_scale_evaluation_interval
