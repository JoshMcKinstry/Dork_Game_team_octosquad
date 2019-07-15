"""
A test for character_manager
"""

import dork.character_manager as character_m


def test_assembling_player():
    """
    Test for assembling player
    """
    position = 'Entrance'
    inventory = 'Donut'
    character_m.assembling_player(position, inventory)
    assert character_m.DICT_CHARACTERS['Player'].position == 'Entrance'
    assert character_m.DICT_CHARACTERS['Player'].inventory == 'Donut'


def test_player_position():
    """
    Test player position
    """
    position = 'Entrance'
    inventory = 'Donut'
    character_m.assembling_player(position, inventory)
    assert character_m.player_position() == 'Entrance'


def test_player_inventory():
    """
    Test player inventory
    """
    position = 'Entrance'
    inventory = 'Donut'
    character_m.assembling_player(position, inventory)
    assert character_m.player_inventory() == 'Donut'


def test_update_player_position():
    """
    Test updated player position
    """
    position = 'Entrance'
    inventory = 'Donut'
    character_m.assembling_player(position, inventory)
    character_m.update_player_position('Trail')
    assert character_m.DICT_CHARACTERS['Player'].position == 'Trail'


def test_player_has_item():
    """
    Test for the player_has_item method
    """
    position = 'Entrance'
    inventory = 'Donut'
    character_m.assembling_player(position, inventory)
    assert character_m.player_has_item('Donut') is True


def test_update_player_inventory():
    """
    Test for the update_player_inventory method
    """
    position = 'Entrance'
    inventory = ['Donut']
    character_m.assembling_player(position, inventory)
    character_m.update_player_inventory('Flower')
    assert character_m.DICT_CHARACTERS['Player'].inventory == ['Donut', 'Flower']


def test_remove_item_from_inventory():
    """
    Test for the update_player_position
    """
    position = 'Entrance'
    inventory = ['Donut', 'Flower']
    character_m.assembling_player(position, inventory)
    character_m.remove_item_from_inventory('Flower')
    assert character_m.DICT_CHARACTERS['Player'].inventory == ['Donut']
