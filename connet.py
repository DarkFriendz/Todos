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
        except:
            self.info['reason'] = 'Error saving information, please try again later!'
            self.info['error'] = True

    #Get Task
    def getTask(self, task):
        try:
            with sql.connect(config['Datebase']) as con:
                cur = con.cursor()
                cur.execute('''SELECT * FROM todos''')
                self.info['content'] = cur.fetchall()
                for tasks in self.info['content']:
                    if tasks[0] == int(task):
                        self.info['content'] = tasks
                        self.info['error'] = False
                        return self.info
                    else:
                        self.info['reason'] = 'Error loading page, please try again later!'
                        self.info['error'] = True
                return self.info
        except:
            self.info['reason'] = 'Error loading page, please try again later!'
            self.info['error'] = True
            return self.info

    #Done Task
    def doneTask(self, task):
        try:
            with sql.connect(config['Datebase']) as con:
                cur = con.cursor()
                cur.execute('''UPDATE todos SET done=? WHERE Id=?''', ('S', task))
                self.info['error'] = False
                con.commit()
        except:
            self.info['reason'] = 'Error Completing information, please try again later!'
            self.info['error'] = True

    #Done Remove Task
    def doneRemoveTask(self, task):
        try:
            with sql.connect(config['Datebase']) as con:
                cur = con.cursor()
                cur.execute('''UPDATE todos SET done=? WHERE Id=?''', ('N', task))
                self.info['error'] = False
                con.commit()
        except:
            self.info['reason'] = 'Error Completing information, please try again later!'
            self.info['error'] = True

    #Edit Task
    def editTask(self, task, request):
        try:
            with sql.connect(config['Datebase']) as con:
                cur = con.cursor()
                cur.execute('''SELECT * FROM todos''')
                self.info['content'] = cur.fetchall()
                for tasks in self.info['content']:
                    if tasks[0] == int(task):
                        if request.form['description'] != "":
                            if request.form['date'] != "":
                                try:
                                    if request.form['done']:
                                        cur.execute('''UPDATE todos SET title=?, description=?, done=?, due_date=? WHERE Id=?''', (request.form['title'], request.form['description'], 'S', request.form['date'].split('T')[0], tasks[0]))
                                except:
                                    cur.execute('''UPDATE todos SET title=?, description=?, done=?, due_date=? WHERE Id=?''', (request.form['title'], request.form['description'], 'N', request.form['date'].split('T')[0], tasks[0]))
                            else:
                                try:
                                    if request.form['done']:
                                        cur.execute('''UPDATE todos SET title=?, description=?, done=?, due_date=? WHERE Id=?''', (request.form['title'], request.form['description'], 'S', None, tasks[0]))
                                except:
                                    cur.execute('''UPDATE todos SET title=?, description=?, done=?, due_date=? WHERE Id=?''', (request.form['title'], request.form['description'], 'N', None, tasks[0]))
                        else:
                            if request.form['date'] != "":
                                try:
                                    if request.form['done']:
                                        cur.execute('''UPDATE todos SET title=?, description=?, done=?, due_date=? WHERE Id=?''', (request.form['title'], None, 'S', request.form['date'].split('T')[0], tasks[0]))
                                except:
                                    cur.execute('''UPDATE todos SET title=?, description=?, done=?, due_date=? WHERE Id=?''', (request.form['title'], None, 'N', request.form['date'].split('T')[0], tasks[0]))
                            else:
                                try:
                                    if request.form['done']:
                                        cur.execute('''UPDATE todos SET title=?, description=?, done=?, due_date=? WHERE Id=?''', (request.form['title'], None, 'S', None, tasks[0]))
                                except:
                                    cur.execute('''UPDATE todos SET title=?, description=?, done=?, due_date=? WHERE Id=?''', (request.form['title'], None, 'N', None, tasks[0]))

                        con.commit()
                        self.info['error'] = False
                        return self.info
                    else:
                        self.info['reason'] = 'Error loading page, please try again later!'
                        self.info['error'] = True
        except:
            self.info['reason'] = 'Error Editing information, please try again later!'
            self.info['error'] = True

    #Delet Task
    def deletTask(self, task):
        try:
            with sql.connect(config['Datebase']) as con:
                cur = con.cursor()
                cur.execute('''DELETE FROM todos WHERE Id=?''', (task))
                self.info['error'] = False
                con.commit()
        except:
            self.info['reason'] = 'Error deleting information, please try again later!'
            self.info['error'] = True