#Assets
from flask import Flask
from connect import db

#Class Web
class web:
    #Config Website
    def __init__(self, config):
        #Create Website
        self.website = Flask(__name__)

        #Secret Website
        self.website.secret_key = config['Secret']

        #Database Website
        self.db = db(config)
        

    #Run Website
    def run(self, debug=False):

        self.website.run(debug=debug)