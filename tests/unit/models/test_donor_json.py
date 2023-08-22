'''
Created on Aug 22, 2023

@author: Miho
Unit test of JSON output
Separated this from create donor test to work around Flask app creation error
'''

from tests.base_test import BaseTest

class DonorTest(BaseTest):
    
    #Test json output
    def test_create_json(self):
        donorjson = {'name': self.name, 'type': self.type}
        self.assertDictEqual(self.donor.json(), donorjson)