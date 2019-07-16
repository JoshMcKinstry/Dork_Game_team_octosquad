"""
A test for items
"""
from dork.items import Item


def test_init_method():
    """
    Testing the constructor
    """
    name = 'Donut'
    description = {'This is an old fasion donut'}
    properties = {'eatable'}
    item = Item(name, description, properties)
    assert item.name == name
    assert item.description == description
    assert item.properties == properties


def test_has_property():
    """
    Testing the has_property method
    """
    name = 'Donut'
    description = {'This is an old fasion donut'}
    properties = ['eatable', 'pickable']
    item = Item(name, description, properties)
    assert item.has_property('eatable') is True
