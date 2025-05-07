import unittest
from unittest.mock import Mock, patch, MagicMock

from pieces_os_client.models.seeded_asset import SeededAsset
from pieces_os_client.models.conversation_message import ConversationMessage
from pieces_os_client.wrapper.basic_identifier import BasicAsset, BasicMessage
from pieces_os_client.wrapper.basic_identifier.anchor import BasicAnchor
from pieces_os_client.wrapper.basic_identifier.asset import AssetSnapshot
from pieces_os_client.wrapper.context import Context

class BasicTestContext(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        self.mock_copilot = Mock()
        self.context = Context(self.mock_client, self.mock_copilot)
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

    @patch("pieces_os_client.models.anchor.Anchor")
    @patch("os.path.exists")
    @patch('pieces_os_client.wrapper.basic_identifier.message.BasicMessage')
    @patch('pieces_os_client.wrapper.basic_identifier.asset.BasicAsset')
    def test_clear(self, mock_basic_asset, mock_basic_message, mock_path, mock_anchor):
        BasicAnchor.from_raw_content = Mock(return_value=mock_anchor)
        mock_asset = MagicMock(spec=BasicAsset)
        mock_message = MagicMock(spec=BasicMessage)
        mock_basic_asset.return_value = mock_asset
        mock_basic_message.return_value = mock_message
        mock_basic_message.message.message = MagicMock(spec=ConversationMessage)

        BasicAsset._get_seed = Mock(return_value=MagicMock(spec=SeededAsset))
        self.context._add_path = Mock()
        self.context._add_message = Mock(return_value=mock_basic_message)
        self.context._add_asset = Mock(return_value=mock_basic_asset)
        self.context.raw_assets.append("test")
        self.context.paths.append("test")
        self.context.assets.append(mock_asset)
        self.context.clear()
        self.assertEqual(self.context.raw_assets, [])
        self.assertEqual(self.context.paths, [])
        self.assertEqual(self.context.assets, [])

    def test_check_relevant_existence(self):
        self.assertFalse(self.context._check_relevant_existence())
        self.context.paths = ["/tmp"]
        self.assertTrue(self.context._check_relevant_existence())

