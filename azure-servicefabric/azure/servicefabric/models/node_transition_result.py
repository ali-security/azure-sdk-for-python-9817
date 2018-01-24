# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NodeTransitionResult(Model):
    """Represents information about an operation in a terminal state (Completed or
    Faulted).

    :param error_code: If OperationState is Completed, this is 0.  If
     OperationState is Faulted, this is an error code indicating the reason.
    :type error_code: int
    :param node_result: Contains information about a node that was targeted by
     a user-induced operation.
    :type node_result: ~servicefabric.models.NodeResult
    """

    _attribute_map = {
        'error_code': {'key': 'ErrorCode', 'type': 'int'},
        'node_result': {'key': 'NodeResult', 'type': 'NodeResult'},
    }

    def __init__(self, error_code=None, node_result=None):
        super(NodeTransitionResult, self).__init__()
        self.error_code = error_code
        self.node_result = node_result
