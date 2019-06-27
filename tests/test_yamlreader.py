"""A testing class from yamlreader"""
import unittest
from dork.yamlreader import YamlReader


class TestYamlReader(unittest.TestCase):
    """
    Testing YamlReader
    """

    def test_valid_file_path(self):
        """
        Testing the file path method
        """
        reader = YamlReader()
        flag = reader.valid_file_path('dork.yml')
        self.assertFalse(flag)

    def test_valid_extension(self):
        """
        Testing the valid extension method
        """
        reader = YamlReader()
        path_file = 'dork.yml'
        flag = reader.valid_extension(path_file)
        self.assertTrue(flag)

    def test_yaml_loader(self):
        """
        Testing the yaml_loader method
        """
        reader = YamlReader()
        path_file = 'dork.yml'
        with self.assertRaises(FileNotFoundError):
            reader.yaml_loader(path_file)
