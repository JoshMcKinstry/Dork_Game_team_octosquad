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
        Returns true if the character holds the item. False otherwise.
        """
        return item_name in self.inventory


    def delete_item(self, item_name):
        """
        Delete item from character if it is found inside of character inventory.
        """
        if self.has_item(item_name):
            self.inventory.remove(item_name)
            return (self.name + ' has lost ' + item_name + '.', True)
        return (self.name + ' does not hold ' + item_name + '.', False)


    def add_item(self, item_name):
        """
        Adds item to the character.
        """
        self.inventory.append(item_name)
        return self.name + ' now holds ' + item_name
