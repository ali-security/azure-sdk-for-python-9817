# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os
import platform

import pytest

from devtools_testutils import (
    add_general_regex_sanitizer,
    add_header_regex_sanitizer,
    add_oauth_response_sanitizer,
    add_uri_string_sanitizer,
    test_proxy,
    remove_batch_sanitizers,
)

# Ignore async tests for PyPy
collect_ignore_glob = []
if platform.python_implementation() == "PyPy":
    collect_ignore_glob.append("tests/*_async.py")

@pytest.fixture(scope="session", autouse=True)
def add_sanitizers(test_proxy):
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", "00000000-0000-0000-0000-000000000000")
    tenant_id = os.environ.get("STORAGE_TENANT_ID", "00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=subscription_id, value="00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=tenant_id, value="00000000-0000-0000-0000-000000000000")
    add_header_regex_sanitizer(key="Set-Cookie", value="[set-cookie;]")
    add_header_regex_sanitizer(key="Cookie", value="cookie;")
    add_oauth_response_sanitizer()

    add_header_regex_sanitizer(key="x-ms-copy-source-authorization", value="Sanitized")
    add_header_regex_sanitizer(key="x-ms-encryption-key", value="Sanitized")

    add_uri_string_sanitizer(target=".preprod.", value=".")

    # Remove the following sanitizers since certain fields are needed in tests and are non-sensitive:
    #  - AZSDK3493: $..name
    remove_batch_sanitizers(["AZSDK3493"])
