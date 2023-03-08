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
        @self.website.route('/<lang>/<page>/<id>')
        def home(lang=None, page=None, id=None):
            if lang != None:
                if page != None:
                    if page == 'home':
                        self.db.getAll(session['language'])
                        session['language'] = lang
                        return render_template('home.html', rows=self.db.result['info'])
                    elif page == 'addTask':
                        session['language'] = lang
                        return render_template('task.html')
                    elif page == 'edit':
                        self.db.getRow(id)
                        session['language'] = lang
                        return render_template('edit.html', row=self.db.result['info'])
                else:
                    session['language'] = lang
                    return redirect(f'/{lang}/home')

            session['language'] = 'en'
            return redirect(f'/en/')
        
        #Execute
        @self.website.route('/<lang>/execute/<func>/<id>', methods=['POST', 'GET'])
        @self.website.route('/<lang>/execute/<func>', methods=['POST'])
        def execute(lang=None, func=None, id=None):
            #Add Task
            if func == 'addTask':
                if request.form['title'] != '' and len(request.form['title']) >= 3:
                    self.db.addTask(request.form)
                    if lang == 'en':
                        flash('Add task successfully!', 'sucess')
                    elif lang == 'pt':
                        flash('Adicionar tarefa com sucesso!', 'sucess')
                    elif lang == 'es':
                        flash('¡Agregue la tarea con éxito!', 'sucess')
                    else:
                        flash('Add task successfully!', 'sucess')

                    return redirect(f'/{lang}/addTask')
                else:
                    if lang == 'en':
                        flash('Title is too short!')
                    elif lang == 'pt':
                        flash('Titulo e muito curto!')
                    elif lang == 'es':
                        flash('¡El título es demasiado corto!')
                    else:
                        flash('Title is too short!')

                    session['language'] = lang
                    return redirect(f'/{lang}/addTask')

            #Delete Task
            elif func == 'delet':
                self.db.deletTask(id)
                if lang == 'en':
                    flash('Deleted task successfully!', 'sucess')
                elif lang == 'pt':
                    flash('Tarefa excluída com sucesso!', 'sucess')
                elif lang == 'es':
                    flash('¡Tarea eliminada con éxito!', 'sucess')
                else:
                    flash('Deleted task successfully!', 'sucess')
                session['language'] = lang
                return redirect(f'/{lang}/home')
            
            #Edit Task
            elif func == 'edit':
                self.db.editTask(id, request.form)
                if lang == 'en':
                    flash('Edited task successfully!', 'sucess')
                elif lang == 'pt':
                    flash('Tarefa editada com sucesso!', 'sucess')
                elif lang == 'es':
                    flash('¡Tarea editada con éxito!', 'sucess')
                else:
                    flash('Edited task successfully!', 'sucess')
                session['language'] = lang
                return redirect(f'/{lang}/edit/{id}')
            
            #Done Task
            elif func == 'done':
                self.db.Done(id)
                if lang == 'en':
                    flash('Finished task successfully!', 'sucess')
                elif lang == 'pt':
                    flash('Tarefa finalizada com sucesso!', 'sucess')
                elif lang == 'es':
                    flash('¡Tarea terminada con éxito!', 'sucess')
                else:
                    flash('Finished task successfully!', 'sucess')
                session['language'] = lang
                return redirect(f'/{lang}/home')
            
            #Not Done Task
            elif func == 'notdone':
                self.db.NotDone(id)
                if lang == 'en':
                    flash('Undone task successfully!', 'warning')
                elif lang == 'pt':
                    flash('Tarefa desfeita com sucesso!', 'warning')
                elif lang == 'es':
                    flash('¡Tarea deshecha con éxito!', 'warning')
                else:
                    flash('Undone task successfully!', 'warning')
                session['language'] = lang
                return redirect(f'/{lang}/home')
            
            #Select Language
            elif func == 'language':
                session['language'] = request.form['language']
                return redirect(f'/{request.form["language"]}/home')

            elif func == None:
                session['language'] = lang
                return redirect(f'/{lang}/home')

        #Run
        self.website.run(debug=debug)