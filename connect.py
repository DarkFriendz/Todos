#Assets
import sqlite3
from datetime import datetime

#Class Datebase
class db():
    #Config Datebase
    def __init__(self, config:str):
        #Directory
        self.directory = config['Datebase']

    