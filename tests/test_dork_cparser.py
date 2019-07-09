"""Tests for repl and command parser in dork
"""
from types import FunctionType
from unittest import mock
from unittest.mock import patch
import pytest
from dork import commandsparser

def test_repl_exists():
    """the dork repl should exist
    """
    expect = "Dork.commandsparser should define a repl method"
    assert "repl" in vars(commandsparser), expect
    assert isinstance(commandsparser.repl, FunctionType)


@patch('dork.commandsparser.read', return_value='say goodbye')
@patch('dork.commandsparser.evaluate', return_value=('game is saved', True))
def test_repl_runs_with_input(_mock_read, _mock_evaluate):
    """the repl runs with correct output given specific input
    """
    # https://forum.learncodethehardway.com/t/testing-input-and-print/1757/10
    with patch('sys.stdout') as mock_print:
        commandsparser.repl()
    mock_print.assert_has_calls([
        mock.call.write("Welcome to Dork!"),
        mock.call.write("\n"),
        mock.call.write("game is saved"),
        mock.call.write("\n"),
        mock.call.write("ending repl..."),
        mock.call.write("\n")
    ])


def test_move_north():
    """the commandsparser should ask room_printing to print
    """
    expect = "Dork.commandsparser should define a _move_north method"
    assert "move_north" in vars(commandsparser), expect
    assert isinstance(commandsparser.move_north, FunctionType)
    with patch('sys.stdout') as mock_print:
        commandsparser.move_north()
    mock_print.assert_has_calls([
        mock.call.write('You enter the boss room.'),
        mock.call.write("\n")
    ])

def test_move_south():
    """the commandsparser should ask room_printing to print
    """
    expect = "Dork.commandsparser should define a _move_north method"
    assert "move_south" in vars(commandsparser), expect
    assert isinstance(commandsparser.move_south, FunctionType)
    with patch('sys.stdout') as mock_print:
        commandsparser.move_south()
    mock_print.assert_has_calls([
        mock.call.write("You cannot go/move south."),
        mock.call.write("\n")
    ])
def test_move_east():
    """the commandsparser should ask room_printing to print
    """
    expect = "Dork.commandsparser should define a move_east method"
    assert "move_east" in vars(commandsparser), expect
    assert isinstance(commandsparser.move_east, FunctionType)
    with patch('sys.stdout') as mock_print:
        commandsparser.move_east()
    mock_print.assert_has_calls([
        mock.call.write("There is a table in the room with a donut on top."),
        mock.call.write("\n")
    ])

def test_move_west():
    """the commandsparser should ask room_printing to print
    """
    expect = "Dork.commandsparser should define a move_west method"
    assert "move_west" in vars(commandsparser), expect
    assert isinstance(commandsparser.move_west, FunctionType)
    with patch('sys.stdout') as mock_print:
        commandsparser.move_west()
    mock_print.assert_has_calls([
        mock.call.write("There is a beautiful garden with the roadrunner'snest "+
                        "right \nin the center of the garden. The nest has eggs "+
                        "that look about \nready to hatch but no roadrunner parent to be seen."),
        mock.call.write("\n")
    ])

def test_look_north():
    """the commandsparser should ask room_printing to print
    """
    expect = "Dork.commandsparser should define a look_north method"
    assert "look_north" in vars(commandsparser), expect
    assert isinstance(commandsparser.look_north, FunctionType)
    with patch('sys.stdout') as mock_print:
        commandsparser.look_north()
    mock_print.assert_has_calls([
        mock.call.write("There is a door with a sign that says DANGER."),
        mock.call.write("\n")
    ])
def test_look_south():
    """the commandsparser should ask room_printing to print
    """
    expect = "Dork.commandsparser should define a look_south method"
    assert "look_south" in vars(commandsparser), expect
    assert isinstance(commandsparser.look_south, FunctionType)
    with patch('sys.stdout') as mock_print:
        commandsparser.look_south()
    mock_print.assert_has_calls([
        mock.call.write("There is bag of bird food with all sorts of " +
                        "insects that roadrunners love to eat."),
        mock.call.write("\n")
    ])
def test_look_east():
    """the commandsparser should ask room_printing to print
    """
    expect = "Dork.commandsparser should define a look_east method"
    assert "look_east" in vars(commandsparser), expect
    assert isinstance(commandsparser.look_east, FunctionType)
    with patch('sys.stdout') as mock_print:
        commandsparser.look_east()
    mock_print.assert_has_calls([
        mock.call.write("To the East, there is a sign that says Lounge."),
        mock.call.write("\n")
    ])
def test_look_west():
    """the commandsparser should ask room_printing to print
    """
    expect = "Dork.commandsparser should define a look_west method"
    assert "look_west" in vars(commandsparser), expect
    assert isinstance(commandsparser.look_west, FunctionType)
    with patch('sys.stdout') as mock_print:
        commandsparser.look_west()
    mock_print.assert_has_calls([
        mock.call.write("To the West, there is a sign that says " +
                        "Roadrunner's Nest"),
        mock.call.write("\n")
    ])

def test_read_exists():
    """the commandsparser.read should exist
    """
    expect = "Dork.commandsparser should define a read method"
    assert "read" in vars(commandsparser), expect
    assert isinstance(commandsparser.read, FunctionType)

@pytest.mark.parametrize("expected, actual", [
    ("", ""),
    ("words go here", "words go here"),
    ("555", "555")
])
def test_read_takes_any_input(expected, actual):
    """the repl read function should accept any input
    """
    with patch('builtins.input', return_value=actual, autospec=True):
        assert commandsparser.read() == expected


def test_evaluate_exists():
    """the commandsparser.evaluate should exist
    """
    expect = "Dork.commandsparser should define an evaluate method"
    assert "evaluate" in vars(commandsparser), expect
    assert isinstance(commandsparser.evaluate, FunctionType)


@pytest.mark.parametrize("command,response", [
    ("go north", ("", False)),
    ("go east", ("", False)),
    ("go west", ("", False)),
    ("go south", ("", False))
])
def test_evaluate_go_commands(command, response):
    """dork go commands should be correctly evaluated
    """
    assert commandsparser.evaluate(command) == response


@pytest.mark.parametrize("command,response", [
    ("get object", ("you picked up an item", False)),
    ("use object", ("you used an item", False)),
    ("look around", ("Unknown Command", False)),
    ("drop object", ("you dropped an item", False))
])
def test_evaluate_action_commands(command, response):
    """dork action commands should be correctly evaluated
    """
    assert commandsparser.evaluate(command) == response


@pytest.mark.parametrize("command,response", [
    ("start dork", ("Welcome to Dork!", False)),
    ("quit dork", ("Leaving the game of Dork.", True))
])
def test_evaluate_starting_and_ending_dork(command, response):
    """dork game commands should be correctly evaluated
    """
    assert commandsparser.evaluate(command) == response


@pytest.mark.parametrize("command,response", [
    ("Go north", ("", False)),
    ("GO eaST", ("", False)),
    ("gEt obJecT", ("you picked up an item", False)),
    ("lOOk ArouNd", ("Unknown Command", False)),
    ("sTART dOrK", ("Welcome to Dork!", False)),
    ("QUIT DORK", ("Leaving the game of Dork.", True))
])
def test_evaluate_ignores_case(command, response):
    """dork game commands should not be case sensitive
    """
    assert commandsparser.evaluate(command) == response


@pytest.mark.parametrize("command,response", [
    ("have jelly", ("Unknown Command", False)),
    ("move sideways", ("Unknown Command", False))
])
def test_evaluate_has_unknown_commands(command, response):
    """dork game has commands that are unknown
    """
    assert commandsparser.evaluate(command) == response


# https://medium.com/opsops/how-to-test-if-name-main-1928367290cb
def test_init():
    """testing of the if __name__ == "__main__" method
    """
    with patch.object(commandsparser, "repl", return_value=42):
        with patch.object(commandsparser, "__name__", "__main__"):
            with patch.object(commandsparser.sys, 'exit') as mock_exit:
                commandsparser.init()
                assert mock_exit.call_args[0][0] == 42
