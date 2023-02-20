#Assets
from flask import Flask, redirect, session, flash

#Class Web
class web:
    #Config Web
    def __init__(self, config):
        #Created Website
        self.website = Flask(__name__)

        #Secret Website
        self.website.secret_key = config['Secret']

        #Languages Website
        self.languages = ['en', 'pt']

        #Get Blueprints
        from .blueprints.en.en import en
        from .blueprints.pt.pt import pt

        #Set Blueprints
        self.website.register_blueprint(en)
        self.website.register_blueprint(pt)

    #Run Web
    def run(self, debug=False):
        #Config Language
        @self.website.route('/')
        @self.website.route('/<lang>')
        def index(lang=None):
            if lang != None:
                    for language in self.languages:
                        if language == lang:
                            try:
                                if session['language']:
                                    session['language'] = language
                            except:
                                return redirect(f'/{language}/')
                    return redirect('/en/')
            else:
                return redirect('/en/')

        #Run Website
        self.website.run(debug=debug)