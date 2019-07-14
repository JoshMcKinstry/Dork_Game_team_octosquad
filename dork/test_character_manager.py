"""
A test for character_manager
"""

import character_manager as character_m

def test_assembling_player():
    """
    Test for assembling player
    """
    list_position = ['Entrance']
    list_inventory = ['donut']
    character_m.assembling_player(list_position, list_inventory)
    assert character_m.DICT_CHARACTERS['Player'].position == ['Entrance']
    assert character_m.DICT_CHARACTERS['Player'].inventory == ['donut']
    
def test_player_position():
    """
    Test player position
    """
    list_position = ['Entrance']
    list_inventory = ['donut']
    character_m.assembling_player(list_position, list_inventory)
    assert character_m.player_position() == ['Entrance']
    
def test_player_inventory():
    """
    Test player inventory
    """
    list_position = ['Entrance']
    list_inventory = ['donut']
    character_m.assembling_player(list_position, list_inventory)
    assert character_m.player_inventory() == ['donut']

def test_update_player_position():
    """
    Test updated player position
    """
    list_position = ['Entrance']
    list_inventory = ['donut']
    pass
