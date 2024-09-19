from typing import TYPE_CHECKING, List, Optional

from pieces_os_client.models.existent_metadata import ExistentMetadata
from pieces_os_client.models.seeded_website import SeededWebsite
from pieces_os_client.models.website import Website
import urllib.parse

from .basic import Basic

if TYPE_CHECKING:
	from . import BasicAsset, BasicChat
	from ..client import PiecesClient

class BasicWebsite(Basic):
	def __init__(self,pieces_client:"PiecesClient", id:str) -> None:
		try:
			self.website = pieces_client.website_api.websites_specific_website_snapshot(
				id, transferables=True)
		except:
			raise ValueError("Error in retrieving the website")
		self.pieces_client = pieces_client

	@staticmethod
	def create_website(pieces_client:"PiecesClient",seeded_website:SeededWebsite) -> "BasicWebsite":
		return BasicWebsite(pieces_client,
			pieces_client.websites_api.websites_create_new_website(
				transferables=False,
				seeded_website=seeded_website).id
			)

	@staticmethod
	def websites_exists(pieces_client,url) -> Optional["BasicWebsite"]:
		existance = pieces_client.websites_api.websites_exists(
			ExistentMetadata(
				value=url
			))
		if existance.website:
			return BasicWebsite(pieces_client,existance.website.id)

	@classmethod
	def tag_from_raw_content(cls,pieces_client:"PiecesClient",url:str) -> "BasicWebsite":
		website = cls.websites_exists(pieces_client,url)
		return website if website else cls.create_website(
				pieces_client,
				SeededWebsite(url=url,name=urllib.parse.urlparse(url).netloc)
			)


	@property
	def name(self) -> str:
		return self.website.name

	@name.setter
	def name(self, name):
		self.website.name = name
		self._edit_website(self.website)

	@property
	def id(self) -> str:
		return self.website.id

	@property
	def url(self) -> str:
		return self.website.url

	@url.setter
	def url(self,url):
		self.website.text = url
		self._edit_website(self.website)

	@property
	def assets(self) -> Optional[List["BasicAsset"]]:
		from . import BasicAsset
		if self.website.assets and self.website.assets.iterable:
			return [BasicAsset(asset.id) for asset in self.website.assets.iterable]

	@property
	def chats(self) -> Optional[List["BasicChat"]]:
		from . import BasicChat
		if self.website.conversations and self.website.conversations.iterable:
			return [BasicChat(chat.id) for chat in self.website.conversations.iterable]

	def associate_asset(self,asset:"BasicAsset"):
		self.pieces_client.website_api.website_associate_asset(asset.id,self.website.id)

	def disassociate_asset(self,asset:"BasicAsset"):
		self.pieces_client.website_api.website_disassociate_asset(self.website.id,asset.id)

	def associate_chat(self,chat:"BasicChat"):
		self.pieces_client.website_api.website_associate_conversation(chat.id,self.website.id)

	def disassociate_chat(self,chat:"BasicChat"):
		self.pieces_client.website_api.website_disassociate_conversation(self.website.id,chat.id)

	def delete(self):
		self.pieces_client.websites_api.websites_delete_specific_website(self.website.id)

	def _edit_website(self,website:Website):
		return self.pieces_client.website_api.website_update(False,website)

