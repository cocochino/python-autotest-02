'''
Created on Aug 12, 2023

@author: Miho
This file shouldn't contain any test cases. This is a super class.
This also bundle imports into once place, easing maintenance
'''
import configparser
import os

from unittest import TestCase
from app import app
from db import db #This is SQLAlchemy

from models.donor import DonorModel

class BaseTest(TestCase):
    
    def setUp(self):
        #Setting Flask to a test mode
        app.testing = True 
        
        #Create a new  database connection.
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' 
        
        #app_context() =  Use as a with block to push the context, which will make current_app point at this application
        with app.app_context():
            db.init_app(app)
            #Delete all tables... this doesn't work in tearDown somehow. App context problem.
            db.drop_all()
            db.create_all()
            
        self.app = app.test_client # This line was used in Section 4 too
        self.app_context = app.app_context
        
        #Define path of donor configuraion file relative to the base test
        ROOT_DIR  = os.path.dirname(os.path.abspath(__file__))
        configFilePath = ROOT_DIR + '/donors.txt'
        cp = configparser.RawConfigParser() 
        cp.read(configFilePath)
        
        #Create a simple test donor
        self.name = cp['DONOR1']['name']
        self.type = cp['DONOR1']['blood type']
        self.badname = cp['DONOR invalid']['name']
        self.badtype = cp['DONOR invalid']['blood type']   
        self.donor = DonorModel(self.name, self.type)
        
        #Tell users which test is running.
        print('\n Running test: ', self.id())

        
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            