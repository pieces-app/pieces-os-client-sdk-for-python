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
