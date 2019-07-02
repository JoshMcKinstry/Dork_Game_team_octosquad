"""A testing class for yamlloader"""
import unittest
from unittest.mock import patch
import dork.yamlloader as loader


class TestYamlReader(unittest.TestCase):
    """
    Testing YamlReader
    """
    my_data = 'data'
    @patch('yaml.safe_dump', return_value=my_data)
    def test_yaml_loader(self, my_data):
        """
        Testing the writing_yml method
        """
        my_list = my_data
        file_path = 'file_path'
        self.assertEqual(loader.writing_yml(my_list, file_path), None)
