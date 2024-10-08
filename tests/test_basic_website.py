import unittest
from unittest.mock import Mock, patch, PropertyMock
from pieces_os_client.models.website import Website
from pieces_os_client.models.seeded_website import SeededWebsite
from pieces_os_client.models.existent_metadata import ExistentMetadata
from pieces_os_client.wrapper.basic_identifier import BasicWebsite, BasicAsset

class TestBasicWebsite(unittest.TestCase):

    def setUp(self):
        self.mock_client = Mock()
        self.mock_website = Mock(spec=Website)
        self.mock_website.id = "test_id"
        self.mock_website.name = "Test Website"
        self.mock_website.url = "https://test.com"

    def test_init(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        self.assertEqual(basic_website.website, self.mock_website)
        self.assertEqual(basic_website.pieces_client, self.mock_client)

    @patch('pieces_os_client.wrapper.basic_identifier.website.BasicWebsite')
    def test_from_id(self, mock_basic_website):
        self.mock_client.website_api.websites_specific_website_snapshot.return_value = self.mock_website
        BasicWebsite.from_id(self.mock_client, "test_id")
        self.mock_client.website_api.websites_specific_website_snapshot.assert_called_once_with("test_id", transferables=True)
        mock_basic_website.assert_called_once_with(self.mock_client, self.mock_website)

    def test_from_id_error(self):
        self.mock_client.website_api.websites_specific_website_snapshot.side_effect = Exception("API Error")
        with self.assertRaises(ValueError):
            BasicWebsite.from_id(self.mock_client, "test_id")

    def test_create(self):
        seeded_website = SeededWebsite(url="https://test.com", name="Test Website")
        self.mock_client.websites_api.websites_create_new_website.return_value = self.mock_website
        basic_website = BasicWebsite.create(self.mock_client, seeded_website)
        self.mock_client.websites_api.websites_create_new_website.assert_called_once_with(transferables=False, seeded_website=seeded_website)
        self.assertIsInstance(basic_website, BasicWebsite)

    @patch('pieces_os_client.wrapper.basic_identifier.website.BasicWebsite.from_id')
    def test_exists(self, mock_from_id):
        mock_existent = Mock()
        mock_existent.website = Mock(id="test_id")
        self.mock_client.websites_api.websites_exists.return_value = mock_existent
        BasicWebsite.exists(self.mock_client, "https://test.com")
        self.mock_client.websites_api.websites_exists.assert_called_once_with(ExistentMetadata(value="https://test.com"))
        mock_from_id.assert_called_once_with(self.mock_client, "test_id")

    def test_from_raw_content_existing(self):
        with patch.object(BasicWebsite, 'exists', return_value=Mock(spec=BasicWebsite)) as mock_exists:
            result = BasicWebsite.from_raw_content(self.mock_client, "https://test.com")
            mock_exists.assert_called_once_with(self.mock_client, "https://test.com")
            self.assertIsInstance(result, BasicWebsite)

    @patch('pieces_os_client.wrapper.basic_identifier.website.BasicWebsite.create')
    def test_from_raw_content_new(self, mock_create):
        with patch.object(BasicWebsite, 'exists', return_value=None):
            BasicWebsite.from_raw_content(self.mock_client, "https://test.com")
            mock_create.assert_called_once_with(self.mock_client, SeededWebsite(url="https://test.com", name="https://test.com"))

    def test_properties(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        self.assertEqual(basic_website.name, "Test Website")
        self.assertEqual(basic_website.id, "test_id")
        self.assertEqual(basic_website.url, "https://test.com")

    def test_setters(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        basic_website.name = "New Name"
        self.assertEqual(basic_website.website.name, "New Name")
        self.mock_client.website_api.website_update.assert_called_once()

        basic_website.url = "https://newtest.com"
        self.assertEqual(basic_website.website.text, "https://newtest.com")
        self.mock_client.website_api.website_update.assert_called()

    def test_associate_asset(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        mock_asset = Mock()
        mock_asset.id = "asset_id"

        # Test associate_asset
        basic_website.associate_asset(mock_asset)
        self.mock_client.website_api.website_associate_asset.assert_called_once_with("asset_id", "test_id")

    def test_disassociate_asset(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        mock_asset = Mock()
        mock_asset.id = "asset_id"

        # Test disassociate_asset
        basic_website.disassociate_asset(mock_asset)
        self.mock_client.website_api.website_disassociate_asset.assert_called_once_with("test_id", "asset_id")

    def test_associate_chat(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        mock_chat = Mock()
        mock_chat.id = "chat_id"

        # Test associate_chat
        basic_website.associate_chat(mock_chat)
        self.mock_client.website_api.website_associate_conversation.assert_called_once_with("chat_id", "test_id")

    def test_disassociate_chat(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        mock_chat = Mock()
        mock_chat.id = "chat_id"

        # Test disassociate_chat
        basic_website.disassociate_chat(mock_chat)
        self.mock_client.website_api.website_disassociate_conversation.assert_called_once_with("test_id", "chat_id")

    def test_chats_property(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        
        # Mock the conversations attribute
        mock_conversation1 = Mock()
        mock_conversation1.id = "chat_id_1"
        mock_conversation2 = Mock()
        mock_conversation2.id = "chat_id_2"
        
        self.mock_website.conversations = Mock()
        self.mock_website.conversations.iterable = [mock_conversation1, mock_conversation2]
        
        # Create a mock ConversationsSnapshot
        mock_snapshot = Mock()
        mock_snapshot.identifiers_snapshot = {
            "chat_id_1": mock_conversation1,
            "chat_id_2": mock_conversation2
        }
        mock_snapshot.pieces_client = self.mock_client

        # Test the chats property
        with patch('pieces_os_client.wrapper.basic_identifier.chat.ConversationsSnapshot', mock_snapshot):
            chats = basic_website.chats
            
            self.assertIsNotNone(chats)
            self.assertEqual(len(chats), 2)
            
            # Check if the returned chats have the correct IDs
            chat_ids = [chat.id for chat in chats]
            self.assertIn("chat_id_1", chat_ids)
            self.assertIn("chat_id_2", chat_ids)

    def test_delete(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        basic_website.delete()
        self.mock_client.websites_api.websites_delete_specific_website.assert_called_once_with("test_id")

    def test_assets_property(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        
        # Mock the assets attribute
        mock_asset1 = Mock()
        mock_asset1.id = "asset_id_1"
        mock_asset2 = Mock()
        mock_asset2.id = "asset_id_2"
        
        self.mock_website.assets = Mock()
        self.mock_website.assets.iterable = [mock_asset1, mock_asset2]
        
        # Test the assets property
        
            
        assets = basic_website.assets
        self.assertIsNotNone(assets)
        self.assertEqual(len(assets), 2)
        # Check if the returned assets are instances of MockBasicAsset
        self.assertTrue(all(isinstance(asset,BasicAsset) for asset in assets))

if __name__ == '__main__':
    unittest.main()
