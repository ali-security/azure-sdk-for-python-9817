# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServicePlacementPolicyDescription(Model):
    """Describes the policy to be used for placement of a Service Fabric service.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ServicePlacementInvalidDomainPolicyDescription,
    ServicePlacementNonPartiallyPlaceServicePolicyDescription,
    ServicePlacementPreferPrimaryDomainPolicyDescription,
    ServicePlacementRequiredDomainPolicyDescription,
    ServicePlacementRequireDomainDistributionPolicyDescription

    :param type: Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'Type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'InvalidDomain': 'ServicePlacementInvalidDomainPolicyDescription', 'NonPartiallyPlaceService': 'ServicePlacementNonPartiallyPlaceServicePolicyDescription', 'PreferPrimaryDomain': 'ServicePlacementPreferPrimaryDomainPolicyDescription', 'RequireDomain': 'ServicePlacementRequiredDomainPolicyDescription', 'RequireDomainDistribution': 'ServicePlacementRequireDomainDistributionPolicyDescription'}
    }

    def __init__(self):
        super(ServicePlacementPolicyDescription, self).__init__()
        self.type = None
