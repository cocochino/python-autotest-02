'''
Created on Aug 18, 2023

Item test with database connection. Not unit test casesQ
CRUD = Create, read, update, delete
'''

from models.item import ItemModel
from tests.base_test import BaseTest

name = 'tulip'
price = 1.55
class ItemTest(BaseTest):
    

    def test_crud(self):
        with self.app_context(): #see BaseTest
            item = ItemModel(name, price)
            
            #Confirm that the test item doesn't exist at the beginning
            self.assertIsNone(ItemModel.find_by_name(name))
            
            item.save_to_db() #Saved to SQLite file
            
            #Confirm that the test item has been created and can be read
            self.assertIsNotNone(ItemModel.find_by_name(name))
            
            item.delete_from_db()
            
            #Confirm that the test item has been removed
            self.assertIsNone(ItemModel.find_by_name(name))
            
            