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


class CloningInfo(Model):
    """Represents information needed for cloning operation.

    :param correlation_id: Correlation Id of cloning operation. This id ties
     multiple cloning operations
     together to use the same snapshot
    :type correlation_id: str
    :param overwrite: Overwrite destination web app
    :type overwrite: bool
    :param clone_custom_host_names: If true, clone custom hostnames from
     source web app
    :type clone_custom_host_names: bool
    :param clone_source_control: Clone source control from source web app
    :type clone_source_control: bool
    :param source_web_app_id: ARM resource id of the source web app. Web app
     resource id is of the form
     /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}
     for production slots and
     /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName}
     for other slots
    :type source_web_app_id: str
    :param hosting_environment: Hosting environment
    :type hosting_environment: str
    :param app_settings_overrides: Application settings overrides for cloned
     web app. If specified these settings will override the settings cloned
     from source web app. If not specified, application settings
     from source web app are retained.
    :type app_settings_overrides: dict
    :param configure_load_balancing: If specified configure load balancing
     for source and clone site
    :type configure_load_balancing: bool
    :param traffic_manager_profile_id: ARM resource id of the traffic manager
     profile to use if it exists. Traffic manager resource id is of the form
     /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{profileName}
    :type traffic_manager_profile_id: str
    :param traffic_manager_profile_name: Name of traffic manager profile to
     create. This is only needed if traffic manager profile does not already
     exist
    :type traffic_manager_profile_name: str
    """ 

    _attribute_map = {
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'overwrite': {'key': 'overwrite', 'type': 'bool'},
        'clone_custom_host_names': {'key': 'cloneCustomHostNames', 'type': 'bool'},
        'clone_source_control': {'key': 'cloneSourceControl', 'type': 'bool'},
        'source_web_app_id': {'key': 'sourceWebAppId', 'type': 'str'},
        'hosting_environment': {'key': 'hostingEnvironment', 'type': 'str'},
        'app_settings_overrides': {'key': 'appSettingsOverrides', 'type': '{str}'},
        'configure_load_balancing': {'key': 'configureLoadBalancing', 'type': 'bool'},
        'traffic_manager_profile_id': {'key': 'trafficManagerProfileId', 'type': 'str'},
        'traffic_manager_profile_name': {'key': 'trafficManagerProfileName', 'type': 'str'},
    }

    def __init__(self, correlation_id=None, overwrite=None, clone_custom_host_names=None, clone_source_control=None, source_web_app_id=None, hosting_environment=None, app_settings_overrides=None, configure_load_balancing=None, traffic_manager_profile_id=None, traffic_manager_profile_name=None):
        self.correlation_id = correlation_id
        self.overwrite = overwrite
        self.clone_custom_host_names = clone_custom_host_names
        self.clone_source_control = clone_source_control
        self.source_web_app_id = source_web_app_id
        self.hosting_environment = hosting_environment
        self.app_settings_overrides = app_settings_overrides
        self.configure_load_balancing = configure_load_balancing
        self.traffic_manager_profile_id = traffic_manager_profile_id
        self.traffic_manager_profile_name = traffic_manager_profile_name
