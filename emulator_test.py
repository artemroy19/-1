import unittest
from emulator import Emulator
from commands import ls, cd, uniq, uptime

class EmulatorTest(unittest.TestCase):
    def setUp(self):
        self.emulator = Emulator("/Users/artem/Desktop/conf/archive.tar")


    def test_ls_root(self):
        """Тест ls для корневой директории."""
        result = ls(self.emulator.current_directory)
        self.assertIn("file2.txt", result)
        self.assertIn("file3.txt", result)
        self.assertIn("file1.txt", result)
        self.assertIn("direct", result)
        self.assertIn("._file1.txt", result)


    def test_ls_nonexistent_directory(self):
        """Тест ls для несуществующей директории."""
        result = ls("/error")
        self.assertEqual(result, "Directory not found")

    def test_cd_valid_directory(self):
        """Тест cd для валидной директории."""
        result = cd("direct", self.emulator)
        self.assertEqual(result, "Current directory: /direct")
        self.assertEqual(self.emulator.current_directory, "/direct")


    def test_cd_invalid_directory(self):
        """Тест cd для невалидной директории."""
        result = cd("error", self.emulator)
        self.assertEqual(result, "Directory not found")

    def test_uniq(self):
        """Тест uniq для простого файла."""
        result = uniq(["file1.txt"])
        self.assertEqual(result, "123\n122345\nAAAAAA")
        pass

    def test_uniq_bad(self):
        """Тест uniq для простого файла."""
        result = uniq([])
        self.assertEqual(result, "Usage: uniq <filename>")
        pass

    def test_uptime(self):
        """Тест uptime."""
        result = uptime()
        self.assertTrue(result.startswith("09:31"))
        pass

if __name__ == '__main__':
    unittest.main()
