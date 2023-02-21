#Assets
import sqlite3 as sql
from config import config
from datetime import datetime

#Class Datebase
class db:
    #Config Datebase
    def __init__(self):
        self.directory = config['Datebase']
        self.info = {
            'content': None,
            'reason': None,
            'error': False
        }
        with sql.connect(config['Datebase']) as con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS todos (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title VARCHAR(200) NOT NULL, description TEXT, done VARCHAR(1) NOT NULL DEFAULT 'N', due_date DATE, created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)''')
            #task_data = ('Buy groceries', 'Milk, bread, eggs', 'N', '2023-02-23')
            #cur.execute('''INSERT INTO todos (title, description, done, due_date) VALUES (?, ?, ?, ?)''', task_data)
            con.commit()

    #Get Tasks
    def tasks(self):
        with sql.connect(config['Datebase']) as con:
            cur = con.cursor()
            cur.execute('''SELECT * FROM todos''')
            self.info['content'] = cur.fetchall()
            print(self.info)
            return self.info

    #Add Task
    def addTask(self, request):
        try:
            with sql.connect(config['Datebase']) as con:
                cur = con.cursor()
                if request.form['description'] != "":
                    if request.form['date'] != "":
                        try:
                            if request.form['done']:
                                cur.execute('''INSERT INTO todos (title, description, done, due_date) VALUES (?, ?, ?, ?)''', (request.form['title'], request.form['description'], 'S', request.form['date'].split('T')[0]))
                        except:
                            cur.execute('''INSERT INTO todos (title, description, done, due_date) VALUES (?, ?, ?, ?)''', (request.form['title'], request.form['description'], 'N', request.form['date'].split('T')[0]))
                    else:
                        try:
                            if request.form['done']:
                                cur.execute('''INSERT INTO todos (title, description, done, due_date) VALUES (?, ?, ?, ?)''', (request.form['title'], request.form['description'], 'N', None))
                        except:
                            cur.execute('''INSERT INTO todos (title, description, done, due_date) VALUES (?, ?, ?, ?)''', (request.form['title'], request.form['description'], 'N', None))
                else:
                    if request.form['date'] != "":
                        try:
                            if request.form['done']:
                                cur.execute('''INSERT INTO todos (title, description, done, due_date) VALUES (?, ?, ?, ?)''', (request.form['title'], None, 'S', request.form['date'].split('T')[0]))
                        except:
                            cur.execute('''INSERT INTO todos (title, description, done, due_date) VALUES (?, ?, ?, ?)''', (request.form['title'], None, 'N', request.form['date'].split('T')[0]))
                    else:
                        try:
                            if request.form['done']:
                                cur.execute('''INSERT INTO todos (title, description, done, due_date) VALUES (?, ?, ?, ?)''', (request.form['title'], None, 'N', None))
                        except:
                            cur.execute('''INSERT INTO todos (title, description, done, due_date) VALUES (?, ?, ?, ?)''', (request.form['title'], None, 'N', None))
                self.info['error'] = False
                con.commit()
        except:
            self.info['reason'] = 'Error saving information, please try again later!'
            self.info['error'] = True

    #Delet Task
    def deletTask(self, task):
        print(task)
        try:
            with sql.connect(config['Datebase']) as con:
                cur = con.cursor()
                cur.execute('''DELETE FROM todos WHERE Id=?''', (task))
                self.info['error'] = False
                con.commit()
        except:
            self.info['reason'] = 'Error deleting information, please try again later!'
            self.info['error'] = True