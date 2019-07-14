"""
A module that handles the functionality of items
"""
from dork.items import Item
DICT_ITEMS = {}

def assembling_items(names, descriptions, properties):
    """
    Constructs item objects for all items in game and stores all the items
    inside a dictionary
    """
    scope = range(len(names))
    for i in scope:
        item = Item(names[i], descriptions[i], properties[i])
        DICT_ITEMS.update({item.name: item})


def is_item(item_name):
    """
    """ 
    return item_name in DICT_ITEMS.keys()


def item_description(item_name):
    """
    """
    return DICT_ITEMS[item_name].description