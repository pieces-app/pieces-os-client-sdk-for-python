import pytest
from unittest.mock import Mock, patch
from pieces_os_client.models.annotation_type_enum import AnnotationTypeEnum
from pieces_os_client.wrapper.basic_identifier.chat import BasicChat
from pieces_os_client.wrapper.streamed_identifiers.conversations_snapshot import ConversationsSnapshot
from pieces_os_client.models.conversation import Conversation

class TestBasicChat:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.mock_conversation = Mock(spec=Conversation)
        self.mock_conversation.name = "Test Conversation"
        self.mock_conversation.id = "test_id"
        self.mock_conversation.messages = Mock(indices={})
        self.mock_conversation.annotations = None
        self.mock_conversation.websites = None
        
        self.mock_conversation_other = Mock(spec=Conversation)
        self.mock_conversation_other.name = "Other Conversation"
        self.mock_conversation_other.id = "other_id"
        self.mock_conversation_other.messages = Mock(indices={})
        self.mock_conversation_other.annotations = None
        self.mock_conversation_other.websites = None
        
        ConversationsSnapshot.identifiers_snapshot = {
            "test_id": self.mock_conversation,
            "other_id": self.mock_conversation_other
        }
        ConversationsSnapshot.pieces_client = Mock()

    def test_init_valid_id(self):
        chat = BasicChat("test_id")
        assert chat.id == "test_id"
        assert chat.name == "Test Conversation"

    def test_init_invalid_id(self):
        with pytest.raises(ValueError, match="Conversation not found"):
            BasicChat("invalid_id").conversation

    def test_name_property(self):
        chat = BasicChat("test_id")
        assert chat.name == "Test Conversation"
        
        chat.name = "New Name"
        assert chat.name == "New Name"
        ConversationsSnapshot.pieces_client.conversation_api.conversation_update.assert_called_once()

    def test_name_property_default(self):
        self.mock_conversation.name = None
        chat = BasicChat("test_id")
        assert chat.name == "New Conversation"

    def test_conversation_property(self):
        chat = BasicChat("test_id")
        assert isinstance(chat.conversation, Conversation)
        assert chat.conversation.id == "test_id"

    def test_id_property(self):
        chat = BasicChat("test_id")
        assert chat.id == "test_id"

    @patch('pieces_os_client.wrapper.basic_identifier.message.BasicMessage')
    def test_messages(self, mock_basic_message):
        self.mock_conversation.messages.indices = {
            "msg1": 0,
            "msg2": 1,
            "msg3": -1  # Deleted message
        }
        
        chat = BasicChat("test_id")
        messages = chat.messages()
        
        assert len(messages) == 2
        mock_basic_message.assert_called()

    @patch('pieces_os_client.wrapper.basic_identifier.BasicAnnotation')
    def test_annotations_property(self, mock_basic_annotation):
        mock_annotation1 = Mock(id="ann1")
        mock_basic_annotation.from_id.return_value = mock_annotation1

        self.mock_conversation.annotations = Mock(indices={"ann1":1})
        
        chat = BasicChat("test_id")
        annotations = chat.annotations
        
        assert annotations is not None
        assert len(annotations) == 1

    def test_annotations_property_none(self):
        ConversationsSnapshot.identifiers_snapshot["test_id"].annotations = None
        
        chat = BasicChat("test_id")
        assert chat.annotations == []

    @patch('pieces_os_client.wrapper.basic_identifier.chat.BasicChat')
    def test_summary_property(self, MockBasicChat):
        mock_chat = Mock()
        MockBasicChat.return_value = mock_chat

        mock_summary_annotation = Mock(type=AnnotationTypeEnum.SUMMARY, raw_content="Test summary")
        mock_other_annotation = Mock(type=AnnotationTypeEnum.COMMENT, raw_content="Other content")
        
        mock_chat.annotations = [mock_other_annotation, mock_summary_annotation]
        mock_chat.summary = BasicChat.summary.fget(mock_chat)  # Call the original summary method
        
        assert mock_chat.summary == "Test summary"

    @patch('pieces_os_client.wrapper.basic_identifier.chat.BasicChat')
    def test_summary_property_no_summary(self, MockBasicChat):
        mock_chat = Mock()
        MockBasicChat.return_value = mock_chat

        mock_other_annotation = Mock(type=AnnotationTypeEnum.COMMENT, raw_content="Other content")
        
        mock_chat.annotations = [mock_other_annotation]
        mock_chat.summary = BasicChat.summary.fget(mock_chat)  # Call the original summary method
        
        assert mock_chat.summary is None

    @patch('pieces_os_client.wrapper.basic_identifier.BasicWebsite')
    def test_websites_property(self, mock_bacic_website):
        mock_website1 = Mock(id="web1")
        self.mock_conversation.websites = Mock(indices={mock_website1:"1"})
        mock_bacic_website.from_id.return_value = mock_website1
        chat = BasicChat("test_id")
        websites = chat.websites
        
        assert websites is not None
        assert len(websites) == 1

    def test_delete(self):
        chat = BasicChat("test_id")
        chat.delete()
        
        ConversationsSnapshot.pieces_client.conversations_api.conversations_delete_specific_conversation.assert_called_once_with("test_id")

    def test_str_representation(self):
        chat = BasicChat("test_id")
        assert str(chat) == "ID: test_id, Name: Test Conversation"

    def test_repr_representation(self):
        chat = BasicChat("test_id")
        assert repr(chat) == "<BasicChat(id=test_id)>"

    def test_equality(self):
        chat1 = BasicChat("test_id")
        chat2 = BasicChat("test_id")
        chat3 = BasicChat("other_id")
        
        assert chat1 == chat2
        assert chat1 != chat3
        assert chat1 != "test_id"

    def test_hash(self):
        chat = BasicChat("test_id")
        assert hash(chat) == hash("test_id")

    @patch.object(ConversationsSnapshot, 'pieces_client')
    def test_edit_conversation(self, mock_pieces_client):
        mock_conversation = Mock()
        BasicChat._edit_conversation(mock_conversation)
        
        mock_pieces_client.conversation_api.conversation_update.assert_called_once_with(False, mock_conversation)

if __name__ == '__main__':
    pytest.main([__file__])
