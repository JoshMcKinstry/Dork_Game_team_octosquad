"""REPL and commands parser for dork game
"""
import sys
from dork.room_printing import Room1Printing

PLAYER_ROOM = "room 1"


def _start_game():
    return "Welcome to Dork!", False


def _quit_game():
    return "Leaving the game of Dork.", True


def move_east():
    """Interprets print statement for moving east based on location
    """
    # return "you have moved east", False
    Room1Printing.print_move(PLAYER_ROOM, "east")
    return "", False


def move_west():
    """Interprets print statement for moving west based on location
    """
    Room1Printing.print_move(PLAYER_ROOM, "west")
    return "", False


def move_north():
    """Interprets print statement for moving north based on location
    """
    Room1Printing.print_move(PLAYER_ROOM, "north")
    return "", False


def move_south():
    """Interprets print statement for moving south based on location
    """
    Room1Printing.print_move(PLAYER_ROOM, "south")
    return "", False


def get_item():
    """Interprets print statement for south based on location
    """
    return "you picked up an item", False


def use_item():
    """Logic for using an item based on inventory
    """
    return "you used an item", False


def look_east():
    """Interprets print statement for looking east based on location
    """
    Room1Printing.print_look(PLAYER_ROOM, "east")
    return "", False


def look_west():
    """Interprets print statement for looking west based on location
    """
    Room1Printing.print_look(PLAYER_ROOM, "west")
    return "", False


def look_north():
    """Interprets print statement for looking north based on location
    """
    Room1Printing.print_look(PLAYER_ROOM, "north")
    return "", False


def look_south():
    """Interprets print statement for looking south based on location
    """
    Room1Printing.print_look(PLAYER_ROOM, "south")
    return "", False


def drop():
    """Interprets logic for dropping an item
    """
    return "you dropped an item", False


def read():
    """read input from console to repl
    """
    return input("> ")


def evaluate(command):
    """command evaluating method in repl
    """
    # https://docs.python.org/3/tutorial/datastructures.html
    words_in_command = [words.casefold() for words in command.split()]
    player_commands = {
        "go": {
            "north": move_north,
            "south": move_south,
            "west": move_west,
            "east": move_east
        },
        "get": {"object": get_item},
        "use": {"object": use_item},
        "look": {
            "north": look_north,
            "south": look_south,
            "west": look_west,
            "east": look_east
        },
        "drop": {"object": drop}
    }
    game_commands = {
        "start": {"dork": _start_game},
        "quit": {"dork": _quit_game}
    }
    for word in words_in_command:
        if word in player_commands:
            sub_menu = player_commands[word]
            for sub_word in words_in_command:
                if sub_word in sub_menu:
                    function = sub_menu[sub_word]
                    return function()
        elif word in game_commands:
            sub_menu = game_commands[word]
            for sub_word in words_in_command:
                if sub_word in sub_menu:
                    function = sub_menu[sub_word]
                    return function()
    return "Unknown Command", False


def repl():
    """repl for dork game
    """
    print("Welcome to Dork!")
    while True:
        command = read()
        output, should_exit = evaluate(command)
        print(output)
        if should_exit:
            break
    print("ending repl...")


def init():
    """initializer function
    """
    if __name__ == "__main__":
        sys.exit(repl())


init()