import pytest
from unittest.mock import Mock, patch, call
from pieces_os_client.wrapper.basic_identifier.message import BasicMessage
from pieces_os_client.wrapper.basic_identifier.chat import BasicChat
from pieces_os_client.wrapper.streamed_identifiers.conversations_snapshot import ConversationsSnapshot

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
            b = BasicChat("invalid_id").conversation # Call the conversation to check if it is vaild

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

    @patch.object(BasicMessage, '__init__', return_value=None)
    def test_messages(self, mock_basic_message_init):
        ConversationsSnapshot.identifiers_snapshot["test_id"].messages = Mock()
        ConversationsSnapshot.identifiers_snapshot["test_id"].messages.indices = {
            "msg1": 0,
            "msg2": 1,
            "msg3": -1  # Deleted message
        }


        chat = BasicChat("test_id")
        messages = chat.messages()
        

        assert len(messages) == 2
        assert all(isinstance(msg, BasicMessage) for msg in messages)

        # Check that BasicMessage.__init__ was called twice
        assert mock_basic_message_init.call_count == 2

        # Check that BasicMessage.__init__ was called with the results of _get_message
        for call_args in mock_basic_message_init.call_args_list:
            assert isinstance(call_args[0][0], Mock)
            assert call_args[0][1] in ["msg1", "msg2"]

    def test_annotations_property(self):
        mock_annotations = Mock(iterable=["annotation1", "annotation2"])
        ConversationsSnapshot.identifiers_snapshot["test_id"].annotations = mock_annotations
        
        chat = BasicChat("test_id")
        assert chat.annotations == ["annotation1", "annotation2"]

    def test_annotations_property_none(self):
        ConversationsSnapshot.identifiers_snapshot["test_id"].annotations = None
        
        chat = BasicChat("test_id")
        assert chat.annotations is None

    def test_delete(self):
        chat = BasicChat("test_id")
        chat.delete()
        
        ConversationsSnapshot.pieces_client.conversations_api.conversations_delete_specific_conversation.assert_called_once_with("test_id")

    @patch.object(ConversationsSnapshot, 'pieces_client')
    def test_edit_conversation(self, mock_pieces_client):
        mock_conversation = Mock()
        BasicChat._edit_conversation(mock_conversation)
        
        mock_pieces_client.conversation_api.conversation_update.assert_called_once_with(False, mock_conversation)

if __name__ == '__main__':
    pytest.main([__file__])

