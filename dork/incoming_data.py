"""
A module that loads the game information from a yaml file.
"""


def load_rooms(data):
    """
    Loading the room names.

    Parameter:
        data(dict): Dictionary of all room names.

    Returns:
        room_names(list): Returns list of all room names.
    """
    room_names = list(data['Rooms'].keys())
    return room_names


def load_cardinals(data, room_names):
    """
    Loading the room cardinals.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game.
        room_names(list): List containg room names.

    Returns:
        room_cardinals(list): Returns list of room neighbors.
    """
    room_cardinals = []
    for name in room_names:
        cardinal = data['Rooms'][name]['Neighbors']
        room_cardinals.append(cardinal)
    return room_cardinals


def load_doors(data, room_names):
    """
    Loading the doors in each room.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game.
        room_names(list): List containg room names.

    Returns:
        room_doors(list): Returns list of room doors.
    """
    room_doors = []
    for name in room_names:
        door = data['Rooms'][name]['Door']
        room_doors.append(door)
    return room_doors


def load_room_descrips(data, room_names):
    """
    Loading each rooms respective main description.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game.
        room_names(list): List containg room names.

    Returns:
        room_descrips(list): Returns list of room descriptions.
    """
    room_descrips = []
    for name in room_names:
        descrip = data['Rooms Descriptions'][name]
        room_descrips.append(descrip)
    return room_descrips


def load_list_room_items(data, room_names):
    """
    Loading each room respective list of items.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game.
        room_names(list): List containg room names.

    Returns:
        items_list(list): Returns list of room items.
    """
    items_list = []
    for name in room_names:
        item_list = data['Rooms'][name]['Items']
        items_list.append(item_list)
    return items_list


def load_items(data):
    """
    Loading items into the game.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game.

    Returns:
        items_name(list): Returns list of item names.
    """
    items_name = list(data['Items'].keys())
    return items_name


def load_items_descriptions(data, items_name):
    """
    Loading each items respective description.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game.
        items_name(list): List of item names.

    Returns:
        items_descriptions(list): Returns list of item descriptions.
    """
    item_descriptions = []
    for name in items_name:
        description = data['Items'][name]['Description']
        item_descriptions.append(description)
    return item_descriptions


def load_items_properties(data, items_name):
    """
    Loading each items respective properties.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game.
        items_name(list): List of item names.

    Returns:
        items_descriptions(list): Returns list of item properties.
    """
    item_properties = []
    for name in items_name:
        attribute = data['Items'][name]['Properties']
        item_properties.append(attribute)
    return item_properties


def load_player(data):
    """
    Loading the player specs.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game.

    Returns:
        player_specs(tuple): Tuple of player specs.
    """
    player_specs = (data['Player']['Position'], data['Player']['Inventory'])
    return player_specs
