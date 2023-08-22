'''
Created on Aug 18, 2023

@author: Miho
Demo of web app using Flask client
- Check HTTP response code
- Check response content by jsonifying string 
'''

from tests.base_test import BaseTest
import json

class TestAppHome(BaseTest):

    def test_app_home(self):
        #With Flask test can run against Flask client. No need to run full server
        with self.app() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)
            
            #Flask response is String. So it needs to be converted to JSON format.
            self.assertEqual(
                json.loads(resp.get_data()), #json.loads() convert string to json 
                {'message': 'Welcome to the Donor site!'}
            )
