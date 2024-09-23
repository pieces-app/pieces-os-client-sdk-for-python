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
