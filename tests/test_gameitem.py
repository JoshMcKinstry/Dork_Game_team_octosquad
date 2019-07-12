'''
A testing module for the items module
'''
import unittest
from dork.gameitem import Items


class TestValidItem(unittest.TestCase):
    '''
    A testing class for the Items class
    '''
    def test_constructor(self):
        '''
        testing the __init__ method
        '''
        properties = {'isRemoveable': False}
        testing_item = Items('name', 'description', **properties)
        self.assertTrue(testing_item.name, 'name')
        self.assertTrue(testing_item.description, 'description')
        self.assertIn('isRemoveable', properties)
        #self.assertEquals(attributes.get('isRemoveable'), False)
