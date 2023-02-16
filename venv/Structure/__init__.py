#Assets
from flask import Flask, redirect
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

        #Languages 
        self.languages = config['Languages']

        #Get Blueprints
        from .blueprints.en import en
        from .blueprints.pt import pt

        #Blueprints
        self.website.register_blueprint(en)
        self.website.register_blueprint(pt)
        

    #Run Website
    def run(self, debug=False):

        #Redirect Language
        @self.website.route('/')
        @self.website.route('/<page>')
        def index(page=None):
            if page != None:
                for language in self.languages:
                    if language == page:
                        return redirect(f'/{page}/')
                return redirect(f'/en/')
            else:
                return redirect(f'/en/')

        #Started Website
        self.website.run(debug=debug)