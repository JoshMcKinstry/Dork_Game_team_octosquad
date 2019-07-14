"""
A test for room_manager
"""

import room_manager as room_m


def test_assembling_item():
    """
    Test for assembling items
    """
    list_room = ['entrance']
    list_neighbors = ['trail']
    list_property = ['openable']
    room_m.assembling_rooms(list_room, list_neighbors, list_property)
    assert item_m.DICT_ITEMS['entrance'].name == 'entrance'
    assert item_m.DICT_ITEMS['entrance'].description == 'This is a trail'
    assert item_m.DICT_ITEMS['entrance'].properties == 'openable'

def test_is_item():
    """
    Test for if the item is an item
    """
    list_room = ['entrance']
    list_neighbors = ['This is a trail']
    list_property = ['openable']
    room_m.assembling_rooms(list_room, list_neighbors, list_property)
    assert item_m.is_item('entrance') == True
    assert item_m.is_item('sword') == False

def test_item_description():
    """
    Test for item description
    """
    list_room = ['entrance']
    list_neighbors = ['This is a trail']
    list_property = ['openable']
    room_m.assembling_rooms(list_room, list_neighbors, list_property)
    assert item_m.item_description('entrance') == 'This is a trail'
    assert item_m.item_description('entrance') != 'ewfwefwefe'