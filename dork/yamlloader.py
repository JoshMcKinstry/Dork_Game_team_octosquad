"""
A module that writes data into a yml file
"""
import yaml


def writing_yml(data, file_path):
    """
    loading data into a .yml file

    Parameters:
        data(dict): Dictionary of the game data
        file_path(str): The path of the file
    """
    with open(file_path, 'w') as file_descriptor:
        yaml.safe_dump(data, file_descriptor)
