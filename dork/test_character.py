"""
A test for character
"""
import unittest
import character as character
from character import Character

def test_init_method():
    name = 'Hallway'
    position = 'Entrance'
    inventory =['Paper', 'Cage', 'Freshman Badge']
    character = Character(name, position, inventory) 
    assert character.name == name
    assert character.position == position
    assert character.inventory == inventory

'''def test_has_item():'''

    