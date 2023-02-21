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
        pass
    else:
        return redirect('/en/home')