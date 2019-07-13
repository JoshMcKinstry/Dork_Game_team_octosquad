"""
A module that works as an interface between the main classes in the game
"""
import incoming_data as game_data
import item_manager as item_m
import room_manager as room_m
import yamlreader as reader
from player import Player

DICT_PLAYERS = {}

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

def loading_players():
    """
    """
    user = Player('User', 'Entrance', ['Cage', 'Lamp', 'Gun'])
    DICT_PLAYERS.update({ user.name: user})


def current_player_position():
    """
    """
    print(DICT_PLAYERS['User'].position)


def move(cardinal):
    """
    Moves the player from one room to another if room exists and door is
    open.
    """
    room_before_mov = DICT_PLAYERS['User'].position
    room_after_mov = room_m.move(cardinal, room_before_mov)
    if room_after_mov is None:
        print('No movement was made!')
    else:
        DICT_PLAYERS['User'].position = room_after_mov
        print(room_m.current_description(room_after_mov))
        print(room_m.current_items(room_after_mov))

def use_item(item_name, action):
    """
    Anytime a player uses an item, the action and the item the action is
    executed on is called here.
    """
    pass


if __name__ == "__main__":
    data = reader.reading_yml('C:\Python Scripts\Yaml Loader\saved_progress.yml')
    loading_map(data)
    loading_item(data)
    loading_players()
    current_player_position()
    move('West')
    print('\n ')
    current_player_position()
    move('West')
    current_player_position()
    print('\n')
    