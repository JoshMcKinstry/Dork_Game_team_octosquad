'''
An items module that creates an abstract representation of an item.
'''


class Item():
    '''
    This is a class that models an item object.

    Attributes:
        name (str): The name of an item.
        description (str): The description of an item.
        properties (list): The list of all the properties that an item
            contains.
    '''

    def __init__(self, name, description, properties):
        """
        The constructor for the items class.

        Parameters:
            name (str): The name of the item.
            description (str): The description of the item.
            properties (list): The list of all the properties that an item
            contains.
        """
        self.name = name
        self.description = description
        self.properties = properties

    def has_property(self, attribute):
        """
        The function that checks to see if the item has a certain property.

        Parameters:
            attribute (str): The property of an item.

        Returns:
            bool: True if the attribute is found in the item's list of
                properties. False otherwise.
        """
        return attribute in self.properties

    def yaml_representation(self):
        """
        The function creates a yml compatible representation of a item object.

        Returns:
            item (dict): A dictionary that contains the item's name as
                the key value and a dictionary value containing the
                item's description and properties.
        """

        item_attributes = {'Description': self.description,
                           'Properties': self.properties}
        item = {self.name: item_attributes}
        return item
