'''
A player module that creates an abstract representation of a player
'''


class Player():
    '''
    A class that models an room object
    '''
    def __init__(self, name, position, items):
        self.name = name
        self.position = position
        self.items = items