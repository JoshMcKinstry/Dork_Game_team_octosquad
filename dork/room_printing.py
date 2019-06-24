"""This class prints message to user"""


class Room1Printing():
    """This class prints messages"""

    @classmethod
    def print_move(cls, room, direction):
        """
        Prints a statement to user after player moves a certain direction
        """
        direction_room1 = {
            'north': "You enter the boss room.",
            'south': "You cannot go/move south.",
            'east': "There is a table in the room with a donut on top.",
            'west': "There is a beautiful garden with the roadrunner's" +
                    "nest right \nin the center of the garden. The nest " +
                    "has eggs that look about \nready to hatch but no " +
                    "roadrunner parent to be seen."}
        direction_room2 = {
            'north': "You are in the dean’s office. The dean is irritated " +
                     "that you are \nin the room. You have 1 minute to " +
                     "make him happy; otherwise, campus \nsecurity will " +
                     "arrive and take you away.",
            'south': "You fall to your death.",
            'east': "You are unable to go East.",
            'west': "You are inside the Student Success Building. There " +
                    "is a locked cage \nwith a roadrunner inside. " +
                    "It looks starving and nervous. \nThere is a " +
                    "piece of paper next to the cage."}
        direction_room3 = {
            'north': "You are in the dean’s office. The dean is irritated " +
                     "that you are \nin the room. You have 1 minute to " +
                     "make him happy; otherwise, campus \nsecurity will " +
                     "arrive and take you away.",
            'south': "You are unable to go South.",
            'east': "You are inside the Student Success Building. There " +
                    "is a locked cage \nwith a roadrunner inside. " +
                    "It looks starving and nervous. \nThere is a " +
                    "piece of paper next to the cage.",
            'west': "You are unable to go West."}
        direction_room4 = {
            'north': "The blue door is unlocked, and you enter a room " +
                     "with a gold key.The dean is blocking the door and " +
                     "does not let you through. You cannot enter this room.",
            'south': "You are inside the Student Success Building. " +
                     "There is a locked cage \nwith a roadrunner inside. " +
                     "It looks starving and nervous. \nThere is a " +
                     "piece of paper next to the cage.",
            'east': "There is a table in the room with a donut on top.",
            'west': "There is a beautiful garden with the roadrunner's " +
                    "nest right \nin the center of the garden. The nest " +
                    "has eggs that look about \nready to hatch but no " +
                    "roadrunner parent to be seen."}
        direction_room5 = {
            'north': "You are unable to go North.",
            'south': "You are in the dean’s office. The dean is irritated" +
                     " that you are in \nthe room. You have 1 minute to " +
                     "make him happy; otherwise, \ncampus security " +
                     "will arrive and take you away.",
            'east': "You are unable to go East.",
            'west': "You are unable to go West."}

        if room == "room 1":
            if direction in direction_room1:
                print(direction_room1[direction])

        elif room == "room 2":
            if direction in direction_room2:
                print(direction_room2[direction])

        elif room == "room 3":
            if direction in direction_room3:
                print(direction_room3[direction])

        elif room == "room 4":
            if direction in direction_room4:
                print(direction_room4[direction])

        elif room == "room 5":
            if direction in direction_room5:
                print(direction_room5[direction])

    @classmethod
    def print_look(cls, room, direction):
        """
        Prints a statement after user looks a certain direction
        """
        direction_room1 = {
            'north': "There is a door with a sign that says DANGER.",
            'south': "There is bag of bird food with all sorts of " +
                     "insects that roadrunners love to eat.",
            'east': "To the East, there is a sign that says Lounge.",
            'west': "To the West, there is a sign that says " +
                    "Roadrunner's Nest"}
        direction_room2 = {
            'north': "There is a sign that says DANGER!!",
            'south': "There is a 1000 ft cliff with spikes.",
            'east': "There is an empty wall.",
            'west': "There is a sign that says Student Success " +
                    "Building."}
        direction_room3 = {
            'north': "There is a sign that says DANGER!!",
            'south': "There is an empty wall.",
            'east': "There is a sign that says Student Success Building.",
            'west': "There is an empty wall."}
        direction_room4 = {
            'north': "There is blue door that is being guarded by the dean.",
            'south': "There is a sign that says Student Success Building.",
            'east': "To the East, there is a sign that says Lounge.",
            'west': "To the West, there is a sign that says " +
                    "Roadrunner’s Nest."}
        direction_room5 = {
            'north': "There is an empty wall.",
            'south': "There is a blue door",
            'east': "There is an empty wall.",
            'west': "There is an empty wall."}

        if room == "room 1":
            if direction in direction_room1:
                print(direction_room1[direction])

        elif room == "room 2":
            if direction in direction_room2:
                print(direction_room2[direction])

        elif room == "room 3":
            if direction in direction_room3:
                print(direction_room3[direction])

        elif room == "room 4":
            if direction in direction_room4:
                print(direction_room4[direction])

        elif room == "room 5":
            if direction in direction_room5:
                print(direction_room5[direction])

    @classmethod
    def print_score(cls, score):
        """
        Prints out the score
        """
        print("You have a score of " + str(score))

    @classmethod
    def print_diagnostic(cls, health_score):
        """
        Prints out the health data of the player
        """
        print("You have a health score of: " + str(health_score))

    @classmethod
    def print_get(cls, item):
        """
        Prints the item stored into player inventory
        """
        print("You put the " + item + " in your inventory")

    @classmethod
    def print_read(cls, item):
        """
        Prints the item that is being read.
        """
        if item == "paper":
            print("I don't like this bird. Dispose of it for me. - Dean")
        else:
            print(item + "was not found")

    @classmethod
    def print_drop_item(cls):
        """
        Print the item being dropped
        """
        print("CHANGE THIS FOR FUTURE SPRINT")

    @classmethod
    def print_open_item(cls, item):
        """
        Print what happens after player open the item.
        """
        print("You successfully opened the " + item +
              ", and the bird hops on your shoulder. " +
              "The bird is added to your inventory.")
        # Call the add_inventory() method here

    @classmethod
    def print_move_moveable(cls):
        """
        Prints what happens after the item is moved
        """
        print("CHANGE THIS LATER")

    @classmethod
    def print_attack(cls, creature):
        """
        Prints out what happens after the player attacks a creature
        """
        if creature == "dean":
            print("You run up to the dean and start punching him. He is in " +
                  "lots of pain but was able to call security to take " +
                  "you away. GAME OVER.")
            # import sys
            # sys.exit(0)
        else:
            print("You cannot attack " + creature)

    @classmethod
    def print_examine(cls, item):
        """
        Print out what happens when the player examines an item
        """
        if item == "paper":
            print("I don't " + "like this bird. Dispose of it for me. - Dean")
        elif item == "roadrunner":
            print("The roadrunner is in bad condition. It looks starving " +
                  "and nervous.")
        elif item == "cage":
            print("The cage is tight, dirty, and locked.")
        else:
            print(item + " is unable to be examined")

    @classmethod
    def print_inventory(cls, inventory):
        """
        Print out the player's inventory
        """
        print("You currently have:")
        for items in inventory:
            print(str(items) + " ")

    @classmethod
    def print_eat_food(cls, item):
        """
        Print out what happens after player eats item.
        """
        if item == "donut":
            print("The donut is yummy. Unfortunately, the player dies " +
                  "as THE DONUT IS POISONOUS!!! GAME OVER")
            # import sys
            # sys.exit(0)
        else:
            print(item + "is not something you can eat.")

    @classmethod
    def print_feed_creature(cls, food):
        """
        Print what happens after player feeds the runner
        """
        if food == "donut":
            print("Through one of the tiny openings in the cage, you drop " +
                  "the donut into the cage. The roadrunner finished the " +
                  "donut AND DIES!!! You figure out the donut is " +
                  "poisonous! GAME OVER!")
            # import sys
            # sys.exit(0)
        if food == "bird food":
            print("Through one of the tiny openings in the cage, you " +
                  "drop some bird food into the cage. The roadrunner " +
                  "eats the food and seems energized.")
        if food is None:
            print("There is nothing to feed the bird with.")

    @classmethod
    def print_give_item(cls):
        """
        Print what happens after player gives the item
        """
        print("CHANGE THIS LATER")
