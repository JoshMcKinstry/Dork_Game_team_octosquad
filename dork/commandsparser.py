"""REPL and commands parser for dork game
"""
import sys
from enum import Enum
from dork import game_engine as ge

COMMANDLIST = ["help", "load", "save", "quit",
               "move", "open", "take", "drop", "examine", "use", "eat"]
CARDINALS = ['north', 'east', 'south', 'west']
# will integrate with game_engine later so items can be loaded dynamically
OBJECTS = ['cage', 'cellphone', 'dean-badge', 'donut',
           'flower', 'flyer', 'freshman-badge',
           'junior-badge', 'key', 'nest', 'paper', 'sophomore-badge']


def read():
    """read input from console to repl
    """
    return input("> ")


def _menu_evaluate(tokens):
    """token evaluater for the main menu state
    """
    # new load help quit
    if "quit" in tokens:
        _quit_dork()
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
        evaluate("./dork/state files/game.yml", State.LOAD)
        return State.GAME
    else:
        print("Please input a valid command!\nTry 'help' for more options.")
        return State.MENU


def _game_evaluate(tokens):
    """token evaluater for the in-game state
    """
    action = ""
    obj = ""
    target = ""
    for token in tokens:
        if token in COMMANDLIST:
            action = token
        elif token in OBJECTS:
            obj = token
        elif token in CARDINALS:
            target = token
    if not action:
        print("Please provide a command.")
        return State.GAME
    if action == "quit":
        return _safe_quit()
    if action == "save":
        return State.SAVE
    if action == "load":
        return State.LOAD
        #Validation Needed For Objects Objects and Targets
    ge.user_command((action, obj.title(), target.title()))
    return State.GAME


def _load_evaluate(path):
    """token evaluater for the load screen state
    """
    if ge.game_loader(path):
        return State.GAME
    return State.MENU


def _save_evaluate():
    ge.saving()
    return State.GAME


def _safe_quit():
    print("Would you like to save the game?")
    response = input("y/n\n>")
    if response == "y":
        return State.SAVE
    else:
        return State.MENU


def _quit_dork():
    print("Leaving Dork...\n\n")
    sys.exit()


def _print_load():
    print("Select a save game and hit enter to start!")


def evaluate(command, state):
    """command evaluating method in repl
    """
    # https://docs.python.org/3/tutorial/datastructures.html
    word_list = [words.casefold() for words in command.split()]
    if state == State.MENU:
        return _menu_evaluate(word_list)
    if state == State.GAME:
        return _game_evaluate(word_list)
    if state == State.LOAD:
        return _load_evaluate(command)
    if state == State.SAVE:
        return _save_evaluate()


def repl():
    """repl for dork game
    """
    state = State.MENU
    print("Welcome to Dork!")
    while True:
        command = read()
        state = evaluate(command, state)
        if state == State.QUIT:
            _quit_dork()
        if state == State.LOAD:
            _print_load()


class State(Enum):
    """State tracker for the game
    """
    MENU = 1
    GAME = 2
    LOAD = 3
    SAVE = 4
    QUIT = 5
