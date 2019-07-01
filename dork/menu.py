'''
A menu that handles loading and creating files to
manage user progress in the game.
'''
import yamlloader as writer
import yamlreader as reader
import mapvalidation as validmap


def new_game():
    '''
    Starting a new game
    '''

    data = reader.reading_yml('new_game.yml')
    room_names = validmap.load_rooms(data)
    room_cardinals = validmap.load_cardinals(data)
    room_items = validmap.load_items(data)
    return (room_names, room_cardinals, room_items)


def get_saved_game():
    '''
    Getting a saved state file
    '''

    validated = True
    while validated:
        file_path = input('Type a file path for your saved state file:\n')
        is_file_path = reader.valid_file_path(file_path)
        is_yml = reader.valid_extension(file_path)
        validated = not is_file_path or not is_yml
        if validated:
            print('You must type a file path that points to a .yml file.')
    data = reader.reading_yml(file_path)
    return data


def saved_game():
    '''
    validating a saved state file
    '''

    validated = True
    while validated:
        data = get_saved_game()
        room_names = validmap.load_rooms(data)
        room_cardinals = validmap.load_cardinals(data)
        room_items = validmap.load_items(data)
        invalid_1 = validmap.check_rooms(room_names)
        invalid_2 = validmap.check_cardinals(room_cardinals)
        invalid_3 = validmap.check_connections(room_names, room_cardinals)
        validated = invalid_1 or invalid_2 or invalid_3
        if validated:
            print('Invalid data, please upload another file.')
    return (room_names, room_cardinals, room_items)


def saving_progress():
    '''
    saving progress to a .yml file
    '''

    player = {'Position': 'Boss', 'Health': '100', 'Inventory': None}
    boss_items = {'Sword': True, 'Shield': False}
    boss_car = {'north': None, 'east': None, 'south': 'Cave', 'west': None}
    boss_room = {'Neighbors': boss_car, 'Items': boss_items}
    cave_items = {'Sword': False, 'Shield': True}
    cave_car = {'north': 'Boss', 'east': None, 'south': None, 'west': None}
    cave_room = {'Neighbors': cave_car, 'Items': cave_items}
    game = {'Boss': boss_room, 'Cave': cave_room, 'Player': player}
    my_maze = {'State of Game': game}

    file_name = input('Type a name for your saving file:\n')
    file_name = file_name + '.yml'
    writer.writing_yml(my_maze, file_name)

    
if __name__ == "__main__":
    import menu
    NEW_GAME = menu.new_game()
    print(NEW_GAME)
    SAVED = menu.saved_game()
    print(SAVED)
    menu.saving_progress()
