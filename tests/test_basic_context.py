import unittest
from unittest.mock import Mock, patch, MagicMock

from pieces_os_client.models.anchors import Anchors
from pieces_os_client.models.assets import Assets
from pieces_os_client.models.conversation_messages import ConversationMessages
from pieces_os_client.models.seeds import Seeds
from pieces_os_client.models.flattened_assets import FlattenedAssets 
from pieces_os_client.models.flattened_conversation_messages import FlattenedConversationMessages

from pieces_os_client.wrapper.basic_identifier import BasicAsset, BasicMessage
from pieces_os_client.wrapper.basic_identifier.asset import AssetSnapshot
from pieces_os_client.wrapper.context import Context
from pieces_os_client.wrapper.long_term_memory import LongTermMemory

class BasicTestContext(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        self.context = Context(self.mock_client)
        # Mock AssetSnapshot.pieces_client
        AssetSnapshot.pieces_client = MagicMock()

    @patch('pieces_os_client.wrapper.basic_identifier.message.BasicMessage')
    @patch('pieces_os_client.wrapper.basic_identifier.asset.BasicAsset')
    def test_init(self, mock_basic_asset, mock_basic_message):
        self.assertEqual(self.context.pieces_client, self.mock_client)
        self.assertEqual(self.context.raw_assets, [])
        self.assertEqual(self.context.paths, [])
        self.assertEqual(self.context.assets, [])
        self.assertEqual(self.context.messages, [])

    @patch('pieces_os_client.wrapper.basic_identifier.message.BasicMessage')
    @patch('pieces_os_client.wrapper.basic_identifier.asset.BasicAsset')
    def test_clear(self, mock_basic_asset, mock_basic_message):
        mock_asset = MagicMock(spec=BasicAsset)
        mock_message = MagicMock(spec=BasicMessage)
        mock_basic_asset.return_value = mock_asset
        mock_basic_message.return_value = mock_message

        self.context.raw_assets = ["test"]
        self.context.paths = ["test"]
        self.context.assets = [mock_asset]
        self.context.messages = [mock_message]
        self.context.clear()
        self.assertEqual(self.context.raw_assets, [])
        self.assertEqual(self.context.paths, [])
        self.assertEqual(self.context.assets, [])
        self.assertEqual(self.context.messages, [])

    @patch('pieces_os_client.wrapper.context.os.path.exists', return_value=True)
    @patch('pieces_os_client.wrapper.basic_identifier.asset.AssetSnapshot.identifiers_snapshot')
    @patch('pieces_os_client.wrapper.basic_identifier.message.BasicMessage')
    @patch('pieces_os_client.wrapper.basic_identifier.asset.BasicAsset')
    def test_get_relevant_dict(self, mock_basic_asset, mock_basic_message, mock_identifiers_snapshot, mock_exists):
        mock_identifiers_snapshot.get.return_value = Mock()
        mock_asset = MagicMock(spec=BasicAsset)
        mock_message = MagicMock(spec=BasicMessage)
        mock_ltm = MagicMock(spec=LongTermMemory)
        mock_basic_asset.return_value = mock_asset
        mock_basic_message.return_value = mock_message

        # Set the 'message' attribute on the mock_message
        mock_message.message = "test message"

        # Mock the _check_raw_assets method to return a valid Seeds object
        self.context._check_raw_assets = MagicMock(return_value=Seeds(iterable=[]))

        self.context.paths = ["/tmp"]
        self.context.assets = [mock_asset]
        self.context.raw_assets = ["test"]
        self.context.messages = [mock_message]
        self.context.ltm = mock_ltm

        result = self.context._get_relevant_dict()

        self.assertIsInstance(result["anchors"], Anchors)
        self.assertIsInstance(result["seed"], Seeds)
        self.assertIsInstance(result["assets"], Assets)
        self.assertIsInstance(result["messages"], FlattenedConversationMessages)

    def test_check_relevant_existence(self):
        self.assertFalse(self.context._check_relevant_existence())
        self.context.paths = ["/tmp"]
        self.assertTrue(self.context._check_relevant_existence())

