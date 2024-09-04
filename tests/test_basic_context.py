import unittest
from unittest.mock import Mock, patch, MagicMock
from typing import List , TYPE_CHECKING
from pieces_os_client import QGPTRelevanceInput, Seeds, FlattenedAssets, FlattenedConversationMessages
from pieces_os_client.wrapper.basic_identifier import BasicAsset, BasicMessage
from pieces_os_client.wrapper.basic_identifier.asset import AssetSnapshot
from pieces_os_client.wrapper.context import Context
import os
if TYPE_CHECKING:
	from . import PiecesClient

