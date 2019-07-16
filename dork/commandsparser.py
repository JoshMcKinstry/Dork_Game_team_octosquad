"""REPL and commands parser for dork game
"""

import sys
from enum import Enum
from dork import game_engine as ge

COMMANDLIST = ["help", "load", "save", "quit",
               "move", "open", "take", "look", "use", "eat"]
CARDINALS = ['north', 'east', 'south', 'west']
# will integrate with game_engine later so items can be loaded dynamically
OBJECTS = ['cage', 'cellphone', 'dean badge', 'donut', 'flower', 'flyer', 'freshman badge',
           'junior badge', 'key', 'nest', 'paper', 'sophomore badge']
TARGETS = ['door', 'dean', 'cage']



def read():
    """read input from console to repl
    """
    return input("> ")


def menu_evaluate(tokens):
    """token evaluater for the main menu state
    """
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
    """token evaluater for the in-game state
    """
    action = ""
    obj = ""
    target = ""
    targets = TARGETS + OBJECTS
    # help load save quit
    # move open take look use eat
    for token in tokens:
        if token in COMMANDLIST:
            action = token
        elif token in OBJECTS:
            obj = token
        elif token in CARDINALS or token in targets:
            target = token
    print()


def load_evaluate(tokens):
    print("Select a save game and hit enter to start!")


def save_evaluate(tokens):
    print()


def quit_dork():
    print("Leaving Dork...\n\n")
    sys.exit()


def evaluate(command, state):
    """command evaluating method in repl
    """
    # https://docs.python.org/3/tutorial/datastructures.html
    word_list = [words.casefold() for words in command.split()]
    if state == State.MENU:
        return menu_evaluate(word_list)
    if state == State.GAME:
        return game_evaluate(word_list)
    if state == State.LOAD:
        return load_evaluate(word_list)
    if state == State.SAVE:
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
