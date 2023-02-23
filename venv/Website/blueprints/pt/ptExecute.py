#Assets
from flask import Blueprint, redirect, render_template, flash, get_flashed_messages, request

#Datebase
from connet import db

#Get Datebase
db = db()

#Blueprint
ptExecute = Blueprint('portugueseExecute', __name__, url_prefix='/execute')

@ptExecute.route("/")
@ptExecute.route("/<action>", methods=['GET', 'POST'])
def index(action=None):
    if action != None:
        if request.method == 'POST':
            if action == "addTask":
                db.addTask(request)
                if db.info['error'] != True:
                    flash('Tarefa salva com sucesso!', 'sucess')
                    return redirect('/pt/home')
                else:
                    flash(f'{db.info["reason"]}', 'error')
                    return redirect('/pt/home')
            elif action == "language":
                return redirect('/en/')

        flash('Erro áo carregar a página, tente novamente mais tarde!', 'error')
        return redirect('/pt/home')
    else:
        flash('Erro áo carregar a página, tente novamente mais tarde!', 'error')
        return redirect('/pt/home')

@ptExecute.route("/editTask/")
@ptExecute.route("/editTask/<task>", methods=["GET", "POST"])
def edit(task=None):
    if task != None:
        db.editTask(task, request)
        flash('Tarefa editada com sucesso!', 'sucess')
        return redirect('/pt/home')
    else:
        flash('Erro áo carregar a página, tente novamente mais tarde!', 'error')
        return redirect('/pt/home')

@ptExecute.route("/done/")
@ptExecute.route("/done/<task>")
def done(task=None):
    if task != None:
        db.doneTask(task)
        flash('Tarefa completada com sucesso!', 'sucess')
        return redirect('/pt/home')
    else:
        flash('Erro áo carregar a página, tente novamente mais tarde!', 'error')
        return redirect('/pt/home')

@ptExecute.route("/doneRemove/")
@ptExecute.route("/doneRemove/<task>")
def doneRemove(task=None):
    if task != None:
        db.doneRemoveTask(task)
        flash('Tarefa desfeita com sucesso!', 'warning')
        return redirect('/pt/home')
    else:
        flash('Erro áo carregar a página, tente novamente mais tarde!', 'error')
        return redirect('/pt/home')

@ptExecute.route("/remove/")
@ptExecute.route("/remove/<task>")
def ptExcute(task=None):
    if task != None:
        db.deletTask(task)
        flash('Tarefa deletada com sucesso!', 'sucess')
        return redirect('/pt/home')
    else:
        flash('Erro áo carregar a página, tente novamente mais tarde!', 'error')
        return redirect('/pt/home')