import unittest
from unittest.mock import Mock, patch, MagicMock
from typing import List , TYPE_CHECKING
from pieces_os_client import QGPTRelevanceInput, Seeds, FlattenedAssets, FlattenedConversationMessages
from pieces_os_client.wrapper.basic_identifier import BasicAsset, BasicMessage
from pieces_os_client.wrapper.basic_identifier.asset import AssetSnapshot
from pieces_os_client.wrapper.context import Context
import os
if TYPE_CHECKING:
	from . import PiecesClient

class TestContext(unittest.TestCase):
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

	


