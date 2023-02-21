#Assets
from flask import Blueprint, redirect, render_template, flash, get_flashed_messages, request

#Datebase
from connet import db

#Get Datebase
db = db()

#Blueprint
enExcute = Blueprint('englishExecute', __name__, url_prefix='/execute')

@enExcute.route("/")
@enExcute.route("/<action>", methods=['GET', 'POST'])
def index(action=None):
    if action != None:
        if request.method == 'POST':
            if action == "addTask":
                db.addTask(request)
                if db.info['error'] != True:
                    flash('Task successfully saved!', 'sucess')
                    return redirect('/en/home')
                else:
                    flash(f'{db.info["reason"]}', 'error')
                    return redirect('/en/home')
            elif action == "language":
                return redirect('/pt/')

        flash('Error loading page, please try again later!', 'error')
        return redirect('/en/home')
    else:
        flash('Error loading page, please try again later!', 'error')
        return redirect('/en/home')

@enExcute.route("/editTask/")
@enExcute.route("/editTask/<task>", methods=["GET", "POST"])
def edit(task=None):
    if task != None:
        db.editTask(task, request)
        flash('Task successfully Edited!', 'sucess')
        return redirect('/en/home')
    else:
        flash('Error loading page, please try again later!', 'error')
        return redirect('/en/home')

@enExcute.route("/done/")
@enExcute.route("/done/<task>")
def done(task=None):
    if task != None:
        db.doneTask(task)
        flash('Task successfully Completed!', 'sucess')
        return redirect('/en/home')
    else:
        flash('Error loading page, please try again later!', 'error')
        return redirect('/en/home')

@enExcute.route("/doneRemove/")
@enExcute.route("/doneRemove/<task>")
def doneRemove(task=None):
    if task != None:
        db.doneRemoveTask(task)
        flash('Task successfully descompleted!', 'warning')
        return redirect('/en/home')
    else:
        flash('Error loading page, please try again later!', 'error')
        return redirect('/en/home')

@enExcute.route("/remove/")
@enExcute.route("/remove/<task>")
def remove(task=None):
    if task != None:
        db.deletTask(task)
        flash('Task successfully deleted!', 'sucess')
        return redirect('/en/home')
    else:
        flash('Error loading page, please try again later!', 'error')
        return redirect('/en/home')