"""
A module that works as an interface between the main classes in the game
"""
import dork.incoming_data as game_data
import dork.item_manager as item_m
import dork.room_manager as room_m
import dork.character_manager as char_m


def loading_map(data):
    """
    Loads the map of the game. All the rooms are created along with their
    neighboring rooms, doors, descriptions, and items.
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
    Loads all the items available for the game.
    """
    names = game_data.load_items(data)
    descriptions = game_data.load_items_descriptions(data, names)
    properties = game_data.load_items_properties(data, names)
    item_m.assembling_items(names, descriptions, properties)


def loading_player(data):
    """
    Load the player specs to the game
    """
    (position, inventory) = game_data.load_player(data)
    char_m.assembling_player(position, inventory)


def __current_position():
    """
    Returns the player current position
    """
    return char_m.player_position()


def display_inventory():
    """
    Prints the current player inventory
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
    Prints a detailed description of an item
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
    Picks up items from current room
    """
    (message, picked_up) = room_m.delete_item(__current_position(), item_name)
    if picked_up:
        print(char_m.update_player_inventory(item_name))
        print(message)
    else:
        print(message)


def drop(item_name):
    """
    Drops items into current room
    """
    (message, dropped) = char_m.remove_item_from_inventory(item_name)
    if dropped:
        print(message)
        print(room_m.append_item(__current_position(), item_name))
    else:
        print(message)


def use_key(cardinal, key):
    """
    Player uses the key which opens the door in their current room if they
    have the right key.
    """
    if char_m.player_has_item(key):
        print(room_m.open_door(__current_position(), cardinal, key))
    else:
        print('You do not have ' + key + ' in your inventory')
