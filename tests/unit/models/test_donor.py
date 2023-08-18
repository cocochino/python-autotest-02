'''
Created on Aug 18, 2023

@author: Miho
Demo of unit test with DB interaction

'''

#from tests.system.base_test import BaseTest
from tests.base_test import BaseTest
from models.donor import DonorModel

class DonorTest(BaseTest):
    
    def setUp(self):
        self.name = 'Patient One'
        self.type = 'O+'
        self.donor = DonorModel(self.name, self.type)
    
    #Test __init__
    def test_create_item(self):
        self.assertEqual(self.donor.name, self.name)
        self.assertEqual(self.donor.type, self.type)
        

    #Test json output
    def test_create_json(self):
        donorjson = {'name': self.name, 'type': self.type}
        self.assertDictEqual(self.donor.json(), donorjson)