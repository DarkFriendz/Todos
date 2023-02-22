#Assets
from flask import Blueprint, redirect, render_template, flash, get_flashed_messages

#Datebase
from connet import db

#Get Datebase
db = db()

#Blueprint
en = Blueprint('english', __name__, url_prefix='/en/')

#index
@en.route('/')
@en.route('/<page>')
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
            return render_template('/en/home.html', flashs=flashs, tasks=tasks)
        elif page == 'addTask':
            flashs = list(enumerate(get_flashed_messages(with_categories=True)))
            return render_template('/en/addTask.html', flashs=flashs)

        flash('Error page not found, please try again later!', 'error')
        return redirect('/en/home')
    else:
        flash('Error page not found, please try again later!', 'error')
        return redirect('/en/home')

#Edit
@en.route('/editTask/')
@en.route('/editTask/<task>')
def edit(task=None):
    if task != None:
        db.getTask(task)
        if db.info['error'] != True:
            flashs = list(enumerate(get_flashed_messages(with_categories=True)))
            return render_template('/en/edit.html', flashs=flashs, task=db.info['content'])
        else:
            flash(f'{db.info["reason"]}', 'error')
            return redirect('/en/home')
    else:
        flash('Error page not found, please try again later!', 'error')
        return redirect('/en/home')

#Blueprint Execute
from .enExecute import enExcute

en.register_blueprint(enExcute)