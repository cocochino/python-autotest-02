'''
Created on Aug 11, 2023

@author: Miho
Creating flask app for test experiments
'''
from flask import Flask, jsonify

#Create a Flask app
app = Flask(__name__)
#print("app is ", app)

#setting access point to the root of the site. home() will define the behavior.
@app.route('/') 

#Set default behavior of root. It will just return a message.
#Flask can return strings from its endpoint but not dictionary
def home():
    #jsonify converts dictionary to string
    return jsonify({'message': "Welcome to the Donor site!"})


if __name__ == '__main__':
    app.run()