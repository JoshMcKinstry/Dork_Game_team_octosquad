"""
A test for character
"""
import unittest
import character as character
from character import Character

name = 'Hallway'
position = 'Entrance'
inventory =['Paper', 'Cage', 'Freshman Badge']
main_character = Character(name, position, inventory)

def test_init_method():
    assert main_character.name == name
    assert main_character.position == position
    assert main_character.inventory == inventory

def test_has_item():
    assert main_character.has_item('Paper') == True
    assert main_character.has_item('Donut') == False

def test_delete_item():
    main_character.delete_item('Paper')
    assert main_character.inventory == ['Cage', 'Freshman Badge']

def test_add_item():
    main_character.add_item('Donut')
    assert main_character.has_item('Donut') == True
    assert main_character.has_item('Key') == False




