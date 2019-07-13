"""
A module that works as an interface between the main classes in the game
"""
import incoming_data as game_data
import item_manager as item_m
import room_manager as room_m
import character_manager as char_m
import yamlreader as reader


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


def loading_item(data):
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
    player = game_data.load_player(data)
    char_m.assembling_player(player[0], player[1])


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
        print('No item called ' + item_name + ' is available at the moment.' )


def pick_up(item_name):
    """
    Picks up items from current room
    """
    (not_in_room, picked_up) = room_m.delete_item(__current_position(), item_name)

    if picked_up:
        print(char_m.update_player_inventory(item_name))
    else:
        print(not_in_room)


if __name__ == "__main__":
    PATH = 'C:\\CS 3250 Individual Repository\\Team 34 Repository\\team34\dork\\game.yml'
    DATA = reader.reading_yml(PATH)
    loading_map(DATA)
    loading_item(DATA)
    loading_player(DATA)
    room_to_screen()
    pick_up('Paper')
    pick_up('Cage')
    move('West')
    pick_up('Flower')
    move('West')
    display_inventory()
    move('East')
    move('East')
    examine('Paper')
    examine('Cage')
    examine('Freshman Badge')