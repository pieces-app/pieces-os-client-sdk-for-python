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

        result = self.context._get_relevant_dict()

        self.assertEqual(result["paths"], ["/tmp"])
        self.assertIsInstance(result["seed"], Seeds)
        self.assertIsInstance(result["assets"], FlattenedAssets)
        self.assertIsInstance(result["messages"], FlattenedConversationMessages)

    def test_check_relevant_existence(self):
        self.assertFalse(self.context._check_relevant_existance())
        self.context.paths = ["/tmp"]
        self.assertTrue(self.context._check_relevant_existance())

    @patch('pieces_os_client.wrapper.basic_identifier.message.BasicMessage')
    def test_check_messages(self, mock_basic_message):
        mock_message = MagicMock(spec=BasicMessage)
        mock_message.message = "test_message"
        mock_basic_message.return_value = mock_message

        messages = [mock_message, mock_message]
        result = Context._check_messages(messages)
        self.assertIsInstance(result, FlattenedConversationMessages)
        self.assertEqual(len(result.iterable), 2)

    @patch('pieces_os_client.wrapper.basic_identifier.asset.AssetSnapshot.identifiers_snapshot')
    @patch('pieces_os_client.wrapper.basic_identifier.asset.BasicAsset')
    def test_check_assets(self, mock_basic_asset, mock_identifiers_snapshot):
        mock_identifiers_snapshot.get.return_value = Mock()
        mock_asset = MagicMock(spec=BasicAsset)
        mock_asset.asset = "test_asset"
        mock_basic_asset.return_value = mock_asset

        assets = [mock_asset, mock_asset]
        result = Context._check_assets(assets)
        self.assertIsInstance(result, FlattenedAssets)
        self.assertEqual(len(result.iterable), 2)

    @patch('os.path.exists')
    def test_check_paths(self, mock_exists):
        mock_exists.return_value = True
        Context._check_paths(["/tmp"])
        mock_exists.assert_called_once_with("/tmp")

        mock_exists.return_value = False
        with self.assertRaises(ValueError):
            Context._check_paths(["/invalid"])

    @patch('pieces_os_client.wrapper.basic_identifier.asset.AssetSnapshot.pieces_client')
    @patch('pieces_os_client.wrapper.basic_identifier.asset.BasicAsset._get_seed')
    def test_check_raw_assets(self, mock_get_seed, mock_pieces_client):
        mock_seed = MagicMock()
        mock_get_seed.return_value = mock_seed
        raw_assets = ["test1", "test2"]
        result = Context._check_raw_assets(raw_assets)
        self.assertIsInstance(result, Seeds)
        self.assertEqual(len(result.iterable), 2)
