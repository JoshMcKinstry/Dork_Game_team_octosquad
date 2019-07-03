# -*- coding: utf-8 -*-
"""Basic tests for state and entity relationships in dork
"""
import dork.types
from tests.utils import has_many, is_a


def test_items_exist():
    """the dork module should define an Item
    """
    assert "Item" in vars(dork.types)
    is_a(dork.types.Item, type)


def test_holders_exist():
    """the dork module should define an Holder
    """
    assert "Holder" in vars(dork.types)
    is_a(dork.types.Holder, type)


def test_players_exist():
    """the dork module should define an Player
    """
    assert "Player" in vars(dork.types)
    is_a(dork.types.Player, type)


def test_rooms_exist():
    """the dork module should define an Room
    """
    assert "Room" in vars(dork.types)
    is_a(dork.types.Room, type)


def test_path_exists():
    """the dork module should define an Path
    """
    assert "Path" in vars(dork.types)
    is_a(dork.types.Path, type)


def test_map_exists():
    """the dork module should define an Map
    """
    assert "Map" in vars(dork.types)
    is_a(dork.types.Map, type)


def test_holder_has_many_items():
    """A Holder should have many Items
    """
    has_many(dork.types.Holder, "holder", dork.types.Item, "items")


def test_player_is_a_holder(player):
    """A Player should be a Holder
    """
    is_a(player, dork.types.Holder)


def test_room_is_a_holder(room):
    """A Room should be a Holder
    """
    is_a(room, dork.types.Holder)


def test_room_has_many_players():
    """A Room should have many players
    """
    has_many(dork.types.Room, "room", dork.types.Player, "players")


def test_room_has_many_paths():
    """A Room should have many Paths through exits and entrances.
    """
    has_many(dork.types.Room, "entrance", dork.types.Path, "entrances")
    has_many(dork.types.Room, "exit", dork.types.Path, "exits")


def test_map_has_many_rooms():
    """A Map should have many Rooms
    """
    has_many(dork.types.Map, "map", dork.types.Room, "rooms")
