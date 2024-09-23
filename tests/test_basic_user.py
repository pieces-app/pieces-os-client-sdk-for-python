import unittest
from unittest.mock import MagicMock, patch

from pieces_os_client.models.user_profile import UserProfile 
from pieces_os_client.models.allocation_status_enum import AllocationStatusEnum
from pieces_os_client.wrapper.basic_identifier import BasicUser

class BasicUserTest(unittest.TestCase):
    def setUp(self):
        self.mock_pieces_client = MagicMock()
        self.basic_user = BasicUser(self.mock_pieces_client)
        self.mock_user_profile = MagicMock(spec=UserProfile)
        self.basic_user.user_profile = self.mock_user_profile

    def test_id_property(self):
        self.mock_user_profile.id = "user123"
        self.assertEqual(self.basic_user.id, "user123")

    def test_on_user_callback(self):
        new_user_profile = MagicMock(spec=UserProfile)
        self.basic_user.on_user_callback(new_user_profile, connecting=True)
        self.assertEqual(self.basic_user.user_profile, new_user_profile)

    @patch('threading.Thread')
    def test_login(self, mock_thread):
        self.mock_pieces_client.os_api.sign_into_os.return_value = MagicMock()
        self.basic_user.login(connect_after_login=True, timeout=60)
        self.mock_pieces_client.os_api.sign_into_os.assert_called_once_with(async_req=True)
        mock_thread.assert_called_once()

    def test_login_and_connect(self):
        self.mock_pieces_client.os_api.sign_into_os.return_value = MagicMock()
        with patch('threading.Thread') as mock_thread:
            self.basic_user.login(connect_after_login=True)
            mock_thread.assert_called_once()
            
    def test_logout(self):
        self.basic_user.logout()
        self.mock_pieces_client.os_api.sign_out_of_os.assert_called_once()

    def test_connect(self):
        self.basic_user.connect()
        self.mock_pieces_client.allocations_api.allocations_connect_new_cloud.assert_called_once_with(self.mock_user_profile)

    def test_connect_without_login(self):
        self.basic_user.user_profile = None
        with self.assertRaises(PermissionError):
            self.basic_user.connect()

    def test_disconnect(self):
        self.mock_user_profile.allocation = MagicMock()
        self.basic_user.disconnect()
        self.mock_pieces_client.allocations_api.allocations_disconnect_cloud.assert_called_once_with(self.mock_user_profile.allocation)

    def test_disconnect_without_login(self):
        self.basic_user.user_profile = None
        with self.assertRaises(PermissionError):
            self.basic_user.disconnect()

    def test_picture_property(self):
        self.mock_user_profile.picture = "http://example.com/picture.jpg"
        self.assertEqual(self.basic_user.picture, "http://example.com/picture.jpg")

    def test_name_property(self):
        self.mock_user_profile.name = "John Doe"
        self.assertEqual(self.basic_user.name, "John Doe")

    def test_email_property(self):
        self.mock_user_profile.email = "john.doe@example.com"
        self.assertEqual(self.basic_user.email, "john.doe@example.com")

    def test_vanity_name_property(self):
        self.mock_user_profile.vanityname = "johnatpieces"
        self.assertEqual(self.basic_user.vanity_name, "johnatpieces")

    def test_cloud_status_property(self):
        mock_allocation = MagicMock()
        mock_allocation.status.cloud = AllocationStatusEnum.RUNNING
        self.mock_user_profile.allocation = mock_allocation
        self.assertEqual(self.basic_user.cloud_status, AllocationStatusEnum.RUNNING)

    def test_repr(self):
        expected_repr = f"<BasicUser(pieces_client={self.mock_pieces_client})>"
        self.assertEqual(repr(self.basic_user), expected_repr)

if __name__ == '__main__':
    unittest.main()
