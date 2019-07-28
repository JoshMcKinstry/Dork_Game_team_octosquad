"""
A module that handles the functionality of player both NPCs and Player
"""
from dork.character import Character
DICT_CHARACTERS = {}


def assembling_player(position, inventory):
    """
    Loading the player specifications into the player object.

    Parameters:
        position (dict): A key to a dictionary of possible positions
        inventory (list): A list of the player's held items
    """
    player = Character('Player', position, inventory)
    DICT_CHARACTERS.update({player.name: player})


def player_position():
    """
    Returns the room that the player is in.

    Returns:
        DICT_CHARACTERS['Player'].position (dict): 
            The room the player is currently in
    """
    return DICT_CHARACTERS['Player'].position


def update_player_position(room_name):
    """
    Updates the player's position to the new room after moving.

    Parameters: 
        room_name (dict): A dictionary of possible rooms
    """
    DICT_CHARACTERS['Player'].position = room_name


def player_inventory():
    """
    This function returns a list of the player's inventory.

    Returns:
        DICT_CHARACTERS['Player'].inventory (dict):
            A dictionary of the items held by the player
    """
    return DICT_CHARACTERS['Player'].inventory


def player_has_item(item_name):
    """
    Checks whether or not the item is in the player's inventory.

    Parameters:
        item_name (dict): A dictionary of items
    
    Returns:
        item_name (list): A dictionary of items held by the player.
    """
    return item_name in player_inventory()


def update_player_inventory(item_name):
    """
    Adds an item to the player's inventory.

    Parameters: 
        item_name (dict): A dictionary of items in the game

    Returns:
        DICT_CHARACTERS['Player'].add_item(item_name) (dict):
            A dictionary of items held by the player
            with the item in question added.
    """
    return DICT_CHARACTERS['Player'].add_item(item_name)


def remove_item_from_inventory(item_name):
    """
    Removes the item from the player's inventory.

    Parameters:
        item_name (dict): A dictionary of items in the game

    Returns:
        DICT_CHARACTERS['Player'].delete_item(item_name) (dict):
            A dictionary of items held by the player
            with the item in question deleted.
    """
    return DICT_CHARACTERS['Player'].delete_item(item_name)


def player_yaml_representation():
    """
    Returns a friendly yaml representation of the player.

    Returns:
        player_repr (dict): A dictionary of dictionaries
            showing the current chracter state.
    """
    inventory = DICT_CHARACTERS['Player'].inventory
    position = DICT_CHARACTERS['Player'].position
    player = {'Inventory': inventory, 'Position': position}
    player_repr = {'Player': player}
    return player_repr
