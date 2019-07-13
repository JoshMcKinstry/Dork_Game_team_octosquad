"""
A module that handles the functionality of player both NPCs and Player
"""
from character import Character
DICT_CHARACTERS = {}


def assembling_player(position, inventory):
    """
    Loading the player specs into player object
    """
    player = Character('Player', position, inventory)
    DICT_CHARACTERS.update({player.name: player})

def player_position():
    """
    """
    return DICT_CHARACTERS['Player'].position


def update_player_position(room_name):
    """
    """
    DICT_CHARACTERS['Player'].position = room_name


def player_inventory():
    """
    """
    return DICT_CHARACTERS['Player'].inventory


def update_player_inventory(item_name):
    """
    """
    return DICT_CHARACTERS['Player'].add_item(item_name)
