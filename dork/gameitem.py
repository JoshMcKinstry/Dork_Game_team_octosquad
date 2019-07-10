'''
A class that models a item object
'''


class Items:
    '''
    Creates, uses and stores item objects
    '''

    def __init__(self, name, description, properties):
        '''
        Constructor for items
        '''
        self.name = name
        self.description = description
        self.properties = properties

    def use(self):
        '''
        Using item method
        '''
        return 'You used the ' + self.name + ' item'

    def store(self):
        '''
        Storing item method
        '''
        return 'You stored the ' + self.name + ' into your inventory'
