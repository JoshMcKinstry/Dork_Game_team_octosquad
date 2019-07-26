"""
A test for the methods in the item_manager file.
"""
import dork.item_manager as item_m


def test_assembling_item():
    """
    Test the assembling_items method.
    """
    list_item = ['donut']
    list_description = ['This is a donut']
    list_property = ['openable']
    item_m.assembling_items(list_item, list_description, list_property)
    assert item_m.DICT_ITEMS['donut'].name == 'donut'
    assert item_m.DICT_ITEMS['donut'].description == 'This is a donut'
    assert item_m.DICT_ITEMS['donut'].properties == 'openable'


def test_is_item():
    """
    Tests the is_item method.
    """
    list_item = ['donut']
    list_description = ['This is a donut']
    list_property = ['openable']
    item_m.assembling_items(list_item, list_description, list_property)
    assert item_m.is_item('donut')
    assert not item_m.is_item('sword')


def test_item_description():
    """
    Test the item_description method.
    """
    list_item = ['donut']
    list_description = ['This is a donut']
    list_property = ['openable']
    item_m.assembling_items(list_item, list_description, list_property)
    assert item_m.item_description('donut') == 'This is a donut'
    assert item_m.item_description('donut') != 'ewfwefwefe'


def test_yaml_representation():
    """
    Test the yaml_representation method.
    """
    list_item = ['donut']
    list_description = ['This is a donut']
    list_property = ['openable']
    item_m.assembling_items(list_item, list_description, list_property)
    assert isinstance(item_m.items_yaml_representation(), dict)
