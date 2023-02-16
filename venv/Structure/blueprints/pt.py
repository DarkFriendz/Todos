#Assets
from flask import Blueprint

pt = Blueprint('portuguese', __name__, url_prefix='/pt/')

@pt.route('/')
def index():
    return "pt"