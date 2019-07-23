"""A testing class for yamlloader"""
import unittest
import dork.yamlloader as loader


class TestYamlLoader(unittest.TestCase):
    """
    Testing YamlLoader
    """
    def test_yaml_loader(self):
        """
        Testing the writing_yml method
        """
        data = ['This a .yml file created by the yaml_loader testing module']
        file_path = './tests/testing_files/testing_yaml_loader_file.yml'
        self.assertEqual(loader.writing_yml(data, file_path), None)
