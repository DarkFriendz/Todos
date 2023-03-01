#Assets
from flask import Flask

#Class Website
class web():
    #Config Website
    def __init__(self, config:list):
        #Create Website
        self.website = Flask(__name__)

    #Run Website
    def run(self, debug:bool=False):
        
        #Run
        self.website.run()