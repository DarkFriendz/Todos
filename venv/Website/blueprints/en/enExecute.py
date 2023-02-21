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

        flash('Error loading page, please try again later!', 'error')
        return redirect('/en/home')
    else:
        return redirect('/en/home')