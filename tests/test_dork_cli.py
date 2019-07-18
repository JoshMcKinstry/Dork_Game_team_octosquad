"""Tests for repl and cli in dork
"""
from types import FunctionType
from unittest.mock import patch
import pytest
import dork.cli as cli


def test_repl_exists():
    """the dork repl should exist
    """
    expect = "Dork.cli should define a repl method"
    assert "repl" in vars(cli), expect
    assert isinstance(cli.repl, FunctionType)


def test_read_exists():
    """the cli.read should exist
    """
    expect = "Dork.cli should define a read method"
    assert "read" in vars(cli), expect
    assert isinstance(cli.read, FunctionType)


def test_evaluate_exists():
    """the cli.evaluate should exist
    """
    expect = "Dork.cli should define an evaluate method"
    assert "evaluate" in vars(cli), expect
    assert isinstance(cli.evaluate, FunctionType)


@pytest.mark.parametrize("expected, actual", [
    ("", ""),
    ("words go here", "words go here"),
    ("555", "555")
    ])
def test_read_takes_any_input(expected, actual):
    """the repl read function should accept any input
    """
    with patch('builtins.input', return_value=actual, autospec=True):
        assert cli.read() == expected


def test_print_load(run):
    """Test _print_load outputs correctly
    """
    output, _, _ = run(cli._print_load)
    assert "Loading previous" in output, "_print_load should print a message"


def test_menu_evaluate(run):
    """Test the menu evaluate method
    """
    output, _, _ = run(cli._menu_evaluate, ['help'])
    assert "Main Menu Commands" in output, "help command should provide helpful messages"
    output, _, _ = run(cli._menu_evaluate, ['new'])
    assert "Starting the game" in output, "new command should start a new game"
    output, _, _ = run(cli._menu_evaluate, ['impossible'])
    assert "Please input a valid command" in output, "bad commands should be handled"


def test_game_evaluate(run):
    """Test
    """
    output, _, _ = run(cli._game_evaluate, ['notaction'])
    assert "Please provide a command" in output, "bad commands in game should be handled"


@pytest.mark.parametrize('inputs', [('y'), ('n'), ('bad')])
def test_safe_quit(run, inputs):
    """Test
    """
    output, _, _ = run(cli._safe_quit, input_side_effect=[inputs])
    assert "Would you like to save" in output, "game should ask if game should be saved"

def test_repl(run):
    """Test that game can start and quit
    """
    with pytest.raises(SystemExit):
        output, _, _ = run(cli.repl, input_side_effect=['quit'])
        assert "Welcome to the Game" in output, "game should start from menu"
        assert "Leaving Dork" in output, "game should quit from menu"


def test_print_info(run):
    """Test that description of game is printed out
    """
    output, _, _ = run(cli._print_info)
    assert "What is Dork" in output, "game should have a description"

@pytest.mark.parametrize('command', ['', 'move', 'use'])
def test_game_helper(run, command):
    """Test that game prints help messages
    """
    output, _, _ = run(cli._game_helper, command)
    if command == '':
        assert "List of in game commands" in output, "help should return command list"
    elif command == 'move':
        assert "MOVE" in output, "help move should print 'move' help message"
    elif command == 'use':
        assert "USE" in output, "help use should print 'move' help message"


def test_save_evaluate(run):
    """Test that saving prints message
    """
    output, _, _ = run(cli._save_evaluate)
    assert "Saving Game" in output, "game should notify player that game is saving"


def test_menu_evaluates_info(run):
    """Test that the menu evaluates the 'info' command
    """
    output, _, _ = run(cli._menu_evaluate, ["info"])
    assert "What is Dork" in output, "menu should accept 'info' as a command"

@pytest.mark.parametrize('state', [(5), (3), (1)])
def test_cli_state_changes(run, state):
    """Test that quit and load change states and that menu is printed when returned to
    """
    with pytest.raises(SystemExit):
        if state == 5:
            output, _, _ = run(cli.repl, input_side_effect=['quit'])
            assert "Leaving Dork" in output
        elif state == 3:
            output, _, _ = run(cli.repl, input_side_effect=['load', 'path', 'quit'])
            assert "Loading" in output
        elif state == 1:
            output, _, _ = run(cli.repl, input_side_effect=['help', 'quit'])
            assert "Welcome" in output

def test_game_evaluates_quit(run):
    """Test that when game quits, it asks player to save first
    """
    output, _, _ = run(cli._game_evaluate, ['quit'], input_side_effect=['bad'])
    assert "Would you like to save the game" in output
    assert "Invalid Response" in output


def test_game_evaluates_full_command(run):
    """Test that the game evaluator calls the game engine
    """
    with patch('dork.game_engine.user_command') as called:
        run(cli._game_evaluate, ['move', 'north'])
        called.assert_called_with(('move', '', 'North'))


def test_game_gives_help(run):
    """Test that the game provides help to players
    """
    with patch('dork.cli._game_helper') as helping:
        run(cli._game_evaluate, ['help', 'move'])
        helping.assert_called_with('move')
