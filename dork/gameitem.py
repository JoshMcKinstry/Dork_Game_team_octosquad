'''
A class that models a item object
'''


class Items:
    '''
    Creates, uses and stores item objects
    '''
    def __init__(self, name, description, **properties):
        '''
        Constructor for items
        '''
        self.properties = {}
        self.name = name
        self.description = description
        self.properties.update(properties)
