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
