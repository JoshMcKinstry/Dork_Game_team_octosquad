'''
A module that parses commands via the REPL process
'''
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
see also - 'help open'\n".format(DIRECTIONS),
               "display": "---DISPLAY---\n\
Display the inventory of the player.\n\
USAGE: 'display'",
               "where": "---WHERE---\n\
Show where the player is at.\n\
USAGE: 'where'"}
CARDINALS = ['north', 'east', 'south', 'west']
OBJECTS = ['cage', 'cellphone', 'dean-badge', 'donut',
           'flower', 'flyer', 'freshman-badge',
           'junior-badge', 'key', 'nest', 'paper', 'sophomore-badge']


def read():
    """
    This function reads input from the console to the REPL

    Returns:
        input (str): The user's selection for the game state
    """
    return input("> ")


def _safe_quit():
    """
    This function ends the game with a possible save

    Parameters:
        response (str): The user's input whether or not to save
    
    Returns:
        State (enum): Token delegating the current game state
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


def _quit_dork():
    """
    This function ends the game immediately
    """
    print("Leaving Dork...\n\n")
    sys.exit()


def _print_load():
    """
    This prints a loading statement while the game loads
    """
    print("Loading previous checkpoint...")


def _print_menu():
    """
    This prints out the overall menu for the game
    """
    print("Welcome to the Game of Dork!\n\
        -- NEW\n\
        -- LOAD\n\
        -- HELP\n\
        -- INFO\n\
        -- QUIT")


def _print_info():
    """
    This prints out an informative statement on the game
    """
    print("-----------------------------------------------------\n\
        What is Dork?\n\
        Dork is an interactive text-based adventure game that takes place\n\
        in MSU Denver in the year 2040, where a new dean has been initiated\n\
        into office. The dean has been known for his hatred of birds,\n\
        usually hunting them for fun and putting them into cages\n\
        around the campus. He recently caught a roadrunner and plans\n\
        to give it to exterminators.\n\
        It's up to you to save MSU Denver's mascot.")


def _game_helper(command):
    """
    This function displays the helper list
        whenever a player enters an unknown command

    Parameters: 
        command (dict): A dictionary (of dictionaries) that contains the
            various actions possible in the game.  

    Returns:

    """
    if not command:
        print(COMMANDDICT["help"])
        print("List of in game commands.")
        for commands in COMMANDDICT:
            print(commands)
    else:
        print(COMMANDDICT[command])


def evaluate(command, state):
    """
    This function evaluates the current state of the game

    Parameters:
        state (str): A string indicating current state of the game
    
    Returns:
        State (enum): An enum which selects the correct state
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
    return None


def _load_evaluate(path):
    """
    This function evaluates the current game state
        and loads a new game if called upon
    
    Parameters: 
        path (str): The file location of the saved game

    Returns:
        State (enum): An enum which selects the correct state
    """
    if ge.game_loader(path):
        return State.GAME
    return State.MENU


def _save_evaluate():
    """
    This function prints a statement about saving a new game
        and then saves the game
    """
    print("Saving Game...")
    ge.saving()
    return State.MENU


def _menu_evaluate(tokens):
    """
    This function evalulates the command input by the user
        for the most basic of command options
        (the options available in the initial menu).

    Parameters:
        tokens (list): A list of possible input options by the user

    Returns:
        State (enum): An enum which selects the correct state
    """
    # new load help quit
    if "quit" in tokens:
        _quit_dork()
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
        _print_info()
        return State.MENU
    print("Please input a valid command!\nTry 'help' for more options.")
    return State.MENU


def _game_evaluate(tokens):
    """
    This function evalulates the command input by the user
        for the more complex commands parsing through
        the input for specific keywords.

    Parameters:
        tokens (list): A list of possible input options by the user

    Returns:
        State (enum): An enum which selects the correct state
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
        print("Please provide a command.\n\
            Try 'help' for a list of available commands.")
        return State.GAME
    if action == "quit":
        return _safe_quit()
    if action == "save":
        return State.SAVE
    if action == "load":
        return State.LOAD
    if action == "help":
        _game_helper(target)
        return State.GAME
        # Validation Needed For Objects Objects and Targets
    ge.user_command((action, obj.title(), target.title()))
    return State.GAME


def repl():
    """
    This function is the overall REPL for our game

    Returns:

    """
    state = State.MENU
    _print_menu()
    while state != State.QUIT:
        command = read()
        state = evaluate(command, state)
        if state == State.LOAD:
            _print_load()
        if state == State.MENU:
            _print_menu()


class State(Enum):
    """
    This class tracks the overall state for the game
    """
    MENU = 1
    GAME = 2
    LOAD = 3
    SAVE = 4
    QUIT = 5
