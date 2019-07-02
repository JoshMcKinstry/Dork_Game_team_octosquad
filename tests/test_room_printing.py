"""Test for room_printing"""
from dork.room_printing import Room1Printing


def test_print_move(run):
    """Tests print_move"""
    out, _, _ = run(Room1Printing.print_move, 'room 1', 'north')
    assert out == 'You enter the boss room.\n'
    out, _, _ = run(Room1Printing.print_move, 'room 1', 'south')
    assert out == 'You cannot go/move south.\n'
    out, _, _ = run(Room1Printing.print_move, 'room 1', 'east')
    assert out == "There is a table in the room with a donut on top.\n"
    out, _, _ = run(Room1Printing.print_move, 'room 1', 'west')
    assert out == ("There is a beautiful garden with the roadrunner's" +
                   "nest right \nin the center of the garden. The nest " +
                   "has eggs that look about \nready to hatch but no " +
                   "roadrunner parent to be seen.\n")
    out, _, _ = run(Room1Printing.print_move, 'room 1', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_move, 'room 2', 'north')
    assert out == (
        "You are in the dean’s office. The dean is irritated " +
        "that you are \nin the room. You have 1 minute to " +
        "make him happy; otherwise, campus \nsecurity will " +
        "arrive and take you away.\n")
    out, _, _ = run(Room1Printing.print_move, 'room 2', 'south')
    assert out == "You fall to your death.\n"
    out, _, _ = run(Room1Printing.print_move, 'room 2', 'east')
    assert out == "You are unable to go East.\n"
    out, _, _ = run(Room1Printing.print_move, 'room 2', 'west')
    assert out == (
        "You are inside the Student Success Building. There " +
        "is a locked cage \nwith a roadrunner inside. " +
        "It looks starving and nervous. \nThere is a " +
        "piece of paper next to the cage.\n")
    out, _, _ = run(Room1Printing.print_move, 'room 2', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_move, 'room 3', 'north')
    assert out == (
        "You are in the dean’s office. The dean is irritated " +
        "that you are \nin the room. You have 1 minute to " +
        "make him happy; otherwise, campus \nsecurity will " +
        "arrive and take you away.\n")
    out, _, _ = run(Room1Printing.print_move, 'room 3', 'south')
    assert out == "You are unable to go South.\n"
    out, _, _ = run(Room1Printing.print_move, 'room 3', 'east')
    assert out == (
        "You are inside the Student Success Building. There " +
        "is a locked cage \nwith a roadrunner inside. " +
        "It looks starving and nervous. \nThere is a " +
        "piece of paper next to the cage.\n")
    out, _, _ = run(Room1Printing.print_move, 'room 3', 'west')
    assert out == "You are unable to go West.\n"
    out, _, _ = run(Room1Printing.print_move, 'room 3', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_move, 'room 4', 'north')
    assert out == (
        "The blue door is unlocked, and you enter a room " +
        "with a gold key." + "The dean is blocking the door and " +
        "does not let you through. You cannot enter this room.\n")
    out, _, _ = run(Room1Printing.print_move, 'room 4', 'south')
    assert out == (
        "You are inside the Student Success Building. " +
        "There is a locked cage \nwith a roadrunner inside. " +
        "It looks starving and nervous. \nThere is a " +
        "piece of paper next to the cage.\n")
    out, _, _ = run(Room1Printing.print_move, 'room 4', 'east')
    assert out == "There is a table in the room with a donut on top.\n"
    out, _, _ = run(Room1Printing.print_move, 'room 4', 'west')
    assert out == (
        "There is a beautiful garden with the roadrunner's " +
        "nest right \nin the center of the garden. The nest " +
        "has eggs that look about \nready to hatch but no " +
        "roadrunner parent to be seen.\n")
    out, _, _ = run(Room1Printing.print_move, 'room 4', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_move, 'room 5', 'north')
    assert out == "You are unable to go North.\n"
    out, _, _ = run(Room1Printing.print_move, 'room 5', 'south')
    assert out == (
        "You are in the dean’s office. The dean is irritated" +
        " that you are in \nthe room. You have 1 minute to " +
        "make him happy; otherwise, \ncampus security " +
        "will arrive and take you away.\n")
    out, _, _ = run(Room1Printing.print_move, 'room 5', 'east')
    assert out == "You are unable to go East.\n"
    out, _, _ = run(Room1Printing.print_move, 'room 5', 'west')
    assert out == "You are unable to go West.\n"


def test_print_look(run):
    """Tests print_look"""
    out, _, _ = run(Room1Printing.print_look, 'room 1', 'north')
    assert out == 'There is a door with a sign that says DANGER.\n'
    out, _, _ = run(Room1Printing.print_look, 'room 1', 'south')
    assert out == (
        "There is bag of bird food with all sorts of " +
        "insects that roadrunners love to eat.\n")
    out, _, _ = run(Room1Printing.print_look, 'room 1', 'east')
    assert out == "To the East, there is a sign that says Lounge.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 1', 'west')
    assert out == (
        "To the West, there is a sign that says " +
        "Roadrunner's Nest\n")
    out, _, _ = run(Room1Printing.print_look, 'room 1', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_look, 'room 2', 'north')
    assert out == "There is a sign that says DANGER!!\n"
    out, _, _ = run(Room1Printing.print_look, 'room 2', 'south')
    assert out == "There is a 1000 ft cliff with spikes.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 2', 'east')
    assert out == "There is an empty wall.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 2', 'west')
    assert out == (
        "There is a sign that says Student Success " +
        "Building.\n")
    out, _, _ = run(Room1Printing.print_look, 'room 2', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_look, 'room 3', 'north')
    assert out == "There is a sign that says DANGER!!\n"
    out, _, _ = run(Room1Printing.print_look, 'room 3', 'south')
    assert out == "There is an empty wall.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 3', 'east')
    assert out == "There is a sign that says Student Success Building.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 3', 'west')
    assert out == "There is an empty wall.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 3', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_look, 'room 4', 'north')
    assert out == "There is blue door that is being guarded by the dean.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 4', 'south')
    assert out == "There is a sign that says Student Success Building.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 4', 'east')
    assert out == "To the East, there is a sign that says Lounge.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 4', 'west')
    assert out == (
        "To the West, there is a sign that says " +
        "Roadrunner’s Nest.\n")
    out, _, _ = run(Room1Printing.print_look, 'room 4', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_look, 'room 5', 'north')
    assert out == "There is an empty wall.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 5', 'south')
    assert out == "There is a blue door\n"
    out, _, _ = run(Room1Printing.print_look, 'room 5', 'east')
    assert out == "There is an empty wall.\n"
    out, _, _ = run(Room1Printing.print_look, 'room 5', 'west')
    assert out == "There is an empty wall.\n"


def test_print_invalid(run):
    """
    Test invalid arguments
    """
    out, _, _ = run(Room1Printing.print_move, 'room 5', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_move, 'invalid', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_look, 'room 5', 'invalid')
    assert out == ''
    out, _, _ = run(Room1Printing.print_look, 'invalid', 'invalid')
    assert out == ''


def test_print_score(run):
    """Tests print_score"""
    out, _, _ = run(Room1Printing.print_score, 5)
    assert out == ("You have a score of " + str(5) + "\n")


def test_print_diagnostic(run):
    """Tests print_diagnostic"""
    out, _, _ = run(Room1Printing.print_diagnostic, 10)
    assert out == ("You have a health score of: " + str(10) + "\n")


def test_print_get(run):
    """Tests print_get"""
    out, _, _ = run(Room1Printing.print_get, 'donut')
    assert out == "You put the donut in your inventory\n"


def test_print_read(run):
    """Tests print_read"""
    out, _, _ = run(Room1Printing.print_read, 'paper')
    assert out == "I don't like this bird. Dispose of it for me. - Dean\n"
    out, _, _ = run(Room1Printing.print_read, 'notpaper')
    assert out == "notpaperwas not found\n"


def test_print_drop_item(run):
    """Tests print_drop_item"""
    out, _, _ = run(Room1Printing.print_drop_item)
    assert out == "CHANGE THIS FOR FUTURE SPRINT\n"


def test_print_open_item(run):
    """Tests print_open_item"""
    out, _, _ = run(Room1Printing.print_open_item, 'cage')
    assert out == (
        "You successfully opened the cage" +
        ", and the bird hops on your shoulder. " +
        "The bird is added to your inventory.\n")


def test_print_move_moveable(run):
    """Tests print_move_moveable"""
    out, _, _ = run(Room1Printing.print_move_moveable)
    assert out == ("CHANGE THIS LATER\n")


def test_print_attack(run):
    """Tests print_attack"""
    out, _, _ = run(Room1Printing.print_attack, 'dean')
    assert out == (
        "You run up to the dean and start punching him. He is in " +
        "lots of pain but was able to call security to take " +
        "you away. GAME OVER.\n")
    out, _, _ = run(Room1Printing.print_attack, 'bob')
    assert out == "You cannot attack bob\n"


def test_print_examine(run):
    """Tests print_examine"""
    out, _, _ = run(Room1Printing.print_examine, 'paper')
    assert out == (
        "I don't " + "like this bird. Dispose of it for me. - Dean\n")
    out, _, _ = run(Room1Printing.print_examine, 'roadrunner')
    assert out == (
        "The roadrunner is in bad condition. It looks starving " +
        "and nervous.\n")
    out, _, _ = run(Room1Printing.print_examine, 'cage')
    assert out == "The cage is tight, dirty, and locked.\n"
    out, _, _ = run(Room1Printing.print_examine, 'whatever')
    assert out == "whatever is unable to be examined\n"


def test_print_inventory(run):
    """Tests print_inventory"""
    inventory_items = ["donut"]
    out, _, _ = run(Room1Printing.print_inventory, inventory_items)
    assert out == "You currently have:\ndonut\n"


def test_print_eat_food(run):
    """Tests print_eat_food"""
    out, _, _ = run(Room1Printing.print_eat_food, 'donut')
    assert out == (
        "The donut is yummy. Unfortunately, the player dies " +
        "as THE DONUT IS POISONOUS!!! GAME OVER\n")
    out, _, _ = run(Room1Printing.print_eat_food, 'fruit')
    assert out == "fruit is not something you can eat.\n"


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
