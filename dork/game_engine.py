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


def room_to_screen():
    """
    Prints the room name, room description and room items.
    """
    print('**' + __current_position() + '**')
    print(room_m.current_description(__current_position()))
    print('---' + room_m.to_string_current_items(__current_position()))


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


if __name__ == "__main__":
    PATH = 'C:\\CS 3250 Individual Repository\\Team 34 Repository\\team34\dork\\game.yml'
    DATA = reader.reading_yml(PATH)
    loading_map(DATA)
    loading_item(DATA)
    loading_player(DATA)
    room_to_screen()
    move('West')
