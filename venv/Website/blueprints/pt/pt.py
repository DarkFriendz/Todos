#Assets
from flask import Blueprint, redirect, render_template, flash, get_flashed_messages

#Datebase
from connet import db

#Get Datebase
db = db()

#Blueprint
pt = Blueprint('portugues', __name__, url_prefix='/pt/')

#index
@pt.route('/')
@pt.route('/<page>')
def index(page=None):
    if page != None:
        if page == 'home':
            db.tasks()
            flashs = list(enumerate(get_flashed_messages(with_categories=True)))
            tasks = db.info['content']
            for id, task in enumerate(tasks):
                if task[4] != None:
                    tasklist = list(task)
                    dateFormat = task[4].split('-')
                    dateFormat = f'{dateFormat[2]}/{dateFormat[1]}/{dateFormat[0]}'
                    tasklist[4] = dateFormat
                    tasks[id] = tuple(tasklist)
            return render_template('/pt/home.html', flashs=flashs, tasks=tasks)
        elif page == 'addTask':
            flashs = list(enumerate(get_flashed_messages(with_categories=True)))
            return render_template('/pt/addTask.html', flashs=flashs)

        flash('Erro áo carregar a página, tente novamente mais tarde!', 'error')
        return redirect('/pt/home')
    else:
        flash('Erro áo carregar a página, tente novamente mais tarde!', 'error')
        return redirect('/pt/home')
    
#Edit
@pt.route('/editTask/')
@pt.route('/editTask/<task>')
def edit(task=None):
    if task != None:
        db.getTask(task)
        if db.info['error'] != True:
            flashs = list(enumerate(get_flashed_messages(with_categories=True)))
            return render_template('/pt/edit.html', flashs=flashs, task=db.info['content'])
        else:
            flash(f'{db.info["reason"]}', 'error')
            return redirect('/pt/home')
    else:
        flash('Erro áo carregar a página, tente novamente mais tarde!', 'error')
        return redirect('/pt/home')

#Blueprint Execute
from .ptExecute import ptExecute

pt.register_blueprint(ptExecute)