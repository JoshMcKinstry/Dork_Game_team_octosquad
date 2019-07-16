"""REPL and commands parser for dork game
"""

import sys
from enum import Enum
from dork import game_engine


'''def _start_game(data):
    return "Welcome to Dork!", False


def _quit_game():
    return "Leaving the game of Dork.", True


def print_help():
    """Prints Main Menu
    """
    print("Dork")


def load(command):
    """Logic for interpreting the game yaml to start
    """
    if command is not None:
        _start_game(command)
    else:
        _start_game('.\\dork\\game.yml')


def move_east():
    """Interprets print statement for moving east based on location
    """
    # return "you have moved east", False
    game_engine.move("east")
    return "", False


def move_west():
    """Interprets print statement for moving west based on location
    """
    game_engine.move("west")
    return "", False


def move_north():
    """Interprets print statement for moving north based on location
    """
    game_engine.move("north")
    return "", False


def move_south():
    """Interprets print statement for moving south based on location
    """
    game_engine.move("south")
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
    return "", False


def look_west():
    """Interprets print statement for looking west based on location
    """
    return "", False


def look_north():
    """Interprets print statement for looking north based on location
    """
    return "", False


def look_south():
    """Interprets print statement for looking south based on location
    """
    return "", False


def drop():
    """Interprets logic for dropping an item
    """
    return "you dropped an item", False


def show_inventory():
    """Displays the players inventory to the console from the games engine
    """
    game_engine.display_inventory()
    return "", False
'''

def read():
    """read input from console to repl
    """
    return input("> ")


def menu_evaluate(tokens):
    # new load help quit
    if "quit" in tokens:
        quit_dork()
    elif "load" in tokens:
        return State.LOAD
    elif "help" in tokens:
        print("Main Menu Commands for Dork")
        print("help - Print a list of commands.")
        print("load - Load a game save file from available saves.")
        print("new - Start a new game on a fresh save file.")
        print("quit - Exits the game of 'Dork'.")
        return State.MENU
    elif "new" in tokens:
        print("\nStarting the game of 'Dork'.\n")
        return State.GAME
    else:
        print("Please input a valid command!\nTry 'help' for more options.")
        return State.MENU


def game_evaluate(tokens):
    # help load save quit
    # move open take look use eat
    print()

def load_evaluate(tokens):
    print("Select a save game and hit enter to start!")


def save_evaluate(tokens):
    print()


def quit_dork():
    print("Leaving Dork...")
    sys.exit(0)

def evaluate(command, state):
    """command evaluating method in repl
    """
    # ['Paper', 'Cage', 'Freshman Badge', 'Flyer', 'Donut', 'Sophomore Badge', 'Flower', 'Nest', 'Junior Badge', 'Cellphone', 'Dean Badge', 'Key']
    # https://docs.python.org/3/tutorial/datastructures.html
    word_list = [words.casefold() for words in command.split()]
    if state == State.MENU:
        return menu_evaluate(word_list)
    elif state == State.GAME:
        return game_evaluate(word_list)
    elif state == State.LOAD:
        return load_evaluate(word_list)
    elif state == State.SAVE:
        return save_evaluate(word_list)


def repl():
    """repl for dork game
    """
    state = State.MENU
    print("Welcome to Dork!")
    while True:
        command = read()
        state = evaluate(command, state)
        if state == State.QUIT:
            quit_dork()

class State(Enum):
    """State tracker for the game
    """
    MENU = 1
    GAME = 2
    LOAD = 3
    SAVE = 4
    QUIT = 5
