'''
A room module that creates an abstract representation of a room
'''


class Room():
    '''
    A class that models an room object
    '''
    def __init__(self, name, neighbors, door, items):
        self.name = name
        self.neighbors = neighbors
        self.door = door
        self.items = items

    def has_door_at(self, cardinal):
        """
        Returns true if there is a door. False otherwise.
        """
        if self.door == None:
            return False
        else:
            return True

    def has_item(self, item_name):
        """
        Returns true if the item is in the room. False otherwise.
        """
        return item_name in self.items

    def has_neighbor(self, cardinal):
        """
        Returns true if the room has a neighboor at a cardinal. 
        Returns false if there is no neighboring room at the cardinal.
        """
        return self.neighbors[cardinal] != None

    def has_closed_door(self, cardinal):
        """
        Returns true if the door is closed. False if door is open.
        """
        return self.door['State'] == 'Closed'

    def get_door_status(self, cardinal):
        """
        Checks the status of the door.
        """
        if self.has_door_at(cardinal):
            return self.door['Status']
        else:
            return None

    def delete_item(self, item_name):
        """
        Delete item from room if it is found inside of room.
        """
        if self.has_item(item_name):
            self.items.remove(item_name)
            return item_name + ' has been picked up from ' +  self.name
        else:
            return item_name + 'is not in ' + self.name

    def add_item(self, item_name):
        """
        Adds item to the room.
        """
        self.items.append(item_name)
        return item_name + ' has been dropped in ' +  self.name


if __name__ == "__main__":
    name = 'Entrance'
    neighbors = {'East': 'Hallway',
                 'North': None,
                 'South': None,
                'West': 'Trail'}
    doors = None
    items = ['Donut', 'Paper']

    room = Room(name, neighbors, doors, items)

    print(room.has_door_at('East'))
    print(room.has_item('Donut'))
    print(room.has_item('Badge'))
    print(room.has_neighbor('North'))
    print(room.has_neighbor('West'))
    print(room.has_closed_door('East'))
    print(room.add_item('Cage'))
    print(room.items)
    print(room.delete_item('Cage'))
    print(room.items)
    print(room.get_door_status('East'))
