#Assets
from flask import Blueprint, redirect, render_template, flash, get_flashed_messages

#Blueprint
en = Blueprint('english', __name__, url_prefix='/en/')

#index
@en.route('/')
@en.route('/<page>')
def index(page=None):
    if page != None:
        if page == 'home':
            flashs = list(enumerate(get_flashed_messages(with_categories=True)))
            print(flashs)
            return render_template('/en/home.html', flashs=flashs)
        elif page == 'teste':
            
            flash('error',  'error')
            flash('error',  'error')
            flash('error',  'error')
            return redirect('/en/home')
        return redirect('/en/home')
    else:
        return redirect('/en/home')