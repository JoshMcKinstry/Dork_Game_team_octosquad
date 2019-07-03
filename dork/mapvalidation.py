"""
A class that validates a maze coming from a .yml/.yaml file
"""


def load_rooms(maze):
    """
    Loading the room names
    """
    for room_name in maze:
        room_names = list(maze[room_name].keys())
    del room_names[-1]
    return room_names


def load_cardinals(maze):
    """
    Loading the room cardinals
    """
    room_cardinals = []
    for room_name in maze:
        room_specs = list(maze[room_name].values())
    scope = range(len(room_specs)-1)
    for i in scope:
        neighbors_dict = room_specs[i]['Neighbors']
        room_cardinals.append(neighbors_dict)
    return room_cardinals


def load_items(maze):
    """
    Loading the room items
    """
    room_items = []
    for room_name in maze:
        room_specs = list(maze[room_name].values())
    scope = range(len(room_specs)-1)
    for i in scope:
        items_dict = room_specs[i]['Items']
        room_items.append(items_dict)
    return room_items


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
