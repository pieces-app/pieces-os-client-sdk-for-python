import unittest
from unittest.mock import Mock, patch
from pieces_os_client.models.annotation import Annotation
from pieces_os_client.models.annotation_type_enum import AnnotationTypeEnum
from pieces_os_client.models.seeded_annotation import SeededAnnotation
from pieces_os_client.wrapper.basic_identifier.annotation import BasicAnnotation

class TestBasicAnnotation(unittest.TestCase):
    def setUp(self):
        self.mock_pieces_client = Mock()
        self.mock_annotation = Mock(spec=Annotation)
        self.mock_annotation.id = "test_annotation_id"
        self.mock_annotation.type = AnnotationTypeEnum.COMMENT
        self.mock_annotation.text = "Test annotation text"
        self.basic_annotation = BasicAnnotation(self.mock_pieces_client, self.mock_annotation)

    def test_init(self):
        self.assertEqual(self.basic_annotation.pieces_client, self.mock_pieces_client)
        self.assertEqual(self.basic_annotation.annotation, self.mock_annotation)
        self.assertEqual(self.basic_annotation.id, "test_annotation_id")

    def test_id_property(self):
        self.assertEqual(self.basic_annotation.id, "test_annotation_id")

    @patch('pieces_os_client.wrapper.basic_identifier.annotation.BasicAnnotation')
    def test_from_id(self, mock_basic_annotation):
        mock_basic_annotation.return_value = self.basic_annotation
        result = BasicAnnotation.from_id(self.mock_pieces_client, "test_annotation_id")
        self.assertEqual(result, self.basic_annotation)
        self.mock_pieces_client.annotation_api.annotation_specific_annotation_snapshot.assert_called_once_with("test_annotation_id")

    def test_type_property(self):
        self.assertEqual(self.basic_annotation.type, AnnotationTypeEnum.COMMENT)

    def test_raw_content_property(self):
        self.assertEqual(self.basic_annotation.raw_content, "Test annotation text")

    def test_raw_content_setter(self):
        self.basic_annotation.raw_content = "New annotation text"
        self.assertEqual(self.mock_annotation.text, "New annotation text")
        self.mock_pieces_client.annotation_api.annotation_update.assert_called_once_with(self.mock_annotation)

    @patch('pieces_os_client.wrapper.basic_identifier.asset.BasicAsset')
    def test_asset_property(self, MockBasicAsset):
        mock_asset = Mock()
        mock_asset.id = "test_asset_id"
        self.mock_annotation.asset = mock_asset
        
        mock_basic_asset = MockBasicAsset.return_value
        mock_basic_asset.name = "Test Asset"

        result = self.basic_annotation.asset
        self.assertIsNotNone(result)
        self.assertEqual(result, mock_basic_asset)
        MockBasicAsset.assert_called_once_with("test_asset_id")

    @patch('pieces_os_client.wrapper.basic_identifier.chat.BasicChat')
    def test_chat_property(self, MockBasicChat):
        mock_conversation = Mock()
        mock_conversation.id = "test_conversation_id"
        self.mock_annotation.conversation = mock_conversation
        
        mock_basic_chat = MockBasicChat.return_value
        mock_basic_chat.name = "Test Chat"

        result = self.basic_annotation.chat
        self.assertIsNotNone(result)
        self.assertEqual(result, mock_basic_chat)
        MockBasicChat.assert_called_once_with("test_conversation_id")

    @patch('pieces_os_client.wrapper.basic_identifier.annotation.BasicAnnotation')
    def test_create(self, mock_basic_annotation):
        mock_seeded_annotation = Mock(spec=SeededAnnotation)
        mock_created_annotation = Mock(spec=Annotation)
        self.mock_pieces_client.annotations_api.annotations_create_new_annotation.return_value = mock_created_annotation
        mock_basic_annotation.return_value = "Created BasicAnnotation"

        result = BasicAnnotation.create(self.mock_pieces_client, mock_seeded_annotation)
        
        self.assertEqual(result, "Created BasicAnnotation")
        self.mock_pieces_client.annotations_api.annotations_create_new_annotation.assert_called_once_with(mock_seeded_annotation)
        mock_basic_annotation.assert_called_once_with(self.mock_pieces_client, mock_created_annotation)

    def test_delete(self):
        self.basic_annotation.delete()
        self.mock_pieces_client.annotations_api.annotations_delete_specific_annotation.assert_called_once_with("test_annotation_id")

    def test_edit_annotation(self):
        mock_annotation = Mock(spec=Annotation)
        self.basic_annotation._edit_annotation(mock_annotation)
        self.mock_pieces_client.annotation_api.annotation_update.assert_called_once_with(mock_annotation)

if __name__ == '__main__':
    unittest.main()
