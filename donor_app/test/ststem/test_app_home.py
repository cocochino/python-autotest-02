'''
Created on Aug 11, 2023

@author: Miho
Testing web app with Flask client
'''

from donor_app.test.ststem.base_test import BaseTest
#Following are replaced by base_test
#from unittest import TestCase
#from donor_app.src.flask_app import app #Note that test dosen't need to run the app server on the background
import json

class TestAppHome(BaseTest):
#Following are replaced by BaseTest
#class TestAppHome(TestCase):



    def test_app_home(self):
        #With Flask test can run against Flask client. No need to run full server
        with self.app() as c:
        #Following are replaced by BaseTest. Now this test case can ignore flask client aspect of the test app
        #with app.test_client() as c:
            resp = c.get('/')
            #print(resp.get_data())
            #print(resp.status_code)
            self.assertEqual(resp.status_code, 200)
            
            #Flast response is String. So it needs to be converted to JSON format.
            self.assertEqual(
                json.loads(resp.get_data()), #json.loads() convert string to json 
                {'message': 'Welcome to the Donor site!'}
            )
