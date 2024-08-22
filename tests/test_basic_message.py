import pytest
from unittest.mock import Mock, patch, call
from typing import Literal, Optional, List, TYPE_CHECKING , Dict , Union, Callable
from abc import ABC, abstractmethod
from pieces_os_client import (
    ApiClient,
    Application,
    Configuration,
    ConversationApi,
    ConversationMessageApi,
    ConversationMessagesApi,
    ConversationsApi,
    QGPTApi,
    UserApi,
    FormatApi,
    ConnectorApi,
    SeededConnectorConnection,
    SeededTrackedApplication,
    AssetApi,
    AssetsApi,
    FragmentMetadata,
    ModelsApi,
    AnnotationApi
)
import platform
import atexit
import sys
import importlib.util
import queue
from pieces_os_client import Conversation, StreamedIdentifiers, Asset
import threading
from pieces_os_client.wrapper.websockets import *
from pieces_os_client.wrapper.copilot import Copilot
from pieces_os_client.wrapper.client import PiecesClient
from pieces_os_client.wrapper.basic_identifier.asset import BasicAsset
from pieces_os_client.wrapper.basic_identifier.basic import Basic
from pieces_os_client.wrapper.basic_identifier.message import BasicMessage
from pieces_os_client.wrapper.basic_identifier.chat import BasicChat
from pieces_os_client.wrapper.streamed_identifiers.assets_snapshot import AssetSnapshot
from pieces_os_client.wrapper.streamed_identifiers._streamed_identifiers import StreamedIdentifiersCache
from pieces_os_client.wrapper.streamed_identifiers.conversations_snapshot import ConversationsSnapshot

# Test class
class TestBasicMessage:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.mock_pieces_client = Mock()
        self.mock_message = Mock()
        self.mock_message.id = "test_message_id"
        self.mock_message.fragment.string.raw = "Test message content"
        self.mock_message.role.value = "USER"
        self.mock_message.annotations = None

        # Mock the API call
        self.mock_pieces_client.conversation_message_api.message_specific_message_snapshot.return_value = self.mock_message

    def test_init_valid_id(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        assert message.id == "test_message_id"
        self.mock_pieces_client.conversation_message_api.message_specific_message_snapshot.assert_called_once_with(
            message="test_message_id", transferables=True
        )

    def test_init_invalid_id(self):
        self.mock_pieces_client.conversation_message_api.message_specific_message_snapshot.side_effect = Exception("Error")
        with pytest.raises(ValueError, match="Error in retrieving the message"):
            BasicMessage(self.mock_pieces_client, "invalid_id")

    def test_raw_property(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        assert message.raw == "Test message content"

    def test_raw_setter(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        message.raw = "New content"
        assert message.message.fragment.string.raw == "New content"
        self.mock_pieces_client.conversation_message_api.message_update_value.assert_called_once_with(
            False, message.message
        )

    def test_role_property(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        assert message.role == "USER"

    def test_id_property(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        assert message.id == "test_message_id"

    def test_delete_method(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        message.delete()
        self.mock_pieces_client.conversation_messages_api.messages_delete_specific_message.assert_called_once_with(
            "test_message_id"
        )

    def test_annotations_property_none(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        assert message.annotations is None

    def test_annotations_property_with_annotations(self):
        mock_annotation = Mock()
        mock_annotation.id = "test_annotation_id"
        self.mock_message.annotations = Mock(iterable=[Mock(id="test_annotation_id")])
        self.mock_pieces_client.annotation_api.annotation_specific_annotation_snapshot.return_value = mock_annotation

        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        annotations = message.annotations

        assert annotations is not None
        assert isinstance(annotations, Annotations)
        assert len(annotations.iterable) == 1
        assert annotations.iterable[0].id == "test_annotation_id"

    def test_description_property_no_annotations(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        assert message.description is None

    def test_description_property_with_description(self):
        # Create a mock annotation with the correct structure
        mock_annotation = Mock()
        mock_annotation.type = AnnotationTypeEnum.DESCRIPTION
        mock_annotation.text = "Test description"

        # Set up the mock message with annotations
        self.mock_message.annotations = Mock(iterable=[Mock(id="test_annotation_id")])

        # Mock the annotation API call
        self.mock_pieces_client.annotation_api.annotation_specific_annotation_snapshot.return_value = mock_annotation

        # Create the BasicMessage instance
        message = BasicMessage(self.mock_pieces_client, "test_message_id")

        # Replace the message's annotations with our mocked annotations
        message.message.annotations = self.mock_message.annotations

        # Now test the description property
        description = message.description
        print("Returned description:", description)

        assert description == "Test description"

        # Verify that the annotation API was called
        self.mock_pieces_client.annotation_api.annotation_specific_annotation_snapshot.assert_called_once_with("test_annotation_id")

    def test_repr(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        assert repr(message) == "<BasicMessage(id=test_message_id)>"

    def test_eq(self):
        # Create separate mock messages for each BasicMessage instance
        mock_message1 = Mock()
        mock_message1.id = "test_message_id_1"
        mock_message2 = Mock()
        mock_message2.id = "test_message_id_1"  # Same as message1
        mock_message3 = Mock()
        mock_message3.id = "test_message_id_2"  # Different from message1 and message2

        # Mock the API call to return different mock messages based on the input ID
        def mock_get_message(message, transferables):
            if message == "test_message_id_1":
                return mock_message1
            elif message == "test_message_id_2":
                return mock_message3
            else:
                raise ValueError("Unexpected message ID")

        self.mock_pieces_client.conversation_message_api.message_specific_message_snapshot.side_effect = mock_get_message

        message1 = BasicMessage(self.mock_pieces_client, "test_message_id_1")
        message2 = BasicMessage(self.mock_pieces_client, "test_message_id_1")
        message3 = BasicMessage(self.mock_pieces_client, "test_message_id_2")

        assert message1 == message2
        assert message1 != message3
        assert message1 != "not_a_message"

        # Verify that the API was called with the correct IDs
        self.mock_pieces_client.conversation_message_api.message_specific_message_snapshot.assert_has_calls([
            call(message="test_message_id_1", transferables=True),
            call(message="test_message_id_1", transferables=True),
            call(message="test_message_id_2", transferables=True)
        ])

    def test_str(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        assert str(message) == "ID: test_message_id"

    def test_hash(self):
        message = BasicMessage(self.mock_pieces_client, "test_message_id")
        assert hash(message) == hash("test_message_id")
