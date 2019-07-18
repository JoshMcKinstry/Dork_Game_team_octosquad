"""Tests for repl and cli in dork
"""
from types import FunctionType
from unittest.mock import patch
import pytest
import dork.cli as cli

# pylint: disable=protected-access
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

#def test_menu_through_repl(run):
#    """Test
#    """
#    with patch('dork.cli._load_evaluate', return_value=3):
#        output, _, _ = run(cli.repl, input_side_effect=['load', 'path', 'quit', 'quit'])
#    assert "Loading" in output, "menu should load previous save and then quit the game"

# https://stackoverflow.com/questions/15672151/is-it-possible-for-a-unit-test-to-assert-that-a-method-calls-sys-exit
#def test_quit_dork(run):
#    with assertRaises(SystemExit):
#        output, _, _ = run(cli._quit_dork)
#        assert output == "Leaving Dork...\n\n"
