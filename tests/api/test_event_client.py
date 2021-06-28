#
# Copyright (c) 2021 Nitric Technologies Pty Ltd.
#
# This file is part of Nitric Python 3 SDK.
# See https://github.com/nitrictech/python-sdk for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from betterproto.lib.google.protobuf import Struct

from nitric.api import EventClient, Event
from nitric.api._utils import _struct_from_dict


class Object(object):
    pass


class EventClientTest(IsolatedAsyncioTestCase):
    async def test_publish(self):
        mock_publish = AsyncMock()
        mock_response = Object()
        mock_response.id = "test-id"
        mock_publish.return_value = mock_response

        payload = {"content": "of event"}

        with patch("nitric.proto.nitric.event.v1.EventStub.publish", mock_publish):
            topic = EventClient().topic("test-topic")
            event = await topic.publish(Event(payload=payload))

        # Check the returned ID was set on the event
        assert event.id == "test-id"

        # Check expected values were passed to Stub
        mock_publish.assert_called_once()
        assert mock_publish.call_args.kwargs["topic"] == "test-topic"
        assert mock_publish.call_args.kwargs["event"].id == ""
        assert mock_publish.call_args.kwargs["event"].payload_type == ""
        assert len(mock_publish.call_args.kwargs["event"].payload.fields) == 1
        assert mock_publish.call_args.kwargs["event"].payload == _struct_from_dict(payload)

    async def test_publish_dict(self):
        mock_publish = AsyncMock()
        mock_response = Object()
        mock_response.id = "123"
        mock_publish.return_value = mock_response

        payload = {"content": "of event"}

        with patch("nitric.proto.nitric.event.v1.EventStub.publish", mock_publish):
            topic = EventClient().topic("test-topic")
            await topic.publish({"id": "123", "payload": payload})

        # Check expected values were passed to Stub
        mock_publish.assert_called_once()
        assert mock_publish.call_args.kwargs["topic"] == "test-topic"
        assert mock_publish.call_args.kwargs["event"].id == "123"
        assert mock_publish.call_args.kwargs["event"].payload_type == ""
        assert len(mock_publish.call_args.kwargs["event"].payload.fields) == 1
        assert mock_publish.call_args.kwargs["event"].payload == _struct_from_dict(payload)

    async def test_publish_invalid_type(self):
        mock_publish = AsyncMock()
        mock_response = Object()
        mock_response.id = "test-id"
        mock_publish.return_value = mock_response

        payload = {"content": "of event"}

        with patch("nitric.proto.nitric.event.v1.EventStub.publish", mock_publish):
            topic = EventClient().topic("test-topic")
            try:
                await topic.publish((1, 2, 3))
                assert False
            except AttributeError:
                # Exception raised if expected duck type attributes are missing
                assert True

    async def test_publish_none(self):
        mock_publish = AsyncMock()
        mock_response = Object()
        mock_response.id = "123"
        mock_publish.return_value = mock_response

        payload = {"content": "of event"}

        with patch("nitric.proto.nitric.event.v1.EventStub.publish", mock_publish):
            topic = EventClient().topic("test-topic")
            await topic.publish()

        # Check expected values were passed to Stub
        mock_publish.assert_called_once()
        assert mock_publish.call_args.kwargs["topic"] == "test-topic"
        assert mock_publish.call_args.kwargs["event"].id == ""
        assert mock_publish.call_args.kwargs["event"].payload_type == ""
        assert mock_publish.call_args.kwargs["event"].payload == Struct()
