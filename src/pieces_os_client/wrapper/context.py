from typing import TYPE_CHECKING, List, Callable
import os

from pieces_os_client.models.anchors import Anchors
from pieces_os_client.models.assets import Assets
from pieces_os_client.models.seeds import Seeds
from pieces_os_client.models.flattened_conversation_messages import FlattenedConversationMessages
from pieces_os_client.wrapper.basic_identifier.anchor import BasicAnchor

from .long_term_memory import LongTermMemory

if TYPE_CHECKING:
	from .basic_identifier import BasicAsset,BasicMessage
	from . import PiecesClient
	from .copilot import Copilot

class ValidatedContextList(List):
	"""
	This is a list that notifies the callables if any item is added or removed from it.
	"""
	def __init__(self, *args, on_add: Callable = None, on_remove: Callable = None):
		self.on_add = on_add
		self.on_remove = on_remove
		super().__init__()
		for arg in args:
			self.append(arg)

	def append(self, value):
		self.on_add(value)
		super().append(value)

	def extend(self, iterable):
		for value in iterable:
			self.append(value)

	def insert(self, index, value):
		self.on_add(value)
		super().insert(index, value)

	def remove(self, value):
		index = self.index(value)
		self.on_remove(index)
		super().remove(value)

	def __setitem__(self, index, value):
		self.on_remove(index)
		self.on_add(value)
		super().__setitem__(index, value)

	def __iadd__(self, other):
		for value in other:
			self.append(value)
		return self

	def __add__(self, other):
		new_list = ValidatedContextList(self, on_add=self.on_add, on_remove=self.on_remove)
		for value in other:
			new_list.append(value)
		return new_list

	def pop(self, index: int = -1):
		value = super().pop(index)
		self.on_remove(index)
		return value

class Context:
	def __init__(self,
				 pieces_client: "PiecesClient",
				 copilot: "Copilot" = None,
				 paths: List[str] = None,
				 raw_assets: List[str] = None,
				 assets: List["BasicAsset"] = None,
				 messages: List["BasicMessage"] = None):
		self.pieces_client = pieces_client
		self.raw_assets: List[str] = ValidatedContextList(raw_assets, on_add=self._add_raw_asset, on_remove=self._remove_raw_asset) if raw_assets is not None else ValidatedContextList(on_add=self._add_raw_asset, on_remove=self._remove_raw_asset)
		self.paths: List[str] = ValidatedContextList(paths, on_add=self._add_path, on_remove=self._remove_path) if paths is not None else ValidatedContextList(on_add=self._add_path, on_remove=self._remove_path)
		self.assets: List["BasicAsset"] = ValidatedContextList(assets, on_add=self._add_asset, on_remove=self._remove_asset) if assets is not None else ValidatedContextList(on_add=self._add_asset, on_remove=self._remove_asset)
		self.messages: List["BasicMessage"] = ValidatedContextList(messages, on_add=self._add_message, on_remove=self._remove_message) if messages is not None else ValidatedContextList(on_add=self._add_message, on_remove=self._remove_message)
		self.copilot = copilot
		self.ltm = LongTermMemory(self)

		## Internal stuff
		self._assets: Assets = Assets(iterable=[])
		self._raw_assets: Seeds = Seeds(iterable=[])
		self._messages: FlattenedConversationMessages = FlattenedConversationMessages(iterable=[])
		self._paths: Anchors = Anchors(iterable=[])

	def clear(self):
		"""Clears the Copilot context"""
		self.raw_assets = []
		self.paths = []
		self.assets = []
		self.messages = []
		self._paths = Anchors(iterable=[])
		self._assets = Assets(iterable=[])
		self._raw_assets = Seeds(iterable=[])
		self._messages = FlattenedConversationMessages(iterable=[])

	def _get_relevant_dict(self):
		return {
			"anchors": self._paths,
			"seed": self._raw_assets,
			"assets": self._assets,
			"messages": self._messages
		}

	def _check_relevant_existence(self) -> bool:
		return bool(self.paths or self.assets or self.raw_assets)

	def _add_message(self, message):
		if not isinstance(message, BasicMessage):
			raise ValueError("Message should be BasicMessage type")
		self._messages.iterable.append(message.message)
		self.copilot.chat.associate_message(message)

	def _remove_message(self, index: int):
		message = self._messages.iterable.pop(index)
		self.copilot.chat.disassociate_message(BasicMessage(self.pieces_client, message.id))

	def _add_asset(self, asset):
		if not isinstance(asset, BasicAsset):
			raise ValueError("Snippet content should be BasicAsset type")
		self._assets.iterable.append(asset.asset)
		self.copilot.chat.associate_asset(asset)

	def _remove_asset(self, index: int):
		asset = self._assets.iterable.pop(index)
		self.copilot.chat.disassociate_asset(BasicAsset(asset.id))

	def _add_path(self,path):
		if not os.path.exists(path):
			raise ValueError("Invalid path in the context")
		anchor = BasicAnchor.from_raw_content(path)
		self._paths.iterable.append(anchor)
		self.copilot.chat.associate_anchor(anchor)

	def _remove_path(self, index: int):
		anchor = self._paths.iterable.pop(index)
		self.copilot.chat.disassociate_anchor(BasicAnchor(anchor.id))

	def _add_raw_asset(self, asset: str):
		if not isinstance(asset, str):
			raise ValueError("Raw snippet content should be string type")
		self._raw_assets.iterable.append(BasicAsset._get_seed(asset))

	def _remove_raw_asset(self, index: int):
		self._raw_assets.iterable.pop(index)

