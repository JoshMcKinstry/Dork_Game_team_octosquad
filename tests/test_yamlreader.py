"""A testing class for yamlreader"""
import unittest
from unittest.mock import patch
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

    @patch('dork.yamlreader.valid_extension')
    @patch('dork.yamlreader.valid_file_path')
    @patch('yaml.safe_load', return_value={})
    def test_yaml_loader(self, user_file_path, is_path, is_valid):
        """
        Testing the reading_yml method
        """
        file_path = user_file_path
        is_path.return_value = True
        is_valid.return_value = True
        self.assertIsInstance(reader.reading_yml(file_path), dict)
        is_path.return_value = False
        is_valid.return_value = False
        self.assertIsNone(reader.reading_yml(file_path), None)
