"""
A module that handles the functionality of rooms
"""
from rooms import Room
dict_rooms ={}
dict_descrips = {}


def assembling_rooms(names, neighbors, doors, items):
    """
    Constructs room objects for all rooms in maze and stores all the rooms
    inside a dictionary.
    """
    scope = range(len(names))
    for i in scope:
        room = Room(names[i], neighbors[i], doors[i], items[i])
        dict_rooms.update({room.name: room})
  
def assembling_descriptions(names, descriptions):
    """
    Adds the room descriptions for all rooms inside a dictionary.
    """
    scope = range(len(names))
    for i in scope:
        dict_descrips.update({names[i] : descriptions[i]})

def current_room(name):
    """
    The current room the player is in.
    """
    return dict_rooms[name]

def move(cardinal, name):
    """
    Returns the current room of the player after the player moves
    a certain direction.
    """
    if current_room(name).has_door_at(cardinal):
        return 'Closed door'
    elif not current_room(name).has_neighbor(cardinal):
        return 'No neighbor'
    else:
        current_key = current_room(name).neighbors[cardinal]
        return current_key
