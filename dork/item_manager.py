"""
A module that handles the functionality of items.
"""
from dork.items import Item
DICT_ITEMS = {}


def assembling_items(names, descriptions, properties):
    """
    Constructs item objects for all items in game and stores all the items
    inside a dictionary.

    Parameters:
        names(list): A list that contains all the items available to game.
        description(list): A list that has all the item descriptions.
        properties(list): A list of  lists that contain all the
                properties associated with an item.
    """
    scope = range(len(names))
    for i in scope:
        item = Item(names[i], descriptions[i], properties[i])
        DICT_ITEMS.update({item.name: item})


def is_item(item_name):
    """
    A function that verifies that an object is a valid item.

    Parameters:
        item_name(str): Holds the name of item.

    Returns:
        bool: Returns true if item is in dictionary. Returns false otherwise.
    """
    return item_name in DICT_ITEMS.keys()


def item_description(item_name):
    """
    A function that gets the item description.

    Parameters:
        item_name(str): Name of item in dictionary

    Returns:
        dict: String description of item.
    """
    return DICT_ITEMS[item_name].description


def items_yaml_representation():
    """
    Creates a yaml friendly representation of the set of items.

    Returns:
        items_repr(dict): Returns dictionary that contains all item objects.
    """
    items = {}
    items_repr = {'Items': items}
    for item_obj in list(DICT_ITEMS.values()):
        items.update(item_obj.yaml_representation())
    return items_repr
