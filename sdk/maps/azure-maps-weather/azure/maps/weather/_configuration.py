# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline import policies

VERSION = "unknown"


class MapsWeatherClientConfiguration:  # pylint: disable=too-many-instance-attributes,name-too-long
    """Configuration for MapsWeatherClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :param client_id: Specifies which account is intended for usage in conjunction with the
     Microsoft Entra ID security model.  It represents a unique ID for the Azure Maps account and
     can be retrieved from the Azure Maps management  plane Account API. To use Microsoft Entra ID
     security in Azure Maps see the following `articles <https://aka.ms/amauthdetails>`_ for
     guidance. Default value is None.
    :type client_id: str
    :keyword api_version: Api Version. Default value is "1.1". Note that overriding this default
     value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, credential: AzureKeyCredential, client_id: Optional[str] = None, **kwargs: Any) -> None:
        api_version: str = kwargs.pop("api_version", "1.1")

        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.credential = credential
        self.client_id = client_id
        self.api_version = api_version
        kwargs.setdefault("sdk_moniker", "maps-weather/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.AzureKeyCredentialPolicy(self.credential, "SAS Token", **kwargs)
