'''
A class that models a item object
'''


class Items:
    '''
    Creates, uses and stores item objects
    '''
    attributes = {}

    def __init__(self, name, description, **properties):
        '''
        Constructor for items
        '''
        self.name = name
        self.description = description
        attributes.update(**properties)
