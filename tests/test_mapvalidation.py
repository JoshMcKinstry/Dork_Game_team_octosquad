"""
A test for mapvalidation
"""
import unittest
from dork.mapvalidation import ValidMaze


class TestValidMaze(unittest.TestCase):
    """
    A testing class for ValidMaze
    """
    def test_load_rooms(self):
        """
        Testing the loading rooms methods
        """
        maze = ValidMaze()
        dummy_maze = {'Entrance': {'North': 'Main Hall'}}
        flag = isinstance(maze.load_rooms(dummy_maze), list)
        self.assertTrue(flag)

    def test_load_cardinals(self):
        """
        Testing the loading cardinal methods
        """
        maze = ValidMaze()
        dummy_maze = {'Entrance': {'North': 'Main Hall'}}
        flag = isinstance(maze.load_cardinals(dummy_maze), list)
        self.assertTrue(flag)

    def test_check_rooms(self):
        """
        Testing the check room methods
        """
        maze = ValidMaze()
        room_names = [None]
        self.assertTrue(maze.check_rooms(room_names))

    def test_check_cardinals(self):
        """
        Testing the check cardinal method
        """
        maze = ValidMaze()
        invalidad_cardinals = [
            {'Home': None, 'School': None, 'Office': None, 'Gym': None}]
        invalid_flag = maze.check_cardinals(invalidad_cardinals)
        self.assertTrue(invalid_flag)

    def test_check_connections(self):
        """
        Testing the check connections method
        """
        maze = ValidMaze()
        room_names = ['Cave', 'Armory', 'Gold', 'Boss']
        dual_pointer = [
            {'north': 'Cave', 'east': 'Cave', 'south': None, 'west': None}]
        invalid_pointer = [
            {'north': 'Cave', 'east': 'Armory',
             'south': 'Gold', 'west': 'Lake'}]
        isolated_room = [
            {'north': None, 'east': None,
             'south': None, 'west': None}]
        first_case = maze.check_connections(room_names, dual_pointer)
        second_case = maze.check_connections(room_names, invalid_pointer)
        third_case = maze.check_connections(room_names, isolated_room)
        self.assertTrue(first_case)
        self.assertTrue(second_case)
        self.assertTrue(third_case)


if __name__ == "__main__":
    unittest.main()
