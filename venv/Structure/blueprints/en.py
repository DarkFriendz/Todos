#Assets
from flask import Blueprint

en = Blueprint('english', __name__, url_prefix='/en/')

@en.route('/')
def index():
    return "en"