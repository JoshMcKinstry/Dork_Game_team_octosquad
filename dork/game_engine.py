"""
A module that works as an interface between the main classes in the game.
"""
import dork.incoming_data as game_data
import dork.item_manager as item_m
import dork.room_manager as room_m
import dork.character_manager as char_m
import dork.yamlreader as reader
import dork.yamlloader as loader


def game_loader(path):
    """
    Methods that validates the yaml file path, and if valid
    it loads the game from the CLI.

    Parameters:
        path(str): A String that contains the file path to the yaml file.

    Returns:
        bool: Returns true if file path is valid.
            Returns false if file path is invalid.
    """
    data = reader.reading_yml(path)
    if data is not None:
        loading_map(data)
        loading_items(data)
        loading_player(data)
        print("Game Successfully Loaded.")
        room_to_screen()
        return True
    print("Invalid path for save file.")
    return False


def loading_map(data):
    """
    Loads the map of the game. All the rooms are created along with their
    neighboring rooms, doors, descriptions, and items.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game in regard to rooms.
    """
    names = game_data.load_rooms(data)
    neighbors = game_data.load_cardinals(data, names)
    doors = game_data.load_doors(data, names)
    descriptions = game_data.load_room_descrips(data, names)
    items = game_data.load_list_room_items(data, names)
    room_m.assembling_rooms(names, neighbors, doors, items)
    room_m.assembling_descriptions(names, descriptions)


def loading_items(data):
    """
    Loads the items of the game. All the items are created along with their
    names, properties, and descriptions.

    Parameters:
        data(dict): Nested dictionaries containing
            all information of the game in regard to items.
    """
    names = game_data.load_items(data)
    descriptions = game_data.load_items_descriptions(data, names)
    properties = game_data.load_items_properties(data, names)
    item_m.assembling_items(names, descriptions, properties)


def loading_player(data):
    """
    Loads the player specifications. The player is created along with his
    position and inventory.

    Parameters:
        data(tuple): A tuple containing the player position and inventory.
    """
    (position, inventory) = game_data.load_player(data)
    char_m.assembling_player(position, inventory)


def saving():
    """
    Saving your progress at any given time as a yaml file.
    """
    saved_data = {}
    saved_map = room_m.map_yaml_representation()
    saved_items = item_m.items_yaml_representation()
    saved_char = char_m.player_yaml_representation()
    saved_data.update(saved_map)
    saved_data.update(saved_char)
    saved_data.update(saved_items)
    loader.writing_yml(saved_data, './dork/state files/last_checkpoint.yml')


def user_command(command):
    """
    Perform the method calls to play the game via a dictionary.

    Parameters:
        command(tuple): Tuple containing a verb, an object, and a target.
    """
    commands_lib = {"move": move, "open": use_key, "take": pick_up,
                    "drop": drop, "use": use_key, "examine": examine,
                    "display": display_inventory,
                    "where": room_to_screen}
    no_args = ["where", "display"]
    one_target = ["move"]
    one_obj = ["examine", "take", "drop"]
    two_args = ["open", "use"]
    (verb, obj, target) = command
    if verb in two_args and not (obj == '' or target == ''):
        commands_lib[verb](target, obj)
    elif verb in one_target and target != '':
        commands_lib[verb](target)
    elif verb in one_obj and obj != '':
        commands_lib[verb](obj)
    elif verb in no_args:
        commands_lib[verb]()
    else:
        print('Invalid Command')
        print("Try 'help' for more options")


def __current_position():
    """
    Returns the player current position.

    Returns:
        str: String description of current location.
    """
    return char_m.player_position()


def display_inventory():
    """
    Prints the current player inventory.
    """
    print(char_m.player_inventory())


def room_to_screen():
    """
    Prints the room name, room description and room items.
    """
    print('**' + __current_position() + '**')
    print(room_m.room_description(__current_position()))
    if room_m.not_empty_room(__current_position()):
        print(room_m.to_string_current_items(__current_position()))


def move(cardinal):
    """
    Moves the player from one room to another if room exists and door is
    open.

    Parameters:
        cardinal(str): String that points to a valid cardinal.
            i.e {North, East, South, West}
    """
    room_before_mov = __current_position()
    room_after_mov = room_m.move(cardinal, room_before_mov)
    if room_after_mov is None:
        print('No movement was made!')
    else:
        char_m.update_player_position(room_after_mov)
        room_to_screen()


def examine(item_name):
    """
    Prints a detailed description of an item.

    Parameters:
        item_name(str): Name of item in dictionary.
    """
    valid_item = item_m.is_item(item_name)
    item_in_room = room_m.is_item_in_room(__current_position(), item_name)
    item_in_inventory = char_m.player_has_item(item_name)

    if valid_item and (item_in_room or item_in_inventory):
        print(item_m.item_description(item_name))
    else:
        print('No item called ' + item_name + ' is available at the moment.')


def pick_up(item_name):
    """
    Picks up items from current room.

    Parameters:
        item_name(str): String description of name of item to be picked up.
    """
    (message, picked_up) = room_m.delete_item(__current_position(), item_name)
    if picked_up:
        print(char_m.update_player_inventory(item_name))
        print(message)
    else:
        print(message)


def drop(item_name):
    """
    Drops items into current room.

    Parameters:
        item_name(str): String description of name of item to be dropped.
    """
    (message, dropped) = char_m.remove_item_from_inventory(item_name)
    if dropped:
        print(message)
        print(room_m.append_item(__current_position(), item_name))
    else:
        print(message)


def use_key(cardinal, key):
    """
    Player uses key at a door in a given cardinal,
    if key and cardinal match, method will open the door.

    Parameters:
        cardinal(str): String that points to a valid cardinal.
            i.e {North, East, South, West}
        key(str): String that represents the name of the key.
    """
    if char_m.player_has_item(key):
        print(room_m.open_door(__current_position(), cardinal, key))
    else:
        print('You do not have ' + key + ' in your inventory')
