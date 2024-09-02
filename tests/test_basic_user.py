import unittest
from unittest.mock import MagicMock, patch
from pieces_os_client import UserProfile, AllocationStatusEnum

class BasicUserTest(unittest.TestCase):

    def setUp(self):
        self.mock_pieces_client = MagicMock()
        self.basic_user = BasicUser(self.mock_pieces_client)
        self.mock_user_profile = MagicMock(spec=UserProfile)
        self.basic_user.user_profile = self.mock_user_profile

