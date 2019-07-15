# -*- coding: utf-8 -*-
"""Start CLI"""
# from dork.command_manager import CommandManager
#  """Basic CLI Dork."""
from dork.game_engine import main as main_game_engine

__all__ = ["main"]


def main(*args):
    main_game_engine()

    # command_manage = CommandManager()
    # while command_manage.check_game_over() is not True:
    #    command_manage.read_command()
    #    command_manage.execute_command()
