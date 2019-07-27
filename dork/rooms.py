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
        Checks if a room is present at a certain Cardinal

        Parameters:
            cardinal(str): A string of a direction to check.

        Returns:
            bool: Returns true there is a door at the cardinal. Returns false otherwise.
        """
        if self.door is None:
            return False
        if self.door['Cardinal'] != cardinal:
            return False
        return True

    def has_item(self, item_name):
        """
        Checks to see if a specified item is in the room.

        Parameters:
            item_name(str): an items name to be checked if in room.
        Returns:
            bool: Returns true if item is in the room.  False otherwise.
        """
        return item_name in self.items

    def has_neighbor(self, cardinal):
        """
        Checks to see if the current room has an adjacent room.

        Parameters:
            cardinal(str): A string of a direction to check for a room.

        Returns:
            bool: Returns true if the room has a neighbor.  False otherwise.
        """
        return self.neighbors[cardinal] is not None

    def has_closed_door(self, cardinal):
        """
        Checks to see if the current room has a closed door at a certain cardinal.

        Parameters:
            cardinal(str): A string of a direction to check for a closed door.

        Returns:
            bool: Returns true if a closed door is at the cardinal.  False otherwise.
        """
        if self.has_door_at(cardinal):
            return self.door['State'] == 'Closed'
        return False

    def get_door_status(self, cardinal):
        """
        If there is a door at the specified cardinal, return the status of it.

        Parameters:
            cardinal(str): A string of a direction to check for a door.

        Returns:
            str: The doors status.
        """
        if self.has_door_at(cardinal):
            return self.door['Status']
        return None

    def update_door_status(self):
        """
        Method used to open a door.

        Returns:
            str: prints a string to the user after opening a door.
        """
        self.door['State'] = 'Open'
        return ('Door in ' + self.name + ' at ' + self.door['Cardinal']
                + ' is now open.')

    def delete_item(self, item_name):
        """
        Delete item from room if it is found inside of room.

        Parameters:
            item_name(str): The items name to check for in the room.

        Returns:
            bool: Returns true if the item has been removed from the room. False otherwise.
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

        Parameters:
            item_name(str): The item to be added to the room.

        Returns:
            str: String printed to user when they drop an item.
        """
        self.items.append(item_name)
        return item_name + ' has been dropped in ' + self.name + '.'

    def yaml_representation(self):
        """
        Creates a yml compatible representation of a room object

        Returns:
            Room: The room represented from the yml.
        """

        room_attributes = {'Neighbors': self.neighbors,
                           'Items': self.items, 'Door': self.door}
        room = {self.name: room_attributes}
        return room
