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

        #Get Blueprints
        from .blueprints.en import en
        from .blueprints.pt import pt

        #Blueprints
        self.website.register_blueprint(en)
        self.website.register_blueprint(pt)
        

    #Run Website
    def run(self, debug=False):

        self.website.run(debug=debug)