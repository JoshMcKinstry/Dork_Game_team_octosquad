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
    main_character = Character(name, position, inventory) 
    assert main_character.name == name
    assert main_character.position == position
    assert main_character.inventory == inventory

def test_has_item():
    name = 'Hallway'
    position = 'Entrance'
    inventory =['Paper', 'Cage', 'Freshman Badge']
    main_character = Character(name, position, inventory)
    assert main_character.has_item('Paper') == True
    assert main_character.has_item('Donut') == False








