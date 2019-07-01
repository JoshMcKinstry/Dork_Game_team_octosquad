"""A testing class for yamlreader"""
import unittest
import dork.yamlreader as reader


class TestYamlReader(unittest.TestCase):
    """
    Testing YamlReader
    """

    def test_valid_file_path(self):
        """
        Testing the file path method
        """
        flag = reader.valid_file_path('no_path')
        self.assertFalse(flag)

    def test_valid_extension(self):
        """
        Testing the valid extension method
        """
        path_file = 'dork.yml'
        flag = reader.valid_extension(path_file)
        self.assertTrue(flag)

if __name__ == "__main__":
    unittest.main()