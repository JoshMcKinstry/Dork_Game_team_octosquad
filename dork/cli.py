# -*- coding: utf-8 -*-
"""Start CLI"""
# from dork.command_manager import CommandManager
#  """Basic CLI Dork."""

__all__ = ["main"]


def main(*args):
    """Main CLI runner for Dork
    """
    script_name = args[0] if args else '???'
    if "-h" in args or '--help' in args:
        print("usage:", script_name, "[-h]")
    else:
        print(*args)
    # command_manage = CommandManager()
    # while command_manage.check_game_over() is not True:
    #    command_manage.read_command()
    #    command_manage.execute_command()
