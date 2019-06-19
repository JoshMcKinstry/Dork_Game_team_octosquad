"""Test for room_printing"""
import unittest
from dork.room_printing import Room1Printing

class Room1PrintingTestCase(unittest.TestCase):
    """Test for room_printing"""

    def test_print_move(self):
        """Tests print_move"""
        assert Room1Printing.print_move("room 1", "north") == print(
            "You enter the boss room.")
        assert Room1Printing.print_move("room 1", "south") == print(
            "You cannot go/move south.")
        assert Room1Printing.print_move("room 1", "east") == print(
            "There is a table in the room with a donut on top.")
        assert Room1Printing.print_move("room 1", "west") == print(
            "There is a beautiful garden with the roadrunner's " +
            "nest right \nin the center of the garden. The nest " +
            "has eggs that look about \nready to hatch but no " +
            "roadrunner parent to be seen.")
        assert Room1Printing.print_move("room 2", "north") == print(
            "You are in the dean’s office. The dean is irritated " +
            "that you are \nin the room. You have 1 minute to " +
            "make him happy; otherwise, campus \nsecurity will " +
            "arrive and take you away.")
        assert Room1Printing.print_move("room 2", "south") == print(
            "You fall to your death.")
        assert Room1Printing.print_move("room 2", "east") == print(
            "You are unable to go East.")
        assert Room1Printing.print_move("room 2", "west") == print(
            "You are inside the Student Success Building. There " +
            "is a locked cage \nwith a roadrunner inside. " +
            "It looks starving and nervous. \nThere is a " +
            "piece of paper next to the cage.")
        assert Room1Printing.print_move("room 3", "north") == print(
            "You are in the dean’s office. The dean is irritated" +
            " that you are in \nthe room. You have 1 minute to " +
            "make him happy; otherwise, \ncampus security " +
            "will arrive and take you away.")
        assert Room1Printing.print_move("room 3", "south") == print(
            "You are unable to go South.")
        assert Room1Printing.print_move("room 3", "east") == print(
            "You are inside the Student Success Building. There " +
            "is a locked cage \nwith a roadrunner inside. " +
            "It looks starving and nervous. \nThere is a " +
            "piece of paper next to the cage.")
        assert Room1Printing.print_move("room 3", "west") == print(
            "You are unable to go West.")
        assert Room1Printing.print_move("room 4", "north") == print(
            "The blue door is unlocked, and you enter a room " +
            "with a gold key." + "The dean is blocking the door and " +
            "does not let you through. You cannot enter this room.")
        assert Room1Printing.print_move("room 4", "south") == print(
            "You are inside the Student Success Building. " +
            "There is a locked cage \nwith a roadrunner inside. " +
            "It looks starving and nervous. \nThere is a " +
            "piece of paper next to the cage.")
        assert Room1Printing.print_move("room 4", "east") == print(
            "There is a table in the room with a donut on top.")
        assert Room1Printing.print_move("room 4", "west") == print(
            "There is a beautiful garden with the roadrunner's " +
            "nest right \nin the center of the garden. The nest " +
            "has eggs that look about \nready to hatch but no " +
            "roadrunner parent to be seen.")
        assert Room1Printing.print_move("room 5", "north") == print(
            "You are unable to go North.")
        assert Room1Printing.print_move("room 5", "south") == print(
            "You are in the dean’s office. The dean is irritated" +
            " that you are in \nthe room. You have 1 minute to " +
            "make him happy; otherwise, \ncampus security " +
            "will arrive and take you away.")
        assert Room1Printing.print_move("room 5", "east") == print(
            "You are unable to go East.")
        assert Room1Printing.print_move("room 5", "west") == print(
            "You are unable to go West.")
        self.assertRaises(AssertionError, Room1Printing.print_move(None, None))

    def test_print_look(self):
        """Tests print_look"""
        assert Room1Printing.print_look("room 1", "north") == print(
            'There is a door with a sign that says DANGER.')

    def test_print_score(self):
        """Tests print_score"""
        assert Room1Printing.print_score(5) == print(
            "You have a score of " + str(5))

    def test_print_diagnostic(self):
        """Tests print_diagnostic"""
        assert Room1Printing.print_diagnostic(10) == print(
            "You have a health score of: " + str(10))

    def test_print_get(self):
        """Tests print_get"""
        assert Room1Printing.print_get("donut") == print(
            "You put the donut in your inventory")

    def test_print_read(self):
        """Tests print_read"""
        assert Room1Printing.print_read("paper") == print(
            "I don't like this bird. Dispose of it for me. - Dean")

    def test_print_drop_item(self):
        """Tests print_drop_item"""
        assert Room1Printing.print_drop_item() == print(
            "CHANGE THIS FOR FUTURE SPRINT")

    def test_print_open_item(self):
        """Tests print_open_item"""
        assert Room1Printing.print_open_item("cage") == print(
            "You successfully opened the cage" +
            ", and the bird hops on your shoulder. " +
            "The bird is added to your inventory.")

    def test_print_move_moveable(self):
        """Tests print_move_moveable"""
        assert Room1Printing.print_move_moveable() == print(
            "CHANGE THIS LATER")

    def test_print_attack(self):
        """Tests print_attack"""
        assert Room1Printing.print_attack("dean") == print(
            "You run up to the dean and start punching him. He is in " +
            "lots of pain but was able to call security to take " +
            "you away. GAME OVER.")

    def test_print_examine(self):
        """Tests print_examine"""
        assert Room1Printing.print_examine("paper") == print(
            "I don't "+ "like this bird. Dispose of it for me. - Dean")

    def test_print_inventory(self):
        """Tests print_inventory"""
        inventory_items = []
        inventory = "You currently have:"
        for items in inventory:
            inventory += (items + " ")
        assert Room1Printing.print_inventory(inventory_items) == print(
            inventory)

    def test_print_eat_food(self):
        """Tests print_eat_food"""
        assert Room1Printing.print_eat_food("donut") == print(
            "The donut is yummy. Unfortunately, the player dies " +
            "as THE DONUT IS POISONOUS!!! GAME OVER")

    def test_print_feed_creature(self):
        """Tests print_feed_creature"""
        assert Room1Printing.print_feed_creature("donut") == print(
            "Through one of the tiny openings in the cage, you drop " +
            "the donut into the cage. The roadrunner finished the " +
            "donut AND DIES!!! You figure out the donut is " +
            "poisonous! GAME OVER!")

    def test_print_give_item(self):
        """Tests print_give_item"""
        assert Room1Printing.print_give_item() == print(
            'CHANGE THIS LATER')

if __name__ == '__main__':
    unittest.main()
