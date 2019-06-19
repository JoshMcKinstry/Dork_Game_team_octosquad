"""Tests for repl and command parser in dork
"""
from types import FunctionType
from unittest import mock
from unittest.mock import patch
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
        mock.call.write("starting repl..."),
        mock.call.write("\n"),
        mock.call.write("game is saved"),
        mock.call.write("\n"),
        mock.call.write("ending repl..."),
        mock.call.write("\n")
    ])


def test_read_exists():
    """the commandsparser.read should exist
    """
    expect = "Dork.commandsparser should define a read method"
    assert "read" in vars(commandsparser), expect
    assert isinstance(commandsparser.read, FunctionType)


def test_evaluate_exists():
    """the commandsparser.evaluate should exist
    """
    expect = "Dork.commandsparser should define an evaluate method"
    assert "evaluate" in vars(commandsparser), expect
    assert isinstance(commandsparser.evaluate, FunctionType)
