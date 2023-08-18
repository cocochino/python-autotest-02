'''
Created on Aug 12, 2023

@author: Miho
This file shouldn't contain any test cases. This is a super class.
This also bundle imports into once place, easing maintenance
'''

from unittest import TestCase
from app import app
from db import db #This is SQLAlchemy

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
        
    
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            