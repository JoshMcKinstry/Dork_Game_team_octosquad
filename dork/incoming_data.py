"""
A module that loads the game information
"""
import yamlreader as reader

def load_rooms(data):
    """
    Loading the room names
    """
    room_names = list(data['Rooms'].keys())
    return room_names


def load_cardinals(data, room_names):
    """
    Loading the room cardinals
    """
    room_cardinals = []
    for name in room_names:
        cardinal = data['Rooms'][name]['Neighbors']
        room_cardinals.append(cardinal)
    return room_cardinals


def load_doors(data, room_names):
    """
    Loading the doors in each room
    """
    room_doors = []
    for name in room_names:
        door = data['Rooms'][name]['Door']
        room_doors.append(door)
    return room_doors


def load_room_descrips(data, room_names):
    """
    Loading each room respective main description
    """
    room_descrips = []
    for name in room_names:
        descrip = data['Rooms'][name]['Description']
        room_descrips.append(descrip)
    return room_descrips


def load_list_room_items(data, room_names):
    """
    Loading each room respective list of items
    """
    items_list = []
    for name in room_names:
        item_list = data['Rooms'][name]['Items']
        items_list.append(item_list)
    return items_list


def load_items(data):
    """
    Loading items into the game
    """
    items_name = list(data['Items'].keys())
    return items_name


def load_items_descriptions(data, items_name):
    """
    Loading each item respective description
    """
    item_descriptions = []
    for name in items_name:
        description = data['Items'][name]['Description']
        item_descriptions.append(description)
    return item_descriptions


def load_items_properties(data, items_name):
    """
    Loading each item respective properties
    """
    item_properties = []
    for name in items_name:
        attribute = data['Items'][name]['Properties']
        item_properties.append(attribute)
    return item_properties


def load_player(data):
    """
    Loading the player specs
    """
    player_specs = (data['Player']['Position'], data['Player']['Inventory'])
    return player_specs


def load_characters(data):
    """
    Loading the character names into the game
    """
    character_names = list(data['Characters'].keys())
    return character_names


if __name__ == "__main__":
    PATH = 'C:\\CS 3250 Individual Repository\\Team 34 Repository\\team34\dork\\game.yml'
    DATA = reader.reading_yml(PATH)
