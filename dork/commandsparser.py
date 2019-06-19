"""REPL and commands parser for dork game
"""
import sys


def _start_game():
    return "Welcome to Dork!", False


def _quit_game():
    return "Leaving the game of Dork.", True


def _move_east():
    return "you have moved east", False


def _move_west():
    return "you have moved west", False


def _move_north():
    return "you have moved north", False


def _move_south():
    return "you have moved south", False


def _get_item():
    return "you picked up an item", False


def _use_item():
    return "you used an item", False


def _look():
    return "you are in an empty room", False


def _open():
    return "you opened a door", False


def _drop():
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
            "north": _move_north,
            "south": _move_south,
            "west": _move_west,
            "east": _move_east
        },
        "get": {"object": _get_item},
        "use": {"object": _use_item},
        "look": {"around": _look},
        "open": {"object": _open},
        "drop": {"object": _drop}
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
    print("starting repl...")
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
