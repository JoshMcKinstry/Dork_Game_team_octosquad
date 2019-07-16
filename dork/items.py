'''
A items module that creates an abstract representation of an item
'''


class Item():
    '''
    A class that models an item object
    '''
    def __init__(self, name, description, properties):
        self.name = name
        self.description = description
        self.properties = properties

    def has_property(self, attribute):
        """
        Returns true if the item instance contains a specific attribute
        """
        return attribute in self.properties

    def yaml_representation(self):
        """
        Creates a yml compatible representation of a item object
        """

        item_attributes = {'Description': self.description,
                           'Properties': self.properties}
        item = {self.name: item_attributes}
        return item
