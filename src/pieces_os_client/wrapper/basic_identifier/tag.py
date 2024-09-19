from typing import TYPE_CHECKING, List, Optional

from pieces_os_client.models.existent_metadata import ExistentMetadata
from pieces_os_client.models.seeded_tag import SeededTag
from pieces_os_client.models.tag import Tag

from .basic import Basic

if TYPE_CHECKING:
	from .asset import BasicAsset
	from ..client import PiecesClient

class BasicTag(Basic):
	def __init__(self,pieces_client:"PiecesClient", id:str) -> None:
		try:
			self.tag = pieces_client.tag_api.tags_specific_tag_snapshot(
				id, transferables=True)
		except:
			raise ValueError("Error in retrieving the tag")
		self.pieces_client = pieces_client
		super().__init__(id)

	@classmethod
	def tag_from_raw_content(cls,pieces_client:"PiecesClient",raw_content:str) -> "BasicTag":
		existance = pieces_client.tags_api.tags_exists(ExistentMetadata(
			value=raw_content
		))
		if existance.tag:
			return BasicTag(pieces_client,existance.tag.id)
		else:
			return cls.create_tag(
				pieces_client,
				SeededTag(text=raw_content)
			)

	@staticmethod
	def create_tag(pieces_client:"PiecesClient",seeded_tag:SeededTag) -> "BasicTag":
		return BasicTag(pieces_client,
			pieces_client.tags_api.tags_create_new_tag(
				transferables=False,
				seeded_tag=seeded_tag).id
			)
	
	@property
	def id(self) -> str:
		return self.tag.id

	@property
	def raw_content(self) -> str:
		return self.tag.text

	@raw_content.setter
	def raw_content(self,raw_content):
		self.tag.text = raw_content
		self._edit_tag(self.tag)

	@property
	def assets(self) -> Optional[List["BasicAsset"]]:
		from . import BasicAsset
		if self.tag.assets and self.tag.assets.iterable:
			return [BasicAsset(asset.id) for asset in self.tag.assets.iterable]

	def associate_asset(self,asset:"BasicAsset"):
		self.pieces_client.tag_api.tag_associate_asset(asset.id,self.tag.id)

	def disassociate_asset(self,asset:"BasicAsset"):
		self.pieces_client.tag_api.tag_disassociate_asset(self.tag.id,asset.id)

	def delete(self):
		self.pieces_client.tags_api.tags_delete_specific_tag(self.tag.id)

	def _edit_tag(self,tag:Tag):
		self.pieces_client.tag_api.tag_update(False,tag)

