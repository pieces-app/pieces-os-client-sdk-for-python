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

    @patch('pieces_os_client.wrapper.basic_identifier.tag.BasicTag.from_id')
    def test_exists(self, mock_from_id):
        self.mock_client.tags_api.tags_exists.return_value = Mock(tag=self.mock_tag)
        mock_from_id.return_value = BasicTag(self.mock_client, self.mock_tag)
        
        result = BasicTag.exists(self.mock_client, "test_content")
        
        self.assertIsInstance(result, BasicTag)
        self.mock_client.tags_api.tags_exists.assert_called_once_with(
            ExistentMetadata(value="test_content")
        )

    @patch('pieces_os_client.wrapper.basic_identifier.tag.BasicTag.exists')
    @patch('pieces_os_client.wrapper.basic_identifier.tag.BasicTag.create')
    def test_from_raw_content_existing(self, mock_create, mock_exists):
        mock_exists.return_value = BasicTag(self.mock_client, self.mock_tag)
        
        result = BasicTag.from_raw_content(self.mock_client, "test_content")
        
        self.assertIsInstance(result, BasicTag)
        mock_exists.assert_called_once_with(self.mock_client, "test_content")
        mock_create.assert_not_called()

    @patch('pieces_os_client.wrapper.basic_identifier.tag.BasicTag.exists')
    @patch('pieces_os_client.wrapper.basic_identifier.tag.BasicTag.create')
    def test_from_raw_content_new(self, mock_create, mock_exists):
        mock_exists.return_value = None
        mock_create.return_value = BasicTag(self.mock_client, self.mock_tag)
        
        result = BasicTag.from_raw_content(self.mock_client, "test_content")
        
        self.assertIsInstance(result, BasicTag)
        mock_exists.assert_called_once_with(self.mock_client, "test_content")
        mock_create.assert_called_once_with(self.mock_client, SeededTag(text="test_content"))

    def test_create(self):
        self.mock_client.tags_api.tags_create_new_tag.return_value = self.mock_tag
        seeded_tag = SeededTag(text="test_content")
        
        result = BasicTag.create(self.mock_client, seeded_tag)
        
        self.assertIsInstance(result, BasicTag)
        self.mock_client.tags_api.tags_create_new_tag.assert_called_once_with(seeded_tag=seeded_tag)

    def test_properties(self):
        basic_tag = BasicTag(self.mock_client, self.mock_tag)
        self.assertEqual(basic_tag.id, "test_tag_id")
        self.assertEqual(basic_tag.raw_content, "test_tag_text")

    def test_raw_content_setter(self):
        basic_tag = BasicTag(self.mock_client, self.mock_tag)
        basic_tag.raw_content = "new_content"
        self.assertEqual(basic_tag.tag.text, "new_content")
        self.mock_client.tag_api.tag_update.assert_called_once_with(False, basic_tag.tag)

    @patch.dict('sys.modules', {'pieces_os_client.wrapper.basic_identifier': MagicMock()})
    def test_assets(self):
        mock_basic_asset = MagicMock()
        import sys
        sys.modules['pieces_os_client.wrapper.basic_identifier'].BasicAsset = mock_basic_asset

        mock_asset = Mock()
        mock_asset.id = "test_asset_id"
        self.mock_tag.assets = Mock(iterable=[mock_asset])
        basic_tag = BasicTag(self.mock_client, self.mock_tag)
        
        assets = basic_tag.assets
        
        self.assertIsNotNone(assets)
        self.assertEqual(len(assets), 1)
        mock_basic_asset.assert_called_once_with("test_asset_id")

    def test_associate_asset(self):
        basic_tag = BasicTag(self.mock_client, self.mock_tag)
        mock_asset = Mock()
        mock_asset.id = "test_asset_id"
        
        basic_tag.associate_asset(mock_asset)
        
        self.mock_client.tag_api.tag_associate_asset.assert_called_once_with("test_asset_id", "test_tag_id")

    def test_disassociate_asset(self):
        basic_tag = BasicTag(self.mock_client, self.mock_tag)
        mock_asset = Mock()
        mock_asset.id = "test_asset_id"
        
        basic_tag.disassociate_asset(mock_asset)
        
        self.mock_client.tag_api.tag_disassociate_asset.assert_called_once_with("test_tag_id", "test_asset_id")

    def test_delete(self):
        basic_tag = BasicTag(self.mock_client, self.mock_tag)
        basic_tag.delete()
        self.mock_client.tags_api.tags_delete_specific_tag.assert_called_once_with("test_tag_id")
