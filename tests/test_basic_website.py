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
