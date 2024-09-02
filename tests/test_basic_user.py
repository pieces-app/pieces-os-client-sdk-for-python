import unittest
from unittest.mock import MagicMock, patch
from pieces_os_client import UserProfile, AllocationStatusEnum

class BasicUserTest(unittest.TestCase):

    def setUp(self):
        self.mock_pieces_client = MagicMock()
        self.basic_user = BasicUser(self.mock_pieces_client)
        self.mock_user_profile = MagicMock(spec=UserProfile)
        self.basic_user.user_profile = self.mock_user_profile

    def test_login(self):
        self.mock_pieces_client.os_api.sign_into_os.return_value = MagicMock()
        self.basic_user.login(connect_after_login=False)
        self.mock_pieces_client.os_api.sign_into_os.assert_called_once_with(async_req=True)

