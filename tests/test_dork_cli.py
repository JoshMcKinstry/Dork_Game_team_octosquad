"""Tests for repl and cli in dork
"""
from types import FunctionType
import dork.cli as cli


def test_repl_exists():
    """the dork repl should exist
    """
    expect = "Dork.cli should define a repl method"
    assert "repl" in vars(cli), expect
    assert isinstance(cli.repl, FunctionType)
