#Assets
from flask import Flask, redirect, render_template, session, request, flash
from connect import db

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

        #Datebase
        self.db = db(config['Database'])

    #Run Website
    def run(self, debug:bool=False):

        #Index
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
        
        #Home
        @self.website.route('/<lang>/')
        @self.website.route('/<lang>/<page>')
        def home(lang=None, page=None):
            if lang != None:
                if page != None:
                    if page == 'home':
                        self.db.getAll(session['language'])
                        session['language'] = lang
                        return render_template('home.html', rows=self.db.result['info'])
                    if page == 'addTask':
                        session['language'] = lang
                        return render_template('task.html')
                else:
                    session['language'] = lang
                    return redirect(f'/{lang}/home')

            session['language'] = 'en'
            return redirect(f'/en/')
        
        #Execute
        @self.website.route('/<lang>/execute/<func>', methods=['POST'])
        def execute(lang, func):
            if func == 'addTask':
                if request.form['title'] != '' and len(request.form['title']) >= 3:
                    self.db.addTask(request.form)
                    #return redirect('/en/addTask')
                    return request.form
                else:
                    if lang == 'en':
                        flash('Title is too short!')
                    elif lang == 'pt':
                        flash('Titulo e muito curto!')
                    elif lang == 'es':
                        flash('¡El título es demasiado corto!')
                    else:
                        flash('Title is too short!')
                    
                    return redirect('/en/addTask')

        #Run
        self.website.run(debug=debug)