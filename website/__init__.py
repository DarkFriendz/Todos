#Assets
from flask import Flask, redirect, render_template, session

#Class Website
class web():
    #Config Website
    def __init__(self, config:list):
        #Create Website
        self.website = Flask(__name__)

        #Secret Key Website
        self.website.secret_key = config['Secret']

        #Language Website
        self.languages = ['en', 'pt', 'es']

    #Run Website
    def run(self, debug:bool=False):

        @self.website.route('/')
        @self.website.route('/<lang>')
        def index(lang=None):
            if lang != None:
                for language in self.languages:
                    if language == lang:
                        session['language'] = lang
                        return redirect(f'/{lang}/')

            session['language'] = 'en'
            return redirect('/en/')
        
        @self.website.route('/<lang>/')
        @self.website.route('/<lang>/<page>')
        def home(lang=None, page=None):
            if lang != None:
                if page != None:
                    if page == 'home':
                        session['language'] = lang
                        return render_template('home.html')
                else:
                    session['language'] = lang
                    return redirect(f'/{lang}/home')

            session['language'] = 'en'
            return redirect(f'/en/')
        
        #Run
        self.website.run(debug=debug)