"""
A test for rooms
"""
from rooms import Room

def test_init_method():
    """
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    assert room.name == name
    assert room.neighbors == neighbors
    assert room.door == door
    assert room.items == items
    