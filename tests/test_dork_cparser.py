"""Tests for repl and command parser in dork
"""
from types import FunctionType
from unittest.mock import patch
import pytest
import dork.commandsparser as parser


def test_repl_exists():
    """the dork repl should exist
    """
    expect = "Dork.commandsparser should define a repl method"
    assert "repl" in vars(parser), expect
    assert isinstance(parser.repl, FunctionType)


def test_read_exists():
    """the commandsparser.read should exist
    """
    expect = "Dork.commandsparser should define a read method"
    assert "read" in vars(parser), expect
    assert isinstance(parser.read, FunctionType)


@pytest.mark.parametrize("expected, actual", [
    ("", ""),
    ("words go here", "words go here"),
    ("555", "555")
])
def test_read_takes_any_input(expected, actual):
    """the repl read function should accept any input
    """
    with patch('builtins.input', return_value=actual, autospec=True):
        assert parser.read() == expected


def test_evaluate_exists():
    """the commandsparser.evaluate should exist
    """
    expect = "Dork.commandsparser should define an evaluate method"
    assert "evaluate" in vars(parser), expect
    assert isinstance(parser.evaluate, FunctionType)


def test_print_load(run):
    output, _, _ = run(parser._print_load)
    assert output == ("Select a save game and hit enter to start!\n")


def test_menu_evaluate(run):
    """
    Test the menu evaluate method
    """
    output, _, _ = run(parser._menu_evaluate, ['help'])
    assert output == ("Main Menu Commands for Dork\n" +
        "help - Print a list of commands.\n" +
        "load - Load a game save file from available saves.\n" +
        "new - Start a new game on a fresh save file.\n" +
        "quit - Exits the game of 'Dork'.\n")
    output, _, _ = run(parser._menu_evaluate, ['new'])
    assert output == ("\nStarting the game of 'Dork'.\n\n" + 
        "Game Successfully Loaded.\n" + "**Entrance**\n" +
        "Welcome the campus entrance! You are in the student success building. " +
        "There are walls on the north and south ends of the " + 
        "room. There is a door in the east and a trail in the west.\n" +
        "You notice the following items--- Paper, Cage, Freshman-Badge.\n")
    output, _, _ = run(parser._menu_evaluate, ['impossible'])
    assert output == ("Please input a valid command!\nTry 'help' for more options.\n")

# Got from https://stackoverflow.com/questions/15672151/is-it-possible-for-a-unit-test-to-assert-that-a-method-calls-sys-exit
#def test_quit_dork(run):
#    with assertRaises(SystemExit):
#        output, _, _ = run(parser._quit_dork)
#        assert output == "Leaving Dork...\n\n"
    
