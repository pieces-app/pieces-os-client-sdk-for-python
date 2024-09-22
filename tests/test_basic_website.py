import unittest
from unittest.mock import Mock, patch, PropertyMock
from pieces_os_client.models import Website, SeededWebsite, ExistentMetadata
from pieces_os_client.wrapper.basic_identifier.website import BasicWebsite

class TestBasicWebsite(unittest.TestCase):

    def setUp(self):
        self.mock_client = Mock()
        self.mock_website = Mock(spec=Website)
        self.mock_website.id = "test_id"
        self.mock_website.name = "Test Website"
        self.mock_website.url = "https://test.com"

    @patch('pieces_os_client.wrapper.basic_identifier.website.BasicWebsite')
    def test_init(self):
        basic_website = BasicWebsite(self.mock_client, self.mock_website)
        self.assertEqual(basic_website.website, self.mock_website)
        self.assertEqual(basic_website.pieces_client, self.mock_client)

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
