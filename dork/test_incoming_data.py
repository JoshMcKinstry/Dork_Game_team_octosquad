"""
A test for mapvalidation
"""
import unittest
import incoming_data as game_data


class TestValidMaze(unittest.TestCase):
    """
    A testing class for ValidMaze
    """
  

    def test_load_rooms(self):
        """
        Testing the Loading of the room names
        """
        room_1 = {'Neighbors': 'A', 'Door': 'B', 'Items': 'C', 'Description': 'D'}
        rooms = {'room_1': room_1}
        data = {'Rooms': rooms}
        out_put = game_data.load_rooms(data)
        expected = ['room_1']
        self.assertEqual(out_put, expected)


    def test_load_cardinals(self):
        """
        Testing the Loading of the room cardinals
        """
        room_1 = {'Neighbors': 'A', 'Door': 'B', 'Items': 'C', 'Description': 'D'}
        rooms = {'room_1': room_1}
        data = {'Rooms': rooms}
        expected = ['A']
        out_put = game_data.load_cardinals(data, ['room_1'])
        self.assertEqual(out_put, expected)


    def test_load_doors(self):
        """
        Testing the Loading of the doors in each room
        """
        room_1 = {'Neighbors': 'A', 'Door': 'B', 'Items': 'C', 'Description': 'D'}
        rooms = {'room_1': room_1}
        data = {'Rooms': rooms}
        expected = ['B']
        out_put = game_data.load_doors(data, ['room_1'])
        self.assertEqual(out_put, expected)


    def test_load_room_descrips(self):
        """
        Testing the Loading of each room respective main description
        """
        room_1 = {'Neighbors': 'A', 'Door': 'B', 'Items': 'C', 'Description': 'D'}
        rooms = {'room_1': room_1}
        data = {'Rooms': rooms}
        expected = ['D']
        out_put = game_data.load_room_descrips(data, ['room_1'])
        self.assertEqual(out_put, expected)


    def test_load_list_room_items(self):
        """
        Testing the Loading of each room respective list of items
        """
        room_1 = {'Neighbors': 'A', 'Door': 'B', 'Items': 'C', 'Description': 'D'}
        rooms = {'room_1': room_1}
        data = {'Rooms': rooms}
        expected = ['C']
        out_put = game_data.load_list_room_items(data, ['room_1'])
        self.assertEqual(out_put, expected)


    def test_load_items(self):
        """
        Testing the Loading of items into the game
        """
        item = {'Description': 'A', 'Properties': 'B'}
        item_name = {'item_1': item}
        data = {'Items': item_name}
        expected = ['item_1']
        out_put = game_data.load_items(data)
        self.assertEqual(out_put, expected)


    def test_load_items_descriptions(self):
        """
        Testing the Loading of each item respective description
        """
        item = {'Description': 'A', 'Properties': 'B'}
        item_name = {'item_1': item}
        data = {'Items': item_name}
        expected = ['A']
        out_put = game_data.load_items_descriptions(data, ['item_1'])
        self.assertEqual(out_put, expected)
        


    def test_load_items_properties(self):
        """
        Testing the Loading of each item respective properties
        """
        item = {'Description': 'A', 'Properties': 'B'}
        item_name = {'item_1': item}
        data = {'Items': item_name}
        expected = ['B']
        out_put = game_data.load_items_properties(data, ['item_1'])
        self.assertEqual(out_put, expected)


    def test_load_player(self):
        """
        Testing the Loading of the player specs
        """
        player = {'Inventory': 'A', 'Position': 'B'}
        data = {'Player': player}
        expected = ('B', 'A')
        out_put = game_data.load_player(data)
        self.assertEqual(out_put, expected)