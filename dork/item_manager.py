"""
A module that handles the functionality of items
"""
from items import Item
dict_items ={ }

def assembling_items(names, descriptions, properties):
    """
    Constructs item objects for all items in game and stores all the items
    inside a dictionary
    """
    scope = range(len(names))
    for i in scope:
        item = Item(names[i], descriptions[i], properties[i])
        dict_items.update({item.name: item})
