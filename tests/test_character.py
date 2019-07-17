"""
A test for character
"""
from dork.character import Character


def test_init_method():
    """
    Test constructor
    """
    name = 'Hallway'
    position = 'Entrance'
    inventory = ['Paper', 'Cage', 'Freshman Badge']
    main_character = Character(name, position, inventory)
    assert main_character.name == name
    assert main_character.position == position
    assert main_character.inventory == inventory


def test_has_item():
    """
    Check that inventory has item
    """
    name = 'Hallway'
    position = 'Entrance'
    inventory = ['Paper', 'Cage', 'Freshman Badge']
    main_character = Character(name, position, inventory)
    assert main_character.has_item('Paper') is True
    assert main_character.has_item('Donut') is False


def test_delete_item():
    """
    Test to see if items delete
    """
    name = 'Player'
    position = 'Entrance'
    inventory = ['Paper', 'Cage', 'Freshman Badge']
    main_character = Character(name, position, inventory)
    out_put = main_character.delete_item('Paper')
    expected = ('Player has lost Paper.', True)
    assert out_put == expected
    out_put_2 = main_character.delete_item('Key')
    expected_2 = ('Player does not hold Key.', False)
    assert out_put_2 == expected_2


def test_add_item():
    """
    Test to make sure item is added
    """
    name = 'Hallway'
    position = 'Entrance'
    inventory = ['Paper', 'Cage', 'Freshman Badge']
    main_character = Character(name, position, inventory)
    main_character.add_item('Donut')
    assert main_character.has_item('Donut') is True
    assert main_character.has_item('Key') is False
