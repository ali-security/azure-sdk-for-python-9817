# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from azure.appconfiguration.provider import SettingSelector
from devtools_testutils import recorded_by_proxy
from preparers import app_config_decorator
from testcase import AppConfigTestCase


class TestAppConfigurationProvider(AppConfigTestCase):
    # method: provider_creation
    @recorded_by_proxy
    @app_config_decorator
    def test_provider_creation(self, appconfiguration_connection_string, appconfiguration_keyvault_secret_url):
        client = self.create_client(
            appconfiguration_connection_string, keyvault_secret_url=appconfiguration_keyvault_secret_url
        )
        assert client["message"] == "hi"
        assert client["my_json"]["key"] == "value"
        assert "FeatureManagementFeatureFlags" in client
        assert "Alpha" in client["FeatureManagementFeatureFlags"]

    # method: provider_trim_prefixes
    @recorded_by_proxy
    @app_config_decorator
    def test_provider_trim_prefixes(self, appconfiguration_connection_string, appconfiguration_keyvault_secret_url):
        trimmed = {"test."}
        client = self.create_client(
            appconfiguration_connection_string,
            trim_prefixes=trimmed,
            keyvault_secret_url=appconfiguration_keyvault_secret_url,
        )
        assert client["message"] == "hi"
        assert client["my_json"]["key"] == "value"
        assert client["trimmed"] == "key"
        assert "test.trimmed" not in client
        assert "FeatureManagementFeatureFlags" in client
        assert "Alpha" in client["FeatureManagementFeatureFlags"]

    # method: provider_selectors
    @recorded_by_proxy
    @app_config_decorator
    def test_provider_selectors(self, appconfiguration_connection_string, appconfiguration_keyvault_secret_url):
        selects = {SettingSelector(key_filter="message*", label_filter="dev")}
        client = self.create_client(
            appconfiguration_connection_string,
            selects=selects,
            keyvault_secret_url=appconfiguration_keyvault_secret_url,
        )
        assert client["message"] == "test"
        assert "test.trimmed" not in client
        assert "FeatureManagementFeatureFlags" not in client

    # method: provider_selectors
    @recorded_by_proxy
    @app_config_decorator
    def test_provider_key_vault_reference(
        self, appconfiguration_connection_string, appconfiguration_keyvault_secret_url
    ):
        selects = {SettingSelector(key_filter="*", label_filter="prod")}
        client = self.create_client(
            appconfiguration_connection_string,
            selects=selects,
            keyvault_secret_url=appconfiguration_keyvault_secret_url,
        )
        assert client["secret"] == "Very secret value"

    # method: provider_selectors
    @recorded_by_proxy
    @app_config_decorator
    def test_provider_secret_resolver(self, appconfiguration_connection_string):
        selects = {SettingSelector(key_filter="*", label_filter="prod")}
        client = self.create_client(
            appconfiguration_connection_string, selects=selects, secret_resolver=secret_resolver
        )
        assert client["secret"] == "Reslover Value"


def secret_resolver(secret_id):
    return "Reslover Value"
