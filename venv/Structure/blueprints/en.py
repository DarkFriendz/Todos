#Assets
from flask import Blueprint, render_template, redirect

en = Blueprint('english', __name__, url_prefix='/en/')

@en.route('/')
@en.route('/<page>')
def index(page=None):
    if page != None:
        if page == "work":
            tasks = ["ola", "ola2"]
            return render_template("en/work.html", tasks=tasks)
    else:
        return redirect('/en/work')