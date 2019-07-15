"""
A test for rooms
"""
from dork.rooms import Room

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
    door_open = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Open'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    room2 = Room(name, neighbors, door_open, items)
    assert room.has_closed_door('North') == True
    assert room2.has_closed_door('North') == False
    assert room.has_closed_door('East') == False


def test_get_door_status():
    """
    Test the door status
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    assert room.get_door_status('East') is None
    assert room.get_door_status('North') == 'Dean Badge'


def test_update_door_status():
    """
    Test if the door status updates
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    room.update_door_status()
    assert room.door['State'] == 'Open'
    assert room.update_door_status() == (
        'Door in ' + room.name + ' at ' + room.door['Cardinal'] 
        + ' is now open.')

def test_delete_item():
    """
    Test if the item was deleted was in room
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    assert room.delete_item('Donut') == (
        'Donut' + ' has been picked up from ' +  room.name + '.', True)
    assert room.delete_item('Flyer') == (
        'No item called ' + 'Flyer' + ' is in ' + room.name + '.', False)

def test_add_item():
    """
    Test if the item was added to the room
    """
    name = 'Entrance'
    neighbors = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    door = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    items = ['Paper', 'Donut']
    room = Room(name, neighbors, door, items)
    assert room.add_item('Flyer') == (
        'Flyer' + ' has been dropped in ' +  room.name + '.')
    assert room.items == ['Paper', 'Donut', 'Flyer']
