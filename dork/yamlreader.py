"""A parser for .yml and .ymal files."""
import os
import yaml


class YamlReader:
    """
    A .yml/.ymal reader
    """
    @classmethod
    def valid_file_path(cls, file_path):
        """
        checking for valid file path and valid extension
        """
        return os.path.isfile(file_path)

    @classmethod
    def valid_extension(cls, file_path):
        """
        validating .yml or .ymal extension
        """
        file_extension = os.path.splitext(file_path)
        valid_extension = file_extension[1] == '.yml'
        return valid_extension

    @classmethod
    def yaml_loader(cls, file_path):
        """
        reading the content of the .yml or .ymal file
        """
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data
