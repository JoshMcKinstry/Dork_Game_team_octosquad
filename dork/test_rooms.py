"""
A test for rooms
"""
from rooms import Room

def test_init_method():
    """
    Test the constructor
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

def test_has_door_at():
    """
    Test if the room has a door at a cardinal
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    no_door = None
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    room_no_door = Room(name, neighbors, no_door, items)
    assert room.has_door_at('North') == True
    assert room.has_door_at('South') == False
    assert room_no_door.has_door_at('North') == False


def test_has_item():
    """
    Test has_item method
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    assert room.has_item('Paper') == True
    assert room.has_item('Freshman Badge') == False    

def test_has_neighbor():
    """
    Test if the room has a neighbor
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    assert room.has_neighbor('North') == True
    assert room.has_neighbor('East') == False
    
def test_has_closed_door():
    """
    Test if the room has a closed door
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    assert room.has_closed_door('East') == False
    assert room.door['State'] == 'Closed'

def test_get_door_status():
    """
    Test the door status
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    assert room.get_door_status('East') == None
    assert room.

def test_update_door_status():
    """
    Test if the door status updates
    """
    pass

def test_delete_item():
    """
    Test if the item was deleted was in room
    """
    pass

def test_add_item():
    """
    Test if the item was added to the room
    """
    pass
