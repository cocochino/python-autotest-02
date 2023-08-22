'''
Created on Aug 18, 2023

Modified for TestAppHome test cases
'''

import os

#from flask import Flask
from flask import Flask, jsonify
from flask_restful import Api

from resources.item import Item, ItemList

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Item, '/item/<string:name>')

'''Begin: Modified by Miho'''
#setting access point to the root of the site. home() will define the behavior.
@app.route('/') 

#Set default behavior of root. It will just return a message.
#Flask can return strings from its endpoint but not dictionary
def home():
    #jsonify converts dictionary to string
    return jsonify({'message': "Welcome to the Donor site!"})

'''End: Modified by Miho'''

if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
