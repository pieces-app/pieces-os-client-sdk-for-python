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
