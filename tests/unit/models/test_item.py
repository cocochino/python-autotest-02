'''
Created on Aug 18, 2023

@author: Miho
Not relaying on BaseTest
'''
from unittest import TestCase

from models.item import ItemModel

class ItemTest(TestCase):
    
    def setUp(self):
        self.name = 'tulip'
        self.price = 1.55
        self.item = ItemModel(self.name, self.price)
    
    #Test __init__
    def test_create_item(self):
        self.assertEqual(self.item.name, self.name)
        self.assertEqual(self.item.price, self.price)
        

    #Test json output
    def test_create_json(self):
        itemjson = {'name': self.name, 'price': self.price}
        self.assertDictEqual(self.item.json(), itemjson)