from typing import TYPE_CHECKING, Optional

from pieces_os_client.models.annotation import Annotation
from pieces_os_client.models.annotation_type_enum import AnnotationTypeEnum
from pieces_os_client.models.seeded_annotation import SeededAnnotation
from .basic import Basic

if TYPE_CHECKING:
	from . import BasicChat, BasicAsset
	from ..client import PiecesClient

class BasicAnnotation(Basic):
	def __init__(self,pieces_client:"PiecesClient", annotation:Annotation) -> None:
		self.pieces_client = pieces_client
		self.annotation = annotation
		super().__init__(annotation.id)

	@property
	def id(self):
		return self.annotation.id

	@staticmethod
	def annotation_from_id(pieces_client:"PiecesClient",id) -> "BasicAnnotation":
		return BasicAnnotation(pieces_client,
			pieces_client.annotation_api.annotation_specific_annotation_snapshot(id))

	def type(self) -> AnnotationTypeEnum:
		return self.annotation.type

	@property
	def raw_content(self):
		return self.annotation.text

	@raw_content.setter
	def raw_content(self,t):
		self.annotation.text = t 
		self._edit_annotation(self.annotation)

	@property
	def asset(self) -> Optional["BasicAsset"]:
		from . import BasicAsset
		if self.annotation.asset:
			return BasicAsset(self.annotation.asset.id)

	@property
	def chat(self) -> Optional["BasicChat"]:
		from . import BasicChat
		if self.annotation.conversation:
			return BasicChat(self.annotation.conversation.id)

	def _edit_annotation(self,annotation:Annotation):
		self.pieces_client.annotation_api.annotation_update(annotation)

	@staticmethod
	def create_annotation(pieces_client,seeded_annotation:SeededAnnotation) -> "BasicAnnotation":
		return BasicAnnotation(
			pieces_client,
			pieces_client.annotations_api.annotations_create_new_annotation(
				seeded_annotation
			))

	def delete(self):
		self.pieces_client.annotations_api.annotations_delete_specific_annotation(self.annotation.id)

