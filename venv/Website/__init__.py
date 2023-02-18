#Assets
from flask import Flask, redirect, flash

#Class Web
class web:
    #Config Web
    def __init__(self, config):
        #Created Website
        self.website = Flask(__name__)

        #Secret Website
        self.website.secret_key = config['Secret']

    #Run Web
    def run(self, debug=False):

        #Run Website
        self.website.run(debug=debug)
