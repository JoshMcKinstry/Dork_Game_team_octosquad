'''
A items module that creates an abstract representation of an item.
'''


class Item():
    '''
    This is a class that models an item object.

    Attributes:
        name (list): A list that contains all the items available to game.
        description (list): A list that contains all the descriptions
            for each of the items.
        properties (list): A list of lists that contain all the properties
            associated with an item.
    '''

    def __init__(self, name, description, properties):
        """
        The constructor for the items class.

        Parameters:
            name (list): A list that contains all the items available to game.
            description (list): A list that contains all the descriptions
                for each of the items.
            properties (list): A list of lists that contain all the properties
                associated with an item.
        """
        self.name = name
        self.description = description
        self.properties = properties

    def has_property(self, attribute):
        """
        The function that checks to see if the item has a certain property.

        Parameters:
            attribute (str): A string that contains the property of item.

        Returns:
            bool: True if the attribute is found in the item's list of
                properties. False otherwise.
        """
        return attribute in self.properties

    def yaml_representation(self):
        """
        The function creates a yml compatible representation of a item object.

        Returns:
            item (dictionary): A dictionary that contains the item's name as
                the key value and a value of a dictionary containing the
                item's description and properties.
        """

        item_attributes = {'Description': self.description,
                           'Properties': self.properties}
        item = {self.name: item_attributes}
        return item
