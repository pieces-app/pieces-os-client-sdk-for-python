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
