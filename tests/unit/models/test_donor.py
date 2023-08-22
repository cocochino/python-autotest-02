'''
Created on Aug 18, 2023

@author: Miho
Demo of unit test with items and config read from BaseTest.

'''

from tests.base_test import BaseTest

class DonorTest(BaseTest):
    
        
    #Test __init__
    def test_create_item(self):
        self.assertEqual(self.donor.name, self.name)
        self.assertEqual(self.donor.type, self.type)
        
        self.assertNotEqual(self.donor.name, self.badname)
        self.assertNotEqual(self.donor.type, self.badtype)
                
