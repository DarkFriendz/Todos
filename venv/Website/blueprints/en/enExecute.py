#Assets
from flask import Blueprint, redirect, render_template, flash, get_flashed_messages

#Datebase
from connet import db

#Get Datebase
db = db()

#Blueprint
enExcute = Blueprint('englishExecute', __name__, url_prefix='/execute')

@enExcute.route("/")
@enExcute.route("/<action>")
def index(action=None):
    if action != None:
        if action == "addTask":
            return "ola"

        flash('Error loading page, please try again later!', 'error')
        return redirect('/en/home')
    else:
        return redirect('/en/home')