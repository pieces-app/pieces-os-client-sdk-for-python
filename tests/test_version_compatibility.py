import unittest
from pieces_os_client.wrapper.version_compatibility import VersionChecker,UpdateEnum

class TestVersionChecker(unittest.TestCase):
    def test_version_in_range(self):
        checker = VersionChecker("1.0.0", "2.0.0", "1.5.0")
        result = checker.version_check()
        self.assertTrue(result.compatible)
        self.assertIsNone(result.update)

    def test_version_below_minimum(self):
        checker = VersionChecker("1.0.0", "2.0.0", "0.9.0")
        result = checker.version_check()
        self.assertFalse(result.compatible)
        self.assertEqual(result.update, UpdateEnum.PiecesOS)

    def test_version_above_maximum(self):
        checker = VersionChecker("1.0.0", "2.0.0", "2.1.0")
        result = checker.version_check()
        self.assertFalse(result.compatible)
        self.assertEqual(result.update, UpdateEnum.Plugin)

    def test_version_at_minimum(self):
        checker = VersionChecker("1.0.0", "2.0.0", "1.0.0")
        result = checker.version_check()
        self.assertTrue(result.compatible)
        self.assertIsNone(result.update)

    def test_version_at_maximum(self):
        checker = VersionChecker("1.0.0", "2.0.0", "2.0.0")
        result = checker.version_check()
        self.assertFalse(result.compatible)
        self.assertEqual(result.update,UpdateEnum.Plugin)

    def test_version_with_pre_release(self):
        checker = VersionChecker("1.0.0", "2.0.0", "1.0.0-alpha")
        result = checker.version_check()
        self.assertFalse(result.compatible)
        self.assertEqual(result.update,UpdateEnum.PiecesOS)

    def test_version_below_minimum_with_pre_release(self):
        checker = VersionChecker("1.0.0", "2.0.0", "0.9.0-beta")
        result = checker.version_check()
        self.assertFalse(result.compatible)
        self.assertEqual(result.update, UpdateEnum.PiecesOS)

    def test_version_above_maximum_with_pre_release(self):
        checker = VersionChecker("1.0.0", "2.0.0", "2.1.0-beta")
        result = checker.version_check()
        self.assertFalse(result.compatible)
        self.assertEqual(result.update, UpdateEnum.Plugin)

    def test_parse_version(self):
        checker = VersionChecker("1.0.0", "2.0.0", "1.5.0")
        self.assertEqual(checker._parse_version("1.2.3"), ((1, 2, 3), ()))
        self.assertEqual(checker._parse_version("1.2.3-alpha.1"), ((1, 2, 3), ('alpha', '1')))
        self.assertEqual(checker._parse_version("1.2.3-beta"), ((1, 2, 3), ('beta',)))
        with self.assertRaises(ValueError):
            checker._parse_version("invalid.version")

    def test_compare(self):
        self.assertEqual(VersionChecker.compare("1.0.0", "1.0.0"), 0)
        self.assertEqual(VersionChecker.compare("1.0.0", "1.0.1"), -1)
        self.assertEqual(VersionChecker.compare("1.1.0", "1.0.1"), 1)
        self.assertEqual(VersionChecker.compare("1.0.0-alpha", "1.0.0"), -1)
        self.assertEqual(VersionChecker.compare("1.0.0", "1.0.0-alpha"), 1)
        self.assertEqual(VersionChecker.compare("1.0.0-alpha.1", "1.0.0-alpha.2"), -1)
        self.assertEqual(VersionChecker.compare("1.0.0-beta", "1.0.0-alpha"), 1)

    def test_version_check(self):
        # Test version within range
        checker = VersionChecker("1.0.0", "2.0.0", "1.5.0")
        result = checker.version_check()
        self.assertTrue(result.compatible)
        self.assertIsNone(result.update)

        # Test version below minimum
        checker = VersionChecker("1.0.0", "2.0.0", "0.9.0")
        result = checker.version_check()
        self.assertFalse(result.compatible)
        self.assertEqual(result.update, UpdateEnum.PiecesOS)

        # Test version above maximum
        checker = VersionChecker("1.0.0", "2.0.0", "2.1.0")
        result = checker.version_check()
        self.assertFalse(result.compatible)
        self.assertEqual(result.update, UpdateEnum.Plugin)

        # Test edge cases
        checker = VersionChecker("1.0.0", "2.0.0", "1.0.0")
        self.assertTrue(checker.version_check().compatible)
        checker = VersionChecker("1.0.0", "2.0.0", "2.0.0")
        self.assertFalse(checker.version_check().compatible)

if __name__ == "__main__":
    unittest.main()
