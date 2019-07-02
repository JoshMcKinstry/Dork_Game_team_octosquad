"""Test for room_printing"""
from dork.room_printing import Room1Printing


def test_print_move(run):
    """Tests print_move"""
    output, _, _ = run(Room1Printing.print_move, 'room 1', 'north')
    assert output == 'You enter the boss room.\n'
    output, _, _ = run(Room1Printing.print_move, 'room 1', 'south')
    assert output == 'You cannot go/move south.\n'
    output, _, _ = run(Room1Printing.print_move, 'room 1', 'east')
    assert output == "There is a table in the room with a donut on top.\n"
    output, _, _ = run(Room1Printing.print_move, 'room 1', 'west')
    assert output == ("There is a beautiful garden with the roadrunner's" +
                   "nest right \nin the center of the garden. The nest " +
                   "has eggs that look about \nready to hatch but no " +
                   "roadrunner parent to be seen.\n")
    output, _, _ = run(Room1Printing.print_move, 'room 1', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_move, 'room 2', 'north')
    assert output == (
        "You are in the dean’s office. The dean is irritated " +
        "that you are \nin the room. You have 1 minute to " +
        "make him happy; otherwise, campus \nsecurity will " +
        "arrive and take you away.\n")
    output, _, _ = run(Room1Printing.print_move, 'room 2', 'south')
    assert output == "You fall to your death.\n"
    output, _, _ = run(Room1Printing.print_move, 'room 2', 'east')
    assert output == "You are unable to go East.\n"
    output, _, _ = run(Room1Printing.print_move, 'room 2', 'west')
    assert output == (
        "You are inside the Student Success Building. There " +
        "is a locked cage \nwith a roadrunner inside. " +
        "It looks starving and nervous. \nThere is a " +
        "piece of paper next to the cage.\n")
    output, _, _ = run(Room1Printing.print_move, 'room 2', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_move, 'room 3', 'north')
    assert output == (
        "You are in the dean’s office. The dean is irritated " +
        "that you are \nin the room. You have 1 minute to " +
        "make him happy; otherwise, campus \nsecurity will " +
        "arrive and take you away.\n")
    output, _, _ = run(Room1Printing.print_move, 'room 3', 'south')
    assert output == "You are unable to go South.\n"
    output, _, _ = run(Room1Printing.print_move, 'room 3', 'east')
    assert output == (
        "You are inside the Student Success Building. There " +
        "is a locked cage \nwith a roadrunner inside. " +
        "It looks starving and nervous. \nThere is a " +
        "piece of paper next to the cage.\n")
    output, _, _ = run(Room1Printing.print_move, 'room 3', 'west')
    assert output == "You are unable to go West.\n"
    output, _, _ = run(Room1Printing.print_move, 'room 3', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_move, 'room 4', 'north')
    assert output == (
        "The blue door is unlocked, and you enter a room " +
        "with a gold key." + "The dean is blocking the door and " +
        "does not let you through. You cannot enter this room.\n")
    output, _, _ = run(Room1Printing.print_move, 'room 4', 'south')
    assert output == (
        "You are inside the Student Success Building. " +
        "There is a locked cage \nwith a roadrunner inside. " +
        "It looks starving and nervous. \nThere is a " +
        "piece of paper next to the cage.\n")
    output, _, _ = run(Room1Printing.print_move, 'room 4', 'east')
    assert output == "There is a table in the room with a donut on top.\n"
    output, _, _ = run(Room1Printing.print_move, 'room 4', 'west')
    assert output == (
        "There is a beautiful garden with the roadrunner's " +
        "nest right \nin the center of the garden. The nest " +
        "has eggs that look about \nready to hatch but no " +
        "roadrunner parent to be seen.\n")
    output, _, _ = run(Room1Printing.print_move, 'room 4', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_move, 'room 5', 'north')
    assert output == "You are unable to go North.\n"
    output, _, _ = run(Room1Printing.print_move, 'room 5', 'south')
    assert output == (
        "You are in the dean’s office. The dean is irritated" +
        " that you are in \nthe room. You have 1 minute to " +
        "make him happy; otherwise, \ncampus security " +
        "will arrive and take you away.\n")
    output, _, _ = run(Room1Printing.print_move, 'room 5', 'east')
    assert output == "You are unable to go East.\n"
    output, _, _ = run(Room1Printing.print_move, 'room 5', 'west')
    assert output == "You are unable to go West.\n"


def test_print_look(run):
    """Tests print_look"""
    output, _, _ = run(Room1Printing.print_look, 'room 1', 'north')
    assert output == 'There is a door with a sign that says DANGER.\n'
    output, _, _ = run(Room1Printing.print_look, 'room 1', 'south')
    assert output == (
        "There is bag of bird food with all sorts of " +
        "insects that roadrunners love to eat.\n")
    output, _, _ = run(Room1Printing.print_look, 'room 1', 'east')
    assert output == "To the East, there is a sign that says Lounge.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 1', 'west')
    assert output == (
        "To the West, there is a sign that says " +
        "Roadrunner's Nest\n")
    output, _, _ = run(Room1Printing.print_look, 'room 1', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_look, 'room 2', 'north')
    assert output == "There is a sign that says DANGER!!\n"
    output, _, _ = run(Room1Printing.print_look, 'room 2', 'south')
    assert output == "There is a 1000 ft cliff with spikes.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 2', 'east')
    assert output == "There is an empty wall.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 2', 'west')
    assert output == (
        "There is a sign that says Student Success " +
        "Building.\n")
    output, _, _ = run(Room1Printing.print_look, 'room 2', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_look, 'room 3', 'north')
    assert output == "There is a sign that says DANGER!!\n"
    output, _, _ = run(Room1Printing.print_look, 'room 3', 'south')
    assert output == "There is an empty wall.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 3', 'east')
    assert output == "There is a sign that says Student Success Building.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 3', 'west')
    assert output == "There is an empty wall.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 3', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_look, 'room 4', 'north')
    assert output == "There is blue door that is being guarded by the dean.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 4', 'south')
    assert output == "There is a sign that says Student Success Building.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 4', 'east')
    assert output == "To the East, there is a sign that says Lounge.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 4', 'west')
    assert output == (
        "To the West, there is a sign that says " +
        "Roadrunner’s Nest.\n")
    output, _, _ = run(Room1Printing.print_look, 'room 4', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_look, 'room 5', 'north')
    assert output == "There is an empty wall.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 5', 'south')
    assert output == "There is a blue door\n"
    output, _, _ = run(Room1Printing.print_look, 'room 5', 'east')
    assert output == "There is an empty wall.\n"
    output, _, _ = run(Room1Printing.print_look, 'room 5', 'west')
    assert output == "There is an empty wall.\n"


def test_print_invalid(run):
    """
    Test invalid arguments
    """
    output, _, _ = run(Room1Printing.print_move, 'room 5', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_move, 'invalid', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_look, 'room 5', 'invalid')
    assert output == ''
    output, _, _ = run(Room1Printing.print_look, 'invalid', 'invalid')
    assert output == ''


def test_print_score(run):
    """Tests print_score"""
    output, _, _ = run(Room1Printing.print_score, 5)
    assert output == ("You have a score of " + str(5) + "\n")


def test_print_diagnostic(run):
    """Tests print_diagnostic"""
    output, _, _ = run(Room1Printing.print_diagnostic, 10)
    assert output == ("You have a health score of: " + str(10) + "\n")


def test_print_get(run):
    """Tests print_get"""
    output, _, _ = run(Room1Printing.print_get, 'donut')
    assert output == "You put the donut in your inventory\n"


def test_print_read(run):
    """Tests print_read"""
    output, _, _ = run(Room1Printing.print_read, 'paper')
    assert output == "I don't like this bird. Dispose of it for me. - Dean\n"
    output, _, _ = run(Room1Printing.print_read, 'notpaper')
    assert output == "notpaperwas not found\n"


def test_print_drop_item(run):
    """Tests print_drop_item"""
    output, _, _ = run(Room1Printing.print_drop_item)
    assert output == "CHANGE THIS FOR FUTURE SPRINT\n"


def test_print_open_item(run):
    """Tests print_open_item"""
    output, _, _ = run(Room1Printing.print_open_item, 'cage')
    assert output == (
        "You successfully opened the cage" +
        ", and the bird hops on your shoulder. " +
        "The bird is added to your inventory.\n")


def test_print_move_moveable(run):
    """Tests print_move_moveable"""
    output, _, _ = run(Room1Printing.print_move_moveable)
    assert output == ("CHANGE THIS LATER\n")


def test_print_attack(run):
    """Tests print_attack"""
    output, _, _ = run(Room1Printing.print_attack, 'dean')
    assert output == (
        "You run up to the dean and start punching him. He is in " +
        "lots of pain but was able to call security to take " +
        "you away. GAME OVER.\n")
    output, _, _ = run(Room1Printing.print_attack, 'bob')
    assert output == "You cannot attack bob\n"


def test_print_examine(run):
    """Tests print_examine"""
    output, _, _ = run(Room1Printing.print_examine, 'paper')
    assert output == (
        "I don't " + "like this bird. Dispose of it for me. - Dean\n")
    output, _, _ = run(Room1Printing.print_examine, 'roadrunner')
    assert output == (
        "The roadrunner is in bad condition. It looks starving " +
        "and nervous.\n")
    output, _, _ = run(Room1Printing.print_examine, 'cage')
    assert output == "The cage is tight, dirty, and locked.\n"
    output, _, _ = run(Room1Printing.print_examine, 'whatever')
    assert output == "whatever is unable to be examined\n"


def test_print_inventory(run):
    """Tests print_inventory"""
    inventory_items = ["donut"]
    output, _, _ = run(Room1Printing.print_inventory, inventory_items)
    assert output == "You currently have:\ndonut\n"


def test_print_eat_food(run):
    """Tests print_eat_food"""
    output, _, _ = run(Room1Printing.print_eat_food, 'donut')
    assert output == (
        "The donut is yummy. Unfortunately, the player dies " +
        "as THE DONUT IS POISONOUS!!! GAME OVER\n")
    output, _, _ = run(Room1Printing.print_eat_food, 'fruit')
    assert output == "fruit is not something you can eat.\n"


def test_print_feed_creature(run):
    """Tests print_feed_creature"""
    output, _, _ = run(Room1Printing.print_feed_creature, 'donut')
    assert output == (
        "Through one of the tiny openings in the cage, you drop " +
        "the donut into the cage. The roadrunner finished the " +
        "donut AND DIES!!! You figure out the donut is " +
        "poisonous! GAME OVER!\n")
    output, _, _ = run(Room1Printing.print_feed_creature, 'bird food')
    assert output == (
        "Through one of the tiny openings in the cage, you " +
        "drop some bird food into the cage. The roadrunner " +
        "eats the food and seems energized.\n")
    output, _, _ = run(Room1Printing.print_feed_creature, None)
    assert output == "There is nothing to feed the bird with.\n"


def test_print_give_item(run):
    """Tests print_give_item"""
    output, _, _ = run(Room1Printing.print_give_item)
    assert output == 'CHANGE THIS LATER\n'
