"""A testing class for yamlloader"""
import unittest
import dork.yamlloader as loader


class TestYamlReader(unittest.TestCase):
    """
    Testing YamlReader
    """

    def test_yaml_loader(self):
        """
        Testing the yaml_loader method
        """
        file_path = None
        dummy_data = [1]
        with self.assertRaises(TypeError):
            loader.writing_yml(dummy_data, file_path)
