'''
A testing module for the items module
'''
import unittest
from dork.gameitem import Items


class TestValidMaze(unittest.TestCase):
    '''
    A testing class for the Items class
    '''
    def test_constructor(self):
        '''
        testing the __init__ method
        '''
        testing_item = Items('name')
        self.assertEqual(testing_item.name, 'name')

    def test_use(self):
        '''
        testing the use method
        '''
        testing_item = Items('name')
        output = testing_item.use()
        expect = 'You used the ' + testing_item.name + ' item'
        self.assertEqual(output, expect)

    def test_store(self):
        '''
        testing the store method
        '''
        testing_item = Items('name')
        output = testing_item.store()
        expect = 'You stored the ' + testing_item.name + ' into your inventory'
        self.assertEqual(output, expect)
