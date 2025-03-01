import unittest
from unittest.mock import patch, MagicMock
from pieces_os_client.wrapper.installation import PosInstaller, DownloadState

class TestPosInstaller(unittest.TestCase):
    def setUp(self):
        self.progress_updates = []
        self.mock_callback = lambda progress: self.progress_updates.append(progress)
        self.installer = PosInstaller(callback=self.mock_callback)

    def test_start_download_windows(self,):
        self.installer.start_download()
        self.installer.thread.join()
        self.assertEqual(self.installer.state, DownloadState.COMPLETED)
        self.assertEqual(len(self.progress_updates), 3)
        self.assertEqual(self.progress_updates[-1].percent, 100.0)

if __name__ == '__main__':
    unittest.main()
