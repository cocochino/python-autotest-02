'''
Created on Aug 18, 2023

@author: Miho
Demo of unit test with DB interaction
Reading test parameter using ConfigParser

'''
import configparser

from tests.base_test import BaseTest
from models.donor import DonorModel

class DonorTest(BaseTest):
    
    def setUp(self):
        cp = configparser.RawConfigParser() 
        configFilePath = r'../../donors.txt'
        cp.read(configFilePath)
        
        self.name = cp['DONOR1']['name']
        self.type = cp['DONOR1']['blood type']
        self.badname = cp['DONOR invalid']['name']
        self.badtype = cp['DONOR invalid']['blood type']        
        self.donor = DonorModel(self.name, self.type)
        
    #Test __init__
    def test_create_item(self):
        self.assertEqual(self.donor.name, self.name)
        self.assertEqual(self.donor.type, self.type)
        
    #Negative test __init__
    def test_create_item_negative(self):
        self.assertNotEqual(self.donor.name, self.badname)
        self.assertNotEqual(self.donor.type, self.badtype)

    #Test json output
    def test_create_json(self):
        donorjson = {'name': self.name, 'type': self.type}
        self.assertDictEqual(self.donor.json(), donorjson)