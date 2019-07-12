"""
A module that loads and validate the game data.
"""

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

def check_rooms(room_names):
    """
    Checking room names for valid names
    """
    return None in room_names


def check_cardinals(room_cardinals):
    """
    Checking for valid cardinals in each room
    """
    valid_cardinals = ['north', 'east', 'south', 'west']
    invalid_cardinal = False
    scope = range(len(room_cardinals))
    for i in scope:
        if set(room_cardinals[i].keys()) != set(valid_cardinals):
            invalid_cardinal = True
            break
    return invalid_cardinal


def no_null_cardinal(room_cardinals):
    """
    Removing null cardinals for validation
    """
    scope = range(len(room_cardinals))
    for i in scope:
        adjacent_rooms = list(room_cardinals[i].values())
        adjacent_rooms[:] = (
            room for room in adjacent_rooms if room is not None)
    return adjacent_rooms


def check_connections(room_names, room_cardinals):
    """
    Checking for cardinals to be pointing to unique and valid directions
    """
    dual_pointer = False
    invalid_direction = False
    isolated_room = False
    scope = range(len(room_cardinals))
    for i in scope:
        adjacent_rooms = list(room_cardinals[i].values())
        adjacent_rooms[:] = (
            room for room in adjacent_rooms if room is not None)
        unique_rooms = set(adjacent_rooms)
        if len(adjacent_rooms) != len(unique_rooms):
            dual_pointer = True
            break
        elif not set(adjacent_rooms).issubset(set(room_names)):
            invalid_direction = True
            break
        elif unique_rooms.issubset({None}):
            isolated_room = True
            break
    return dual_pointer or invalid_direction or isolated_room
