#Assets
from config import config
from datetime import datetime

#Class Datebase
class db:
    #Config Datebase
    def __init__(self):
        self.directory = config['Datebase']
        self.info = {
            'content': None,
            'error': False
        }

    #teste
    def teste(self, request):
        self.info['error'] = True