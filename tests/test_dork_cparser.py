"""Tests for repl and command parser in dork
"""
from types import FunctionType
from unittest import mock
from unittest.mock import patch
import dork.commandsparser

def test_repl_exists():
    """the dork repl should exist
    """
    assert "repl" in vars(dork.commandsparser), "Dork.commandsparser should define a repl method"
    assert isinstance(dork.commandsparser.repl, FunctionType)

@patch('dork.commandsparser.read', return_value='say goodbye')
@patch('dork.commandsparser.evaluate', return_value=('your game is saved', True))
def test_repl_runs_with_input(_mock_read, _mock_evaluate):
    """the repl runs with correct output given specific input
    """
    #https://forum.learncodethehardway.com/t/testing-input-and-print/1757/10
    with patch('sys.stdout') as mock_print:
        dork.commandsparser.repl()
    mock_print.assert_has_calls([
        mock.call.write("starting repl..."),
        mock.call.write("\n"),
        mock.call.write("your game is saved"),
        mock.call.write("\n"),
        mock.call.write("ending repl..."),
        mock.call.write("\n")
    ])

def test_read_exists():
    """the commandsparser.read should exist
    """
    assert "read" in vars(dork.commandsparser), "Dork.commandsparser should define a read method"
    assert isinstance(dork.commandsparser.read, FunctionType)

def test_evaluate_exists():
    """the commandsparser.evaluate should exist
    """
    expect = "Dork.commandsparser should define an evaluate method"
    assert "evaluate" in vars(dork.commandsparser), expect
    assert isinstance(dork.commandsparser.evaluate, FunctionType)
