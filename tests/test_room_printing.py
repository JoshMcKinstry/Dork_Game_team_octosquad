"""Test for room_printing"""
import unittest
from dork.room_printing import Room1Printing
# from dork.command_manager import CommandManager


class Room1PrintingTestCase(unittest.TestCase):
    """Test for room_printing"""

    @classmethod
    def test_print_move(cls):
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

    @classmethod
    def test_print_look(cls):
        """Tests print_look"""
        assert Room1Printing.print_look("room 1", "north") == print(
            'There is a door with a sign that says DANGER.')
        assert Room1Printing.print_look("room 1", "south") == print(
            "There is bag of bird food with all sorts of " +
            "insects that roadrunners love to eat.")
        assert Room1Printing.print_look("room 1", "east") == print(
            "To the East, there is a sign that says Lounge.")
        assert Room1Printing.print_look("room 1", "west") == print(
            "To the West, there is a sign that says " +
            "Roadrunner's Nest")
        assert Room1Printing.print_look("room 2", "north") == print(
            "There is a sign that says DANGER!!")
        assert Room1Printing.print_look("room 2", "south") == print(
            "There is a 1000 ft cliff with spikes.")
        assert Room1Printing.print_look("room 2", "east") == print(
            "There is an empty wall.")
        assert Room1Printing.print_look("room 2", "west") == print(
            "There is a sign that says Student Success " +
            "Building.")
        assert Room1Printing.print_look("room 3", "north") == print(
            "There is a sign that says DANGER!!")
        assert Room1Printing.print_look("room 3", "south") == print(
            "There is an empty wall.")
        assert Room1Printing.print_look("room 3", "east") == print(
            "There is a sign that says Student Success Building.")
        assert Room1Printing.print_look("room 3", "west") == print(
            "There is an empty wall.")
        assert Room1Printing.print_look("room 4", "north") == print(
            "There is blue door that is being guarded by the dean.")
        assert Room1Printing.print_look("room 4", "south") == print(
            "There is a sign that says Student Success Building.")
        assert Room1Printing.print_look("room 4", "east") == print(
            "To the East, there is a sign that says Lounge.")
        assert Room1Printing.print_look("room 4", "west") == print(
            "To the West, there is a sign that says " +
            "Roadrunner’s Nest.")
        assert Room1Printing.print_look("room 5", "north") == print(
            "There is an empty wall.")
        assert Room1Printing.print_look("room 5", "south") == print(
            "There is a blue door")
        assert Room1Printing.print_look("room 5", "east") == print(
            "There is an empty wall.")
        assert Room1Printing.print_look("room 5", "west") == print(
            "There is an empty wall.")

    @classmethod
    def test_print_score(cls):
        """Tests print_score"""
        assert Room1Printing.print_score(5) == print(
            "You have a score of " + str(5))

    @classmethod
    def test_print_diagnostic(cls):
        """Tests print_diagnostic"""
        assert Room1Printing.print_diagnostic(10) == print(
            "You have a health score of: " + str(10))

    @classmethod
    def test_print_get(cls):
        """Tests print_get"""
        assert Room1Printing.print_get("donut") == print(
            "You put the donut in your inventory")

    @classmethod
    def test_print_read(cls):
        """Tests print_read"""
        assert Room1Printing.print_read("paper") == print(
            "I don't like this bird. Dispose of it for me. - Dean")
        assert Room1Printing.print_read("notpaper") == print(
            "notpaper was not found")

    @classmethod
    def test_print_drop_item(cls):
        """Tests print_drop_item"""
        assert Room1Printing.print_drop_item() == print(
            "CHANGE THIS FOR FUTURE SPRINT")

    @classmethod
    def test_print_open_item(cls):
        """Tests print_open_item"""
        assert Room1Printing.print_open_item("cage") == print(
            "You successfully opened the cage" +
            ", and the bird hops on your shoulder. " +
            "The bird is added to your inventory.")

    @classmethod
    def test_print_move_moveable(cls):
        """Tests print_move_moveable"""
        assert Room1Printing.print_move_moveable() == print(
            "CHANGE THIS LATER")

    @classmethod
    def test_print_attack(cls):
        """Tests print_attack"""
        # command_manage = CommandManager()
        assert Room1Printing.print_attack("dean") == print(
            "You run up to the dean and start punching him. He is in " +
            "lots of pain but was able to call security to take " +
            "you away. GAME OVER.")
        # if Room1Printing.print_attack("dean"):
        # assert command_manage.set_game_over(True)
        assert Room1Printing.print_attack("bob") == print(
            "You cannot attack bob")

    @classmethod
    def test_print_examine(cls):
        """Tests print_examine"""
        assert Room1Printing.print_examine("paper") == print(
            "I don't " + "like this bird. Dispose of it for me. - Dean")
        assert Room1Printing.print_examine("roadrunner") == print(
            "The roadrunner is in bad condition. It looks starving " +
            "and nervous.")
        assert Room1Printing.print_examine("cage") == print(
            "The cage is tight, dirty, and locked.")
        assert Room1Printing.print_examine("whatever") == print(
            "whatever is unable to be examined")

    @classmethod
    def test_print_inventory(cls):
        """Tests print_inventory"""
        inventory_items = ["donut"]
        inventory = "You currently have:"
        for items in inventory:
            inventory += (str(items) + " ")
        assert Room1Printing.print_inventory(inventory_items) == print(
            inventory)

    @classmethod
    def test_print_eat_food(cls):
        """Tests print_eat_food"""
        assert Room1Printing.print_eat_food("donut") == print(
            "The donut is yummy. Unfortunately, the player dies " +
            "as THE DONUT IS POISONOUS!!! GAME OVER")
        assert Room1Printing.print_eat_food("fruit") == print(
            "fruit is not something you can eat.")

    @classmethod
    def test_print_feed_creature(cls):
        """Tests print_feed_creature"""
        assert Room1Printing.print_feed_creature("donut") == print(
            "Through one of the tiny openings in the cage, you drop " +
            "the donut into the cage. The roadrunner finished the " +
            "donut AND DIES!!! You figure out the donut is " +
            "poisonous! GAME OVER!")
        assert Room1Printing.print_feed_creature("bird food") == print(
            "Through one of the tiny openings in the cage, you " +
            "drop some bird food into the cage. The roadrunner " +
            "eats the food and seems energized.")
        assert Room1Printing.print_feed_creature(None) == print(
            "There is nothing to feed the bird with.")

    @classmethod
    def test_print_give_item(cls):
        """Tests print_give_item"""
        assert Room1Printing.print_give_item() == print(
            'CHANGE THIS LATER')


if __name__ == '__main__':
    unittest.main()
