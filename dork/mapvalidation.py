"""
A class that validates a maze coming from a .yml/.yaml file
"""


class ValidMaze:
    """
    A valid maze
    """

    @staticmethod
    def load_rooms(maze):
        """
        Loading the room names
        """
        for room_name in maze:
            room_names = list(maze[room_name].keys())
        return room_names

    @staticmethod
    def load_cardinals(maze):
        """
        Loading the room cardinals
        """
        for room_name in maze:
            room_cardinals = list(maze[room_name].values())
        return room_cardinals

    @staticmethod
    def check_rooms(room_names):
        """
        Checking room names for valid names
        """
        return None in room_names

    @staticmethod
    def check_cardinals(room_cardinals):
        """
        Checking for valid cardinals in each room
        """
        valid_cardinals = ['north', 'east', 'south', 'west']
        invalid_cardinal = False
        scope = range(len(room_cardinals))
        for i in scope:
            if list(room_cardinals[i].keys()) != valid_cardinals:
                invalid_cardinal = True
                break
        return invalid_cardinal

    @staticmethod
    def check_connections(room_names, room_cardinals):
        """
        Checking for cardinals to be pointing to unique and valid directions
        """
        dual_pointer = False
        invalid_direction = False
        isolated_room = False
        scope = range(len(room_cardinals))
        for i in scope:
            adjacent_rooms = list(room_cardinals[i].values())
            adjacent_rooms[:] = (
                room for room in adjacent_rooms if room is not None)
            unique_rooms = set(adjacent_rooms)
            if len(adjacent_rooms) != len(unique_rooms):
                dual_pointer = True
                break
            elif not set(adjacent_rooms).issubset(set(room_names)):
                invalid_direction = True
                break
            elif unique_rooms.issubset({None}):
                isolated_room = True
                break
        return dual_pointer or invalid_direction or isolated_room
