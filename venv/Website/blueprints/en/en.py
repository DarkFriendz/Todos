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
            flashs = list(enumerate(get_flashed_messages(with_categories=True)))
            return render_template('/en/home.html', flashs=flashs)
        elif page == 'addTask':
            flashs = list(enumerate(get_flashed_messages(with_categories=True)))
            return render_template('/en/addTask.html', flashs=flashs)
        elif page == 'teste':
            db.teste('teste')
            if db.info['error'] != False:
                flash('Error page not found, please try again later!', 'error')
            else:
                flash('Enviado com Sucesso!', 'sucess')
            return redirect('/en/home')
        flash('Error page not found, please try again later!', 'error')
        return redirect('/en/home')
    else:
        return redirect('/en/home')

#Blueprint Execute
from .enExecute import enExcute

en.register_blueprint(enExcute)