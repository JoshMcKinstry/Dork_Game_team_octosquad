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
