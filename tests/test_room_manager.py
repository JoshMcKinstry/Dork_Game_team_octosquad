"""
A test for room_manager
"""

import dork.room_manager as room_m
from mock import patch

def test_assembling_rooms():
    """ Testing assembling_rooms method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    assert room_m.DICT_ROOMS['Entrance'].name == 'Entrance'
    assert room_m.DICT_ROOMS['Entrance'].neighbors == {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    assert room_m.DICT_ROOMS['Entrance'].door == {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    assert room_m.DICT_ROOMS['Entrance'].items == 'Paper', "Donut"

def test_assembling_descriptions():
    """
    Testing aseembling_descriptions method
    """
    list_names = ['Entrance']
    list_descriptions = ['This is the entrance']
    room_m.assembling_descriptions(list_names, list_descriptions)
    assert room_m.DICT_DESCRIPTIONS['Entrance'] == 'This is the entrance'

def test_current_room():
    """
    Testing current_room method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    assert room_m.current_room('Entrance').name == 'Entrance'
    assert room_m.current_room('Entrance').neighbors == {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    assert room_m.current_room('Entrance').door == {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    assert room_m.current_room('Entrance').items == 'Paper', "Donut"

def test_room_description():
    """
    Testing room_description method
    """
    list_names = ['Entrance']
    list_descriptions = ['This is the entrance']
    room_m.assembling_descriptions(list_names, list_descriptions)
    assert room_m.room_description('Entrance') == 'This is the entrance'

def test_items_in_room():
    """
    Testing items_in_room method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    assert room_m.items_in_room('Entrance') == 'Paper', 'Donut'

def test_is_item_in_room():
    """
    Testing is_item_in_room method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    assert room_m.is_item_in_room('Entrance', 'Paper') is True

def test_append_item():
    """
    testing append_item method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    room_m.append_item('Entrance', 'Donut')
    assert room_m.DICT_ROOMS['Entrance'].items == 'Paper', 'Donut'

def test_delete_item():
    """
    testing delete_item method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    room_m.delete_item('Entrance', 'Donut')
    assert room_m.DICT_ROOMS['Entrance'].items == 'Paper'

def test_not_empty_room():
    """
    testing not_empty_room method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    assert room_m.not_empty_room('Entrance') is True

def test_to_string_current_items():
    """
    testing to_string_current_items method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    assert room_m.to_string_current_items('Entrance') == 'You notice the following items--- Paper, Donut.'

@patch('dork.rooms.has_closed_door')
@patch('dork.rooms.has_neighbors')
def test_move(mock_has_closed_door, mock_has_neighbors):
    """
    testing move method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    mock_has_closed_door.return_value = False
    mock_has_neighbors.return_value = False
    assert room_m.move('North', 'Entrance') == 'Trail'

@patch('dork.rooms.has_closed_door') 
@patch('dork.rooms.get_door_status')   
def test_open_door(mock_has_closed_door, mock_get_door_status):
    """
    testing open_door method
    """
    list_names = ['Entrance']
    list_neighbors = [{'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [{'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut', 'Dean Badge']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    mock_has_closed_door.return_value = True
    mock_get_door_status.return_value = 'Dean Badge'
    assert room_m.open_door('Enrance', 'North', 'Dean Badge') == 'Door in Entrance at North is now open.' 
