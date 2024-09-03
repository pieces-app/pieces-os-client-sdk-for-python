import unittest
from queue import Queue
from unittest.mock import Mock, patch
from pieces_os_client import (
    QGPTStreamEnum,
    RelevantQGPTSeeds
)
from pieces_os_client.wrapper.websockets import AskStreamWS
from pieces_os_client.wrapper.copilot import Copilot
from pieces_os_client.wrapper.basic_identifier.chat import BasicChat
from pieces_os_client.wrapper.streamed_identifiers.conversations_snapshot import ConversationsSnapshot

class BasicCopilotTest(unittest.TestCase):
    def setUp(self):
        self.assertEqual(1,2)
        self.mock_client = Mock()
        self.mock_client.tracked_application = Mock(id="mock_app_id")
        self.mock_client.model_id = "mock_model_id"
        self.mock_client.qgpt_api = Mock()
        
        self.copilot = Copilot(self.mock_client)

        self.mock_conversation = Mock()
        self.mock_conversation.id = "test_conversation_id"
        self.mock_conversations_snapshot = patch(
            'pieces_os_client.wrapper.streamed_identifiers.conversations_snapshot.ConversationsSnapshot.identifiers_snapshot',
            {"test_conversation_id": self.mock_conversation}
        ).start()
        self.addCleanup(patch.stopall)

    def tearDown(self):
        patch.stopall()

    def test_init(self):
        self.assertIsInstance(self.copilot, Copilot)
        self.assertEqual(self.copilot.pieces_client, self.mock_client)
        self.assertIsInstance(self.copilot._on_message_queue, Queue)
        self.assertIsInstance(self.copilot.ask_stream_ws, AskStreamWS)
        self.assertIsNone(self.copilot._chat)

    @patch('pieces_os_client.wrapper.websockets.AskStreamWS')
    def test_ask(self, mock_ask_stream_ws):
        conversation_id = "test_conversation_id"
        query = "Test query"
        mock_output = Mock(status=QGPTStreamEnum.COMPLETED, conversation=conversation_id, text="Test response")
        self.copilot._on_message_queue.put(mock_output)
        
        # Create a mock for send_message
        mock_send_message = Mock()
        self.copilot.ask_stream_ws.send_message = mock_send_message
        self.copilot.context._relevance_api = lambda query: RelevantQGPTSeeds(iterable=[])# Mock the contexts for now
        result = list(self.copilot.stream_question(query))
        
        # Mock the conversation created
        mock_conversation = Mock()
        mock_conversation.name = "Test Conversation"
        mock_conversation.id = conversation_id
        ConversationsSnapshot.identifiers_snapshot = {conversation_id: mock_conversation}
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], mock_output)
        self.assertIsInstance(self.copilot.chat, BasicChat)
        self.assertEqual(self.copilot.chat.id, conversation_id)
        
        # Assert that send_message was called once
        mock_send_message.assert_called_once()

    def test_question(self):
        query = "Test question"
        mock_output = Mock(text="Test answer", answers=[])
        self.mock_client.qgpt_api.question.return_value = mock_output
        
        result = self.copilot.question(query)
        
        self.assertEqual(result, mock_output)
        self.mock_client.qgpt_api.question.assert_called_once()

    def test_chats(self):
        ConversationsSnapshot.identifiers_snapshot = {"chat1": Mock(), "chat2": Mock()}
        chats = self.copilot.chats()
        
        self.assertEqual(len(chats), 2)
        self.assertIsInstance(chats[0], BasicChat)
        self.assertIsInstance(chats[1], BasicChat)

    def test_chat_property(self):
        self.assertIsNone(self.copilot.chat)
        
        test_chat = BasicChat("test_conversation_id")
        self.copilot.chat = test_chat
        self.assertEqual(self.copilot.chat, test_chat)
        
        with self.assertRaises(ValueError):
            self.copilot.chat = "invalid_chat"
        self.copilot.chat = None
        self.assertEqual(self.copilot.chat, None)

if __name__ == '__main__':
    unittest.main()

