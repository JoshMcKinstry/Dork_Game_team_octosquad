"""REPL and commands parser for dork game
"""
import sys
from enum import Enum
from dork import game_engine as ge

DIRECTIONS = "[direction] --> north\n\
                east\n\
                south\n\
                west\n"
COMMANDDICT = {"help": "---HELP---\n\
Prints a helper list of commands.\n\
USAGE: 'help'\n\
       'help' [command]\n",
               "load": "---LOAD---\n\
Load the last saved checkpoint.\n\
USAGE: 'load'\n",
               "save": "---SAVE---\n\
Save the game. Overrides last save.\n\
USAGE: 'save'\n",
               "quit": "---QUIT---\n\
Return to the Dork Main Menu. Saving game is optional\n\
USAGE: 'quit'\n",
               "move": "---MOVE---\n\
Move between rooms in the Dork Game.\n\
USAGE: 'move' [direction]\n{}".format(DIRECTIONS),
               "open": "---OPEN---\n\
Open a locked door in the Dork Game.\n\
USAGE: 'open' [direction] with [item]\n{}\
see also - 'help use'\n".format(DIRECTIONS),
               "take": "---TAKE---\n\
Pick up an item that is in the room.\n\
USAGE: 'take' [item]\n",
               "drop": "---DROP---\n\
Drop an item that is in your inventory.\n\
USAGE: 'drop' [item]",
               "examine": "---EXAMINE---\n\
Inspect an item.\n\
USAGE: 'examine' [item]",
               "use": "---USE---\n\
Use a key on a door.\n\
USAGE: 'use' [item] on [direction]\n{}\
see also - 'help open'\n".format(DIRECTIONS), }
CARDINALS = ['north', 'east', 'south', 'west']
OBJECTS = ['cage', 'cellphone', 'dean-badge', 'donut',
           'flower', 'flyer', 'freshman-badge',
           'junior-badge', 'key', 'nest', 'paper', 'sophomore-badge']


def read():
    """read input from console to repl
    """
    return input("> ")


def safe_quit():
    """
    Leaving the game
    """
    print("Would you like to save the game?(y/n)")
    response = input(">").casefold()
    if response == "y":
        return State.SAVE
    if response == "n":
        print("Returning to Main Menu.")
        return State.MENU
    print("Invalid Response.\nReturning to Game")
    return State.GAME


def quit_dork():
    '''
    Quitting Dork
    '''
    print("Leaving Dork...\n\n")
    sys.exit()


def print_load():
    """
    Print Load
    """
    print("Loading previous checkpoint...")


def print_menu():
    """
    Print Menu
    """
    print("Welcome to the Game of Dork!\n\
        -- NEW\n\
        -- LOAD\n\
        -- HELP\n\
        -- INFO\n\
        -- QUIT")


def print_info():
    """
    Print Info
    """
    print("-----------------------------------------------------\n\
        What is Dork?\n\
        Dork is an interactive text-based adventure game that takes place\n\
        in MSU Denver in the year 2040, where a new dean has been initiated\n\
        into office. The dean has been known for his hatred of birds,\n\
        hunting them for fun and putting them into cages around the campus.\n\
        He caught a roadrunner and plans to give it to exterminators.\n\
        It`s up to you to save MSU Denver's mascot.")


def game_helper(command):
    """
    Helper Command
    """
    if not command:
        print(COMMANDDICT["help"])
        print("List of in game commands.")
        for commands in COMMANDDICT:
            print(commands)
    else:
        print(COMMANDDICT[command])


def evaluate(command, state):
    """command evaluating method in repl
    """
    # https://docs.python.org/3/tutorial/datastructures.html
    word_list = [words.casefold() for words in command.split()]
    if state == State.MENU:
        function = menu_evaluate(word_list)
    if state == State.GAME:
        function = game_evaluate(word_list)
    if state == State.LOAD:
        function = load_evaluate(command)
    if state == State.SAVE:
        function = save_evaluate()
    return function


def load_evaluate(path):
    """token evaluater for the load screen state
    """
    if ge.game_loader(path):
        return State.GAME
    return State.MENU


def save_evaluate():
    """
    Saving State
    """
    print("Saving Game...")
    ge.saving()
    return State.MENU


def menu_evaluate(tokens):
    """token evaluater for the main menu state
    """
    if "quit" in tokens:
        quit_dork()
    if "load" in tokens:
        return State.LOAD
    if "help" in tokens:
        print("Main Menu Commands for Dork")
        print("help - Print a list of commands.")
        print("load - Load a game save file from available saves.")
        print("new - Start a new game on a fresh save file.")
        print("quit - Exits the game of 'Dork'.")
        return State.MENU
    if "new" in tokens:
        print("\nStarting the game of 'Dork'.\n")
        return evaluate("./dork/state files/game.yml", State.LOAD)
    if "info" in tokens:
        print_info()
        return State.MENU
    print("Please input a valid command!\nTry 'help' for more options.")
    return State.MENU


def game_evaluate(tokens):
    """token evaluater for the in-game state
    """
    action = ""
    obj = ""
    target = ""
    for token in tokens:
        if token in COMMANDDICT and not action:
            action = token
        elif token in OBJECTS:
            obj = token
        elif token in CARDINALS or token in COMMANDDICT:
            target = token
    if not action:
        print("Please provide a command)\n")
        print("Try 'help' for a list of available commands.")
        return State.GAME
    if action == "quit":
        return safe_quit()
    if action == "save":
        return State.SAVE
    if action == "load":
        return State.LOAD
    if action == "help":
        game_helper(target)
        return State.GAME
    ge.user_command((action, obj.title(), target.title()))
    return State.GAME


def repl():
    """repl for dork game
    """
    state = State.MENU
    _print_menu()
    while True:
        command = read()
        state = evaluate(command, state)
        if state == State.QUIT:
            _quit_dork()
        if state == State.LOAD:
            _print_load()
        if state == State.MENU:
            print_menu()


class State(Enum):
    """State tracker for the game
    """
    MENU = 1
    GAME = 2
    LOAD = 3
    SAVE = 4
    QUIT = 5
