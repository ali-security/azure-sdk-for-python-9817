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


class LiveEventActionInput(Model):
    """The LiveEvent action input parameter definition.

    :param remove_outputs_on_stop: The flag indicates if remove LiveOutputs on
     Stop.
    :type remove_outputs_on_stop: bool
    """

    _attribute_map = {
        'remove_outputs_on_stop': {'key': 'removeOutputsOnStop', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(LiveEventActionInput, self).__init__(**kwargs)
        self.remove_outputs_on_stop = kwargs.get('remove_outputs_on_stop', None)
