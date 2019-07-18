"""
A test for game_engine
"""
import unittest
from mock import patch
import dork.game_engine as engine


class TestValidMaze(unittest.TestCase):
    """
    A testing class for ValidMaze
    """

    def test_loading_map(self):
        """
        Testing the data loading method.
        """
        descrps = {'Entrance': 'This is the description'}
        _c = ['Paper', 'Donut']
        _b = {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
        _a = {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
        room_1 = {'Neighbors': _a, 'Door': _b, 'Items': _c}
        rooms = {'Entrance': room_1}
        data = {'Rooms': rooms, 'Rooms Descriptions': descrps}
        self.assertIsNone(engine.loading_map(data))

    def test_loading_item(self):
        """
        Testing the loading item method.
        """
        _b = ['Property']
        _a = ['This is the description']
        items = {'Description': _a, 'Properties': _b}
        item = {'Item': items}
        data = {'Items': item}
        self.assertIsNone(engine.loading_items(data))

    def test_loading_player(self):
        """
        Testing the loading player method
        """
        _b = ['Property']
        _a = ['Help Guide']
        player = {'Inventory': _a, 'Position': _b}
        data = {'Player': player}
        self.assertIsNone(engine.loading_player(data))

    @patch('dork.character_manager.player_inventory')
    def test_display_inventory(self, mock_inventory):
        """
        Testing the method that prints the player inventory
        """
        mock_inventory.return_value = ['Flower', 'Donut']
        self.assertIsNone(engine.display_inventory())

    @patch('dork.room_manager.to_string_current_items')
    @patch('dork.room_manager.room_description')
    @patch('dork.game_engine.__current_position')
    @patch('dork.room_manager.not_empty_room')
    def test_room_to_screen(self, room, current, description, to_string):
        """
        Testing the method that prints the room name,
        room description and room items.
        """
        room.return_value = 'Entrance'
        current.return_value = 'Lake'
        description.return_value = 'This is the description'
        to_string.return_value = 'To the screen'
        self.assertIsNone(engine.room_to_screen())

    @patch('dork.game_engine.room_to_screen')
    @patch('dork.character_manager.update_player_position')
    @patch('dork.room_manager.move')
    @patch('dork.game_engine.__current_position')
    def test_move(self, position, moved, new_pos, to_screen):
        """
        Testing the method that moves the player around
        the map.
        """
        position.return_value = None
        moved.return_value = None
        new_pos.return_value = 'Lake'
        self.assertIsNone(engine.move('North'))
        moved.return_value = ' '
        to_screen.return_value = 'To screen'
        self.assertIsNone(engine.move('East'))

    @patch('dork.item_manager.item_description')
    @patch('dork.character_manager.player_has_item')
    @patch('dork.room_manager.is_item_in_room')
    @patch('dork.item_manager.is_item')
    def test_examine(self, is_item, in_room, in_player, descrip):
        """
        Testing the method that examine the items.
        """
        is_item.return_value = True
        in_room.return_value = True
        in_player.return_value = True
        descrip.return_value = 'Description'
        self.assertIsNone(engine.examine('Donut'))
        is_item.return_value = False
        self.assertIsNone(engine.examine('Flower'))

    @patch('builtins.print')
    @patch('dork.room_manager.delete_item')
    def test_pick_up(self, was_deleted, printed):
        """
        Testing the method that picks up items from current room
        """
        was_deleted.return_value = ('Deleted', True)
        printed.return_value = 'Printed'
        self.assertIsNone(engine.pick_up('Flower'))
        was_deleted.return_value = ('Not Deleted', False)
        self.assertIsNone(engine.pick_up('Donut'))

    @patch('dork.room_manager.append_item')
    @patch('builtins.print')
    @patch('dork.character_manager.remove_item_from_inventory')
    def test_drop(self, was_dropped, printed, append):
        """
        Testing the method that drops items into current room
        """
        was_dropped.return_value = ('Dropped', True)
        printed.return_value = 'Printed'
        append.return_value = 'Append'
        self.assertIsNone(engine.drop('Flower'))
        was_dropped.return_value = ('Not Dropped', False)
        self.assertIsNone(engine.drop('Flower'))

    @patch('dork.room_manager.open_door')
    @patch('dork.character_manager.player_has_item')
    def test_use_key(self, item_in_player, open_door):
        """
        Testing the method that use keys in doors
        """
        item_in_player.return_value = True
        open_door.return_value = 'Door'
        self.assertIsNone(engine.use_key('Door', 'Badge'))
        item_in_player.return_value = False
        self.assertIsNone(engine.use_key('Door', 'Tool'))

    @patch('dork.yamlloader.writing_yml')
    @patch('dork.character_manager.player_yaml_representation')
    @patch('dork.item_manager.items_yaml_representation')
    @patch('dork.room_manager.map_yaml_representation')
    def test_save(self, maze, items, player, write):
        """
        Testing the saving method
        """
        maze.return_value = {'Map': 'Map Value'}
        items.return_value = {'Items': 'Item Value'}
        player.return_value = {'Player': 'Player Value'}
        write.return_value = 'File'
        self.assertIsNone(engine.saving())
