"""
A module that handles the functionality of rooms
"""
from dork.rooms import Room
DICT_ROOMS = {}
DICT_DESCRIPTIONS = {}


def assembling_rooms(names, neighbors, doors, items):
    """
    Constructs room objects for all rooms in maze and stores all the rooms
    inside a dictionary.

    Parameters:
        names(list): A list that contains all the rooms
        neighbors(list): A list that contains all the neighbors of a room
        doors(list): A list that contains all the doors of a room
        items(list): A list that contains all the items of a room
    """
    scope = range(len(names))
    for i in scope:
        room = Room(names[i], neighbors[i], doors[i], items[i])
        DICT_ROOMS.update({room.name: room})


def assembling_descriptions(names, descriptions):
    """
    Adds the room descriptions for all rooms inside a dictionary.

    Parameters:
        names(list): A list that contains all the rooms
        descriptions(list): A list that contains all the
            descriptions of the rooms
    """
    scope = range(len(names))
    for i in scope:
        DICT_DESCRIPTIONS.update({names[i]: descriptions[i]})


def current_room(room_name):
    """
    The current room the player is in.

    Parameters:
        room_name(string): Name of a room

    Return:
        dict: Return the current room that the player is in
    """
    return DICT_ROOMS[room_name]


def room_description(room_name):
    """
    Returns description of current room

    Parameters:
        room_name(string): Name of a room

    Returns:
        dict: Return the description of the gaven room
    """
    return DICT_DESCRIPTIONS[room_name]


def items_in_room(room_name):
    """
    Returns dictionary of items in room

    Parameters:
        room_name(string): Name of a room

    Returns:
        dict: Return dictionary of items of the gaven room
    """
    return DICT_ROOMS[room_name].items


def is_item_in_room(room_name, item_name):
    """
    Retruns if item is in room

    Parameters:
        room_name(string): Name of a room
        item_name(string): Name of an item

    Returns:
        bool: Return true if the item is in the room. Return false otherwise.
    """
    return item_name in items_in_room(room_name)


def append_item(room_name, item_name):
    """
    Adds item to a room

    Parameters:
        room_name: Name of the room where the player is in
        item_name: Name of the item that the player droped off

    Returns:
        dict: Return the items of the gaven room after the player drop an item
    """
    return DICT_ROOMS[room_name].add_item(item_name)


def delete_item(room_name, item_name):
    """
    Deletes item from room

    Parameters:
        room_name(string): Name of the room where the player is in
        item_name(string): Name of the item that the player picked up

    Returns:
        dict: Return the items of the gaven room after
            the player pick up an item
    """
    return DICT_ROOMS[room_name].delete_item(item_name)


def not_empty_room(room_name):
    """
    Checks if room is empty

    Parameters:
        room_name: Name of a room

    Returns:
        bool: Return true if the room has items in it. Return false otherwise.
    """
    return len(items_in_room(room_name)) != 0


def to_string_current_items(name):
    """
    Returns a string that lists the items in the selected room

    Parameters:
        name(list): A list that contains all the items

    Returns:
        item_list: Return a string  that lists the imtems of the gaven room
    """
    item_list = 'You notice the following items--- '
    scope = range(len(DICT_ROOMS[name].items)-1)
    for i in scope:
        item_list += DICT_ROOMS[name].items[i] + ', '
    item_list += DICT_ROOMS[name].items[-1] + '.'
    return item_list


def move(cardinal, name):
    """
    Returns the current room of the player after the player moves
    a certain direction.

    Parameters:
        cardifnal(list): A list that contains all the cardinals of a room
        name(list): A list that contains all the rooms

    Returns:
        current_room_name: Return the current room after the player
            moves a certain direction
    """
    current_room_name = None
    if current_room(name).has_closed_door(cardinal):
        print('Closed door')
    elif not current_room(name).has_neighbor(cardinal):
        print('No neighbor')
    else:
        current_room_name = current_room(name).neighbors[cardinal]
    return current_room_name


def open_door(room_name, cardinal, key):
    """
    Used to open rooms

    Parameters:
    room_name: Name of a room
    cardinal(list): A list that contains the cardinals of a room
    key(list): A list that contains all the keys

    Returns:
    dict: Return the room with the closed door opened
        if there is a matching key
    Print a message to the user when there is no closed door or no matching key
    """
    if current_room(room_name).has_closed_door(cardinal):
        door_status = DICT_ROOMS[room_name].get_door_status(cardinal)
        if door_status == key:
            return DICT_ROOMS[room_name].update_door_status()
        return 'Invalid key for door at ' + cardinal + '!'
    return 'There is no closed door at the ' + cardinal + '!'


def __rooms_yaml_representation():
    """
    Creates a yaml friendly representation of the set of rooms

    Returns:
    rooms_repr(dict): Returns dictionary that contains all the rooms
    """
    rooms = {}
    rooms_repr = {'Rooms': rooms}
    for room_obj in list(DICT_ROOMS.values()):
        rooms.update(room_obj.yaml_representation())
    return rooms_repr


def __description_yaml_representation():
    """
    Creates a yaml friendly representation of the set of descriptions

    Returns:
    descrip_repr(dict): Returns dictionary that contains
        all the descriptions of rooms
    """
    descrip_repr = {'Rooms Descriptions': DICT_DESCRIPTIONS}
    return descrip_repr


def map_yaml_representation():
    """
    Creates a yaml friendly representation of the room with descriptions

    Returns:
    map_representation(dict): Return dictionary that contains
        all the rooms with the description
    """
    map_representation = {}
    map_representation.update(__rooms_yaml_representation())
    map_representation.update(__description_yaml_representation())
    return map_representation
