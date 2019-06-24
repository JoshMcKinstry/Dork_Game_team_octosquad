"""This class acts as the controller for the game"""
from dork.room_printing import Room1Printing


class CommandManager:
    """cli controller"""

    def __init__(self):
        self.game_over = False
        self.input_line = ""
        self.input_helper = ""
        self.player_inventory = [""]
        print("Welcome to Dork")

    def check_game_over(self):
        """
        Check if the game is over
        """
        return self.game_over

    def set_game_over(self, cond):
        """
        Method for conditional termination of the game
        """
        if cond is True:
            self.game_over = True
        if cond is not True:
            self.game_over = False

    def read_command(self):
        """
        Reads command from the console, translates and returns the command
        """

        move = ['move', 'walk', 'run', 'skip', 'go']

        look = ['look', 'see', 'peer', 'view']
        get = ['grab', 'get', 'take']
        put = ['put', 'set', 'lay']

        eat = ['eat']
        feed = ['feed']
        inventory = ['inventory']

        self.input_line = input("")

        if len(self.input_line) == 1:
            self.direction_shorts()
        elif (self.input_line[0:2] in move or
              self.input_line[0:3] in move) and (len(self.input_line) < 6):
            self.input_line = "go"
        elif (self.input_line[0:4] in move or
              self.input_line[0:5] in move) and (len(self.input_line) < 6):
            self.input_line = "go"
        elif self.input_line[0:3] in put:
            self.input_helper = self.input_line[4:len(self.input_line)]
            self.input_line = "put"
        elif self.input_line[0:3] in get:
            self.input_helper = self.input_line[4:len(self.input_line)]
            self.input_line = "get"
        elif self.input_line[0:4] in get:
            self.input_helper = self.input_line[5:len(self.input_line)]
            self.input_line = "get"
        elif self.input_line[0:3] in look:
            self.input_helper = self.input_line[4:len(self.input_line)]
            self.input_line = "look"
        elif self.input_line[0:4] in look:
            self.input_helper = self.input_line[5:len(self.input_line)]
            self.input_line = "look"
        elif self.input_line[0:3] in eat:
            self.input_helper = self.input_line[4:len(self.input_line)]
            self.input_line = "eat"
        elif self.input_line[0:4] in feed:
            self.input_helper = self.input_line[5:len(self.input_line)]
            self.input_line = "feed"
        elif self.input_line in inventory:
            self.input_line = "inventory"

    def direction_shorts(self):
        """
        Handles all of the shortcut moves
        """
        if self.input_line == "n":
            self.input_line = "go north"
        elif self.input_line == "s":
            self.input_line = "go south"
        elif self.input_line == "e":
            self.input_line = "go east"
        elif self.input_line == "w":
            self.input_line = "go west"

    def execute_move(self):
        """
        Handles all of the move commands
        """
        room_one_prints = Room1Printing()
        if self.input_line[0:8] == "go north":
            room_one_prints.print_move("room 1", "north")
        elif self.input_line[0:8] == "go south":
            room_one_prints.print_move("room 1", "south")
        elif self.input_line[0:7] == "go east":
            room_one_prints.print_move("room 1", "east")
        elif self.input_line[0:7] == "go west":
            room_one_prints.print_move("room 1", "west")
        elif self.input_line == "go":
            print("Go where?")

    def execute_command(self):
        """
        Takes the command from previous method if valid and returns the result
        """
        room_one_prints = Room1Printing()
        if self.input_line == "exit":
            print("Bye!")
            self.set_game_over(True)
        elif self.input_line[0:2] == "go":
            self.execute_move()
        elif self.input_line == "look":
            room_one_prints.print_look("room 1", self.input_helper)
            direction = ['north', 'south', 'east', 'west']
            if self.input_helper not in direction:
                room_one_prints.print_examine(self.input_helper)
        elif self.input_line == "get":
            room_one_prints.print_get(self.input_helper)
            self.player_inventory.append(self.input_helper)
        elif self.input_line == "put":
            print("Put not ready")
        elif self.input_line == "eat":
            room_one_prints.print_eat_food(self.input_helper)
        elif self.input_line == "feed":
            room_one_prints.print_feed_creature(self.input_helper)
        elif self.input_line == "inventory":
            room_one_prints.print_inventory(self.player_inventory)
            print("Inventory:")
        else:
            print("Invalid Command!")
