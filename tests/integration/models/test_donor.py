'''
Created on Aug 18, 2023

@author: Miho
CRUD test integrating with database record 
Donor information is coming from BaseTest
'''
from tests.base_test import BaseTest
from models.donor import DonorModel

class DonorTest(BaseTest):
        
    def test_crud(self):
        with self.app_context(): #see BaseTest
            item = self.donor
            
            #Confirm that the test item doesn't exist at the beginning
            self.assertIsNone(DonorModel.find_by_name(self.name))
            
            item.save_to_db() #Saved to SQLite file
            
            #Confirm that the test item has been created and can be read
            self.assertIsNotNone(DonorModel.find_by_name(self.name))
            
            item.delete_from_db()
            
            #Confirm that the test item has been removed
            self.assertIsNone(DonorModel.find_by_name(self.name))