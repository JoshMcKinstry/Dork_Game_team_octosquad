"""A parser for .yml and .ymal files."""
import os
import yaml


def valid_file_path(file_path):
    """
    checking for valid file path and valid extension

    Parameters:
        file_path(string): The path of the file

    Returns:
        bool: Return true if the path of the file is valid
            Return false otherwise
    """
    return os.path.isfile(file_path)


def valid_extension(file_path):
    """
    validating .yml or .ymal extension

    Parameters:
        file_path(string): The path of the file
    Returns:
        bool: Return true if the extention is valid
            Return false otherwise
    """
    file_extension = os.path.splitext(file_path)
    is_valid_extension = file_extension[1] == '.yml'
    return is_valid_extension


def reading_yml(file_path):
    """
    reading the content of the .yml or file

    Parameters:
        file_path(string): The path of the file

    Returns:
        data: Return all the data from the yaml file
            if the path and extention are both valid
        None: Return nothing when path or extention of the file
            is not valid
    """
    if valid_extension(file_path) and valid_file_path(file_path):
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data
    return None
