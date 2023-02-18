#Assets
from flask import flask, redirect, flash

#Class Web
class web:
    #Config Web
    def __init__(self, config):
        #Created Website
        self.website = flask(__name__)

        #Secret Website
        #self.website

    #Run Web
    def run(self, debug=False):

        #Run Website
        self.website.run(debug=debug)
