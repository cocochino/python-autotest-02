'''
Created on Aug 12, 2023

@author: Miho
This file shouldn't contain any test cases. This is a super class.
This also bundle imports into once place, easing maintenance
'''

from unittest import TestCase
from donor_app.src.flask_app import app

class BaseTest(TestCase):
    
    def setUp(self):
        app.testing = True #Setting Flask to a test mode
        self.app = app.test_client