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

def test_safe_quit(run):
    """Test
    """
    output, _, _ = run(cli._safe_quit)
    assert "Would you like to save" in output, "game should ask if game should be saved"

def test_repl(run):
    """Test
    """
    output, _, _ = run(cli.repl, input_side_effect=['quit'])
    assert "Welcome to the Game of Dork" in output, "main menu should welcome player to game"


# https://stackoverflow.com/questions/15672151/is-it-possible-for-a-unit-test-to-assert-that-a-method-calls-sys-exit
#def test_quit_dork(run):
#    with assertRaises(SystemExit):
#        output, _, _ = run(cli._quit_dork)
#        assert output == "Leaving Dork...\n\n"
