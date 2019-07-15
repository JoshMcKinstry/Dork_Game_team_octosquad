"""
A module that handles the functionality of player both NPCs and Player
"""
from dork.character import Character
DICT_CHARACTERS = {}


def assembling_player(position, inventory):
    """
    Loading the player specs into player object.
    """
    player = Character('Player', position, inventory)
    DICT_CHARACTERS.update({player.name: player})


def player_position():
    """
    Returns the room that the player is in.
    """
    return DICT_CHARACTERS['Player'].position


def update_player_position(room_name):
    """
    Updates the player's position to the new room after moving.
    """
    DICT_CHARACTERS['Player'].position = room_name


def player_inventory():
    """
    Returns a list of the player's inventory.
    """
    return DICT_CHARACTERS['Player'].inventory


def player_has_item(item_name):
    """
    Checks whether or not the item is inside of the player's inventory.
    """
    return item_name in player_inventory()


def update_player_inventory(item_name):
    """
    Adds an item to the player's inventory.
    """
    return DICT_CHARACTERS['Player'].add_item(item_name)


def remove_item_from_inventory(item_name):
    """
    Removes the item from the player's inventory.
    """
    return DICT_CHARACTERS['Player'].delete_item(item_name)
