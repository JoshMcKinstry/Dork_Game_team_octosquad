"""
A test for room_manager
"""
import dork.room_manager as room_m


def test_assembling_rooms():
    """ Testing assembling_rooms method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(
        list_names, list_neighbors, list_doors, list_items)
    assert room_m.DICT_ROOMS['Entrance'].name == 'Entrance'
    assert room_m.DICT_ROOMS['Entrance'].neighbors == {
        'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    assert room_m.DICT_ROOMS['Entrance'].door == {
        'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    assert room_m.DICT_ROOMS['Entrance'].items == 'Paper', "Donut"


def test_assembling_descriptions():
    """
    Testing assembling_descriptions method
    """
    list_names = ['Entrance']
    list_descriptions = ['This is the entrance']
    room_m.assembling_descriptions(list_names, list_descriptions)
    assert room_m.DICT_DESCRIPTIONS['Entrance'] == (
        'This is the entrance')


def test_current_room():
    """
    Testing current_room method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(
        list_names, list_neighbors, list_doors, list_items)
    assert room_m.current_room('Entrance').name == 'Entrance'
    assert room_m.current_room('Entrance').neighbors == {
        'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}
    assert room_m.current_room('Entrance').door == {
        'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}
    assert room_m.current_room('Entrance').items == 'Paper', "Donut"


def test_room_description():
    """
    Testing room_description method
    """
    list_names = ['Entrance']
    list_descriptions = ['This is the entrance']
    room_m.assembling_descriptions(list_names, list_descriptions)
    assert room_m.room_description('Entrance') == 'This is the entrance'


def test_items_in_room():
    """
    Testing items_in_room method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(
        list_names, list_neighbors, list_doors, list_items)
    assert room_m.items_in_room('Entrance') == 'Paper', 'Donut'


def test_is_item_in_room():
    """
    Testing is_item_in_room method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper']
    room_m.assembling_rooms(
        list_names, list_neighbors, list_doors, list_items)
    assert room_m.is_item_in_room('Entrance', 'Paper') is True


def test_append_item():
    """
    testing append_item method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = [['Paper', 'Donut']]
    room_m.assembling_rooms(
        list_names, list_neighbors, list_doors, list_items)
    room_m.append_item('Entrance', 'Cellphone')
    assert room_m.DICT_ROOMS['Entrance'].items == [
        'Paper', 'Donut', 'Cellphone']


def test_delete_item():
    """
    testing delete_item method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(
        list_names, list_neighbors, list_doors, list_items)
    room_m.delete_item('Entrance', 'Donut')
    assert room_m.DICT_ROOMS['Entrance'].items == 'Paper'


def test_not_empty_room():
    """
    testing not_empty_room method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(
        list_names, list_neighbors, list_doors, list_items)
    assert room_m.not_empty_room('Entrance') is True


def test_to_string_current_items():
    """
    testing to_string_current_items method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut']
    room_m.assembling_rooms(list_names, list_neighbors, list_doors, list_items)
    assert room_m.to_string_current_items('Entrance') == (
        'You notice the following items--- P, a, p, e, r.')


def test_move():
    """
    testing move method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lounge'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = [['Paper', 'Donut']]
    room_m.assembling_rooms(
        list_names, list_neighbors, list_doors, list_items)
    assert room_m.move('West', 'Entrance') == 'Lounge'
    assert room_m.move('East', 'Entrance') is None
    assert room_m.move('North', 'Entrance') is None


def test_open_door():
    """
    testing open_door method
    """
    list_names = ['Entrance']
    list_neighbors = [
        {'North': 'Trail', 'East': None, 'South': None, 'West': 'Lake'}]
    list_doors = [
        {'Cardinal': 'North', 'Status': 'Dean Badge', 'State': 'Closed'}]
    list_items = ['Paper', 'Donut', 'Dean Badge']
    room_m.assembling_rooms(
        list_names, list_neighbors, list_doors, list_items)
    out_put_2 = room_m.open_door('Entrance', 'North', 'Junior Badge')
    expected_2 = 'Invalid key for door at North!'
    assert out_put_2 == expected_2
    out_put_3 = room_m.open_door('Entrance', 'South', 'Dean Badge')
    expected_3 = 'There is no closed door at the South!'
    assert out_put_3 == expected_3
    out_put_1 = room_m.open_door('Entrance', 'North', 'Dean Badge')
    expected_1 = 'Door in Entrance at North is now open.'
    assert out_put_1 == expected_1
