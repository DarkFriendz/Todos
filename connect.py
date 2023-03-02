#Assets
import sqlite3
from datetime import datetime

#Class Datebase
class db():
    #Config Datebase
    def __init__(self, directory:str):
        #Directory
        self.conn = sqlite3.connect(directory)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT NOT NULL, description TEXT, done VARCHAR(1) NOT NULL DEFAULT 'n', due_date DATE, created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);''')

    def getAll(self):
        self.cursor.execute('SELECT * FROM todo')
        print(self.cursor.fetchall())

    def close(self):
        '''Close the Database connection.'''
        self.cursor.close()
        self.conn.close()