#Assets
from flask import Blueprint, redirect

#Blueprint
en = Blueprint('english', __name__, url_prefix='/en/')

#index
@en.route('/')
@en.route('/<page>')
def index(page=None):
    if page != None:
        if page == 'home':
            return "home"
    else:
        return redirect('/en/home')