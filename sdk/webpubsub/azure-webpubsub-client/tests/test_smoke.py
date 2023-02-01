# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testcase import WebpubsubClientTest, WebpubsubClientPowerShellPreparer


class TestWebpubsubClientSmoke(WebpubsubClientTest):
    # @pytest.mark.live_test_only
    @WebpubsubClientPowerShellPreparer()
    @recorded_by_proxy
    def test_start_stop(self, webpubsubclient_connection_string):
        client = self.create_client(connection_string=webpubsubclient_connection_string)
        client.start()
        client.stop()

    # @pytest.mark.live_test_only
    @WebpubsubClientPowerShellPreparer()
    @recorded_by_proxy
    def test_duplicated_start(self, webpubsubclient_connection_string):
        client = self.create_client(connection_string=webpubsubclient_connection_string)
        client.start()
        with pytest.raises(Exception):
            client.start()
        client.stop()
