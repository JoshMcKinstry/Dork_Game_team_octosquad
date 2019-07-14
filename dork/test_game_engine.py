"""
A test for game_engine
"""
import unittest
from unittest import mock
from mock import patch
import game_engine as engine


class TestValidMaze(unittest.TestCase):
    """
    A testing class for ValidMaze
    """
 
    def test_loading_map(self):
        """
        Testing the data loading method.
        """
        _d = 'This the description'
        _c = ['Paper', 'Donut']
        _b = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
        _a = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
        room_1 = {'Neighbors': _a, 'Door': _b, 'Items': _c, 'Description': _d}
        rooms = {'room_1': room_1}
        data = {'Rooms': rooms}
        self.assertIsNone(engine.loading_map(data))


    def test_loading_item(self):
        """
        Testing the loading item method.
        """
        

'''
    def loading_player():
        """
        Testing the loading player method
        """
        pass

    def __current_position():
        """
        Testing the method that returns the player current position
        """
        pass


    def display_inventory():
        """
        Testing the method that prints the player inventory
        """
        


    def room_to_screen():
        """
        Testing the method that prints the room name,
        room description and room items.
        """
    

    def move():
        """
        Testing the method that moves the player around
        the map.
        """
        


    def examine():
        """
        Testing the method that examine the items.
        """



    def pick_up():
        """
        Testing the method that picks up items from current room
        """
        

    def drop():
        """
        Testing the method that drops items into current room
        """
        

    def use_key():
        """
        Testing the method that use keys in doors
        """
'''