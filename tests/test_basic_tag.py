import unittest
from unittest.mock import Mock, patch, MagicMock
from pieces_os_client.models import Tag, SeededTag, ExistentMetadata
from pieces_os_client.wrapper.basic_identifier.tag import BasicTag

class TestBasicTag(unittest.TestCase):

    def setUp(self):
        self.mock_client = Mock()
        self.mock_tag = Mock(spec=Tag)
        self.mock_tag.id = "test_tag_id"
        self.mock_tag.text = "test_tag_text"

    def test_init(self):
        basic_tag = BasicTag(self.mock_client, self.mock_tag)
        self.assertEqual(basic_tag.pieces_client, self.mock_client)
        self.assertEqual(basic_tag.tag, self.mock_tag)

    @patch('pieces_os_client.wrapper.basic_identifier.tag.BasicTag.from_id')
    def test_from_id(self, mock_from_id):
        mock_from_id.return_value = BasicTag(self.mock_client, self.mock_tag)
        result = BasicTag.from_id(self.mock_client, "test_id")
        self.assertIsInstance(result, BasicTag)
        mock_from_id.assert_called_once_with(self.mock_client, "test_id")
