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
        Returns true if there is a door at the specific cardinal.
        False otherwise.
        """
        if self.door is None:
            return False
        if self.door['Cardinal'] != cardinal:
            return False
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
        return self.neighbors[cardinal] is not None

    def has_closed_door(self, cardinal):
        """
        Returns true if the door is closed. False if door is open.
        """
        if self.has_door_at(cardinal):
            return self.door['State'] == 'Closed'
        return False

    def get_door_status(self, cardinal):
        """
        Checks the status of the door.
        """
        if self.has_door_at(cardinal):
            return self.door['Status']
        return None

    def update_door_status(self):
        """
        Updates status of door to see if open or closed
        """
        self.door['State'] = 'Open'
        return ('Door in ' + self.name + ' at ' + self.door['Cardinal']
                + ' is now open.')

    def delete_item(self, item_name):
        """
        Delete item from room if it is found inside of room.
        """
        if self.has_item(item_name):
            self.items.remove(item_name)
            return (item_name + ' has been picked up from '
                    + self.name + '.', True)
        return ('No item called ' + item_name + ' is in '
                + self.name + '.', False)

    def add_item(self, item_name):
        """
        Adds item to the room.
        """
        self.items.append(item_name)
        return item_name + ' has been dropped in ' + self.name + '.'

    def yaml_representation(self):
        """
        Creates a yml compatible representation of a room object
        """

        room_attributes = {'Neighbors': self.neighbors,
                           'Items': self.items, 'Door': self.door}
        room = {self.name: room_attributes}
        return room
