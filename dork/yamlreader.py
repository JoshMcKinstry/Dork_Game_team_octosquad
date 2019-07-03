"""A parser for .yml and .ymal files."""
import os
import yaml


def valid_file_path(file_path):
    """
    checking for valid file path and valid extension
    """
    return os.path.isfile(file_path)


def valid_extension(file_path):
    """
    validating .yml or .ymal extension
    """
    file_extension = os.path.splitext(file_path)
    is_valid_extension = file_extension[1] == '.yml'
    return is_valid_extension


def reading_yml(file_path):
    """
    reading the content of the .yml or file
    """
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data
