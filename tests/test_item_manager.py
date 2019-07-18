"""
A test for item_manager
"""
import dork.item_manager as item_m


def test_assembling_item():
    """
    Test for assembling items
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
    Test for if the item is an item
    """
    list_item = ['donut']
    list_description = ['This is a donut']
    list_property = ['openable']
    item_m.assembling_items(list_item, list_description, list_property)
    assert item_m.is_item('donut')
    assert not item_m.is_item('sword')


def test_item_description():
    """
    Test for item description
    """
    list_item = ['donut']
    list_description = ['This is a donut']
    list_property = ['openable']
    item_m.assembling_items(list_item, list_description, list_property)
    assert item_m.item_description('donut') == 'This is a donut'
    assert item_m.item_description('donut') != 'ewfwefwefe'

def test_yaml_representation():
    """
    Test for the yaml representation method
    """
    list_item = ['donut']
    list_description = ['This is a donut']
    list_property = ['openable']
    item_m.assembling_items(list_item, list_description, list_property)
    assert isinstance(item_m.items_yaml_representation(), dict)