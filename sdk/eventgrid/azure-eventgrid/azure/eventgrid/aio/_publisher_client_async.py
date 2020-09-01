# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from .._models import CloudEvent, EventGridEvent, CustomEvent
from .._helpers import _get_topic_hostname_only_fqdn, _get_authentication_policy, _is_cloud_event
from azure.core.pipeline.policies import AzureKeyCredentialPolicy
from azure.core.credentials import AzureKeyCredential
from .._generated.aio import EventGridPublisherClient as EventGridPublisherClientAsync
from .. import _constants as constants

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Union, Dict, List
    SendType = Union[
        CloudEvent,
        EventGridEvent,
        CustomEvent,
        Dict,
        List[CloudEvent],
        List[EventGridEvent],
        List[CustomEvent],
        List[Dict]
    ]

class EventGridPublisherClient(object):
    """Asynchronous EventGrid Python Publisher Client.

    :param str topic_hostname: The topic endpoint to send the events to.
    :param credential: The credential object used for authentication which implements SAS key authentication or SAS token authentication.
    :type credential: Union[~azure.core.credentials.AzureKeyCredential, azure.eventgrid.EventGridSharedAccessSignatureCredential]
    """

    def __init__(self, topic_hostname, credential, **kwargs):
        # type: (str, Union[AzureKeyCredential, EventGridSharedAccessSignatureCredential], Any) -> None
        auth_policy = _get_authentication_policy(credential)
        self._client = EventGridPublisherClientAsync(authentication_policy=auth_policy, **kwargs)
        topic_hostname = _get_topic_hostname_only_fqdn(topic_hostname)
        self._topic_hostname = topic_hostname


    async def send(self, events, **kwargs):
        # type: (SendType) -> None
        """Sends event data to topic hostname specified during client initialization.

        :param  events: A list or an instance of CloudEvent/EventGridEvent/CustomEvent to be sent.
        :type events: SendType
        :keyword str content_type: The type of content to be used to send the events.
        Has default value "application/json; charset=utf-8" for EventGridEvents, with "cloudevents-batch+json" for CloudEvents
        :rtype: None
        :raises: :class:`ValueError`, when events do not follow specified SendType.
         """
        if not isinstance(events, list):
            events = [events]

        if all(isinstance(e, CloudEvent) for e in events) or all(_is_cloud_event(e) for e in events):
            kwargs.setdefault("content_type", "application/cloudevents-batch+json; charset=utf-8")
            await self._client.publish_cloud_event_events(self._topic_hostname, events, **kwargs)
        elif all(isinstance(e, EventGridEvent) for e in events) or all(isinstance(e, dict) for e in events):
            kwargs.setdefault("content_type", "application/json; charset=utf-8")
            await self._client.publish_events(self._topic_hostname, events, **kwargs)
        elif all(isinstance(e, CustomEvent) for e in events):
            serialized_events = [dict(e) for e in events]
            await self._client.publish_custom_event_events(self._topic_hostname, serialized_events, **kwargs)
        else:
            raise ValueError("Event schema is not correct.")
    
