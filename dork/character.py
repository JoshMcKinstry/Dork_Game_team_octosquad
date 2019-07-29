'''
A character module that creates an abstract representation of a character
'''


class Character():
    '''
    A class that models an character object
    '''
    def __init__(self, name, position, inventory):
        self.name = name
        self.position = position
        self.inventory = inventory

    def has_item(self, item_name):
        """
        This function determines if the player is holding an item.

        Parameters:
            item_name (dict): A dictionary of possible items

        Returns:
            item_name (bool): True if the player holds the item,
                false otherwise.
        """
        return item_name in self.inventory

    def delete_item(self, item_name):
        """
        This function removes an item from the character

        Parameters:
            item_name (dict): A dictionary of possible items

        Returns:
            A string indicating the state of the item.
        """
        if self.has_item(item_name):
            self.inventory.remove(item_name)
            return (self.name
                    + ' has lost '
                    + item_name + '.', True)
        return (self.name
                + ' does not hold '
                + item_name + '.', False)

    def add_item(self, item_name):
        """
        This function adds an item to the character.

        Parameters:
            item_name (dict): A dictionary of possible items.

        Returns:
            A string verifying that he player has the item.
        """
        self.inventory.append(item_name)
        return self.name + ' now holds ' + item_name
