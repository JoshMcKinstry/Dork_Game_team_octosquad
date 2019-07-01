"""A testing class for mainmenu"""
import unittest
import dork.menu as menu


class TestYamlReader(unittest.TestCase):
    """
    Testing the mainmenu module
    """

    def test_new_game(self):
        """
        Testing the new_game method
        """
        out_put = menu.new_game()
        self.assertIsInstance(out_put, tuple)
