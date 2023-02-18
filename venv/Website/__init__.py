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

        #Get Blueprints
        from .blueprints.en.en import en
        from .blueprints.pt.pt import pt

        #Set Blueprints
        self.website.register_blueprint(en)
        self.website.register_blueprint(pt)

    #Run Web
    def run(self, debug=False):
        #Config Language[
        @self.website.route('/')
        @self.website.route('/<lang>')
        def index(lang=None):
            return f"{lang}"

        #Run Website
        self.website.run(debug=debug)
