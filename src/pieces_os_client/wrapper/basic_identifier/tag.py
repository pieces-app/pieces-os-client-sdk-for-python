from typing import TYPE_CHECKING, List, Optional

from pieces_os_client.models.existent_metadata import ExistentMetadata
from pieces_os_client.models.seeded_tag import SeededTag
from pieces_os_client.models.tag import Tag

from .basic import Basic

if TYPE_CHECKING:
	from .asset import BasicAsset
	from ..client import PiecesClient

class BasicTag(Basic):
	"""
	Represents a basic tag in the system.

	Attributes:
	- pieces_client (PiecesClient): The client used to interact with the Pieces API.
	- tag (Tag): The tag object associated with this BasicTag instance.
	"""

	def __init__(self, pieces_client: "PiecesClient", id: str) -> None:
		"""
		Initializes a BasicTag instance.

		Args:
		- pieces_client (PiecesClient): The client used to interact with the Pieces API.
		- id (str): The ID of the tag.

		Raises:
		- ValueError: If there is an error retrieving the tag.
		"""
		try:
			self.tag = pieces_client.tag_api.tags_specific_tag_snapshot(
				id, transferables=True)
		except:
			raise ValueError("Error in retrieving the tag")
		self.pieces_client = pieces_client
		super().__init__(id)
	
	@classmethod
	def tag_from_raw_content(cls, pieces_client: "PiecesClient", raw_content: str) -> "BasicTag":
		"""
		Creates a BasicTag instance based on raw content.

		Args:
		- pieces_client (PiecesClient): The client used to interact with the Pieces API.
		- raw_content (str): The raw content of the tag.

		Returns:
		- BasicTag: The created BasicTag instance.
		"""
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
	def create_tag(pieces_client: "PiecesClient", seeded_tag: SeededTag) -> "BasicTag":
		"""
		Creates a new tag based on a seeded tag.

		Args:
		- pieces_client (PiecesClient): The client used to interact with the Pieces API.
		- seeded_tag (SeededTag): The seeded tag object.

		Returns:
		- BasicTag: The created BasicTag instance.
		"""

		return BasicTag(pieces_client,
			pieces_client.tags_api.tags_create_new_tag(
				transferables=False,
				seeded_tag=seeded_tag).id
			)

	@property
	def id(self) -> str:
		"""
		Gets the ID of the tag.

		Returns:
		- str: The ID of the tag.
		"""
		return self.tag.id

	@property
	def raw_content(self) -> str:
		"""
		Gets the raw content of the tag.

		Returns:
		- str: The raw content of the tag.
		"""
		return self.tag.text

	@raw_content.setter
	def raw_content(self, raw_content):
		"""
		Sets the raw content of the tag.

		Args:
		- raw_content: The raw content to be set.
		"""
		self.tag.text = raw_content
		self._edit_tag(self.tag)

	@property
	def assets(self) -> Optional[List["BasicAsset"]]:
		"""
		Gets the assets associated with the tag.

		Returns:
		- Optional[List["BasicAsset"]]: A list of BasicAsset objects associated with the tag.
		"""
		from . import BasicAsset
		if self.tag.assets and self.tag.assets.iterable:
			return [BasicAsset(asset.id) for asset in self.tag.assets.iterable]

	def associate_asset(self, asset: "BasicAsset"):
		"""
		Associates an asset with the tag.

		Args:
		- asset (BasicAsset): The asset to be associated.
		"""
		self.pieces_client.tag_api.tag_associate_asset(asset.id,self.tag.id)

	def disassociate_asset(self, asset: "BasicAsset"):
		"""
		Disassociates an asset from the tag.

		Args:
		- asset (BasicAsset): The asset to be disassociated.
		"""
		self.pieces_client.tag_api.tag_disassociate_asset(self.tag.id,asset.id)

	def delete(self):
		"""
		Deletes the tag.
		"""
		self.pieces_client.tags_api.tags_delete_specific_tag(self.tag.id)

	def _edit_tag(self, tag: Tag):
		"""
		Edits the tag.

		Args:
		- tag (Tag): The tag object to be edited.
		"""
		self.pieces_client.tag_api.tag_update(False,tag)

