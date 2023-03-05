#Assets
import sqlite3
from datetime import datetime

#Class Datebase
class db():
    #Config Datebase
    def __init__(self, directory:str):
        #Directory
        self.directory = directory

        #Result
        self.result = {
            'info': None,
            'error': False
        }

        #Table
        conn = sqlite3.connect(directory)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT NOT NULL, description TEXT, done VARCHAR(1) NOT NULL DEFAULT 'N', due_date DATE, created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);''')
        #cursor.execute('''INSERT INTO todo (title, description, due_date, created_at, updated_at) VALUES ('ola', 'ola', '2023-02-30', '2023-02-30 00:00:00', '2023-02-30 00:00:00')''')
        conn.commit()
        conn.close()

    #Get Table List
    def getAll(self, lang):
        self.result = {'info': None, 'error': False}
        try:
            with sqlite3.connect(self.directory) as conn:
                cur = conn.cursor()
                cur.execute('''SELECT * FROM todo''')
                data = []
                for row in cur.fetchall():
                    if row[4] != None and row[4] != '':
                        now = datetime.now()
                        now = datetime.strftime(now, '%Y%m%d%H%M%S')
                        dataFormat = row[4].replace('-', '')+'000000'
                        if now > dataFormat:
                            rows = {
                                'id': row[0],
                                'title': row[1],
                                'description': row[2],
                                'done': row[3],
                                'due_date': row[4],
                                'created_at': row[5],
                                'updated_at': row[6],
                                'expired': False
                            }
                        else:
                            rows = {
                                'id': row[0],
                                'title': row[1],
                                'description': row[2],
                                'done': row[3],
                                'due_date': row[4],
                                'created_at': row[5],
                                'updated_at': row[6],
                                'expired': True
                            }
                    else:
                        rows = {
                            'id': row[0],
                            'title': row[1],
                            'description': row[2],
                            'done': row[3],
                            'due_date': row[4],
                            'created_at': row[5],
                            'updated_at': row[6],
                            'expired': True
                        }
                    data.append(rows)
                self.result['info'] = data
                return self.result
        except:
            if self.result['info'] == None:
                print('error')

    #Get Row
    def getRow(self, id:str):
        self.result = {'info': None, 'error': False}
        try:
            with sqlite3.connect(self.directory) as conn:
                cur = conn.cursor()
                cur.execute('''SELECT * FROM todo WHERE id=?''', id)
                row = cur.fetchone()
                row = {
                        'id': row[0],
                        'title': row[1],
                        'description': row[2],
                        'done': row[3],
                        'due_date': row[4],
                        'created_at': row[5],
                        'updated_at': row[6]
                }
            self.result['info'] = row
        except:
            if self.result['info'] == None:
                print('error')

    #Add Task
    def addTask(self, request:list):
        self.result = {'info': None, 'error': False}
        try:
            with sqlite3.connect(self.directory) as conn:
                cur = conn.cursor()
                if request['date'] != '':
                    date = request['date']
                    date2 = date.replace('T', ' ')+':00'
                    date = date.split('T')[0]
                else: 
                    date = None
                    date2 = datetime.now()
                    date2 = datetime.strftime(date2, '%Y-%m-%d %H:%M:00')
                try:
                    if request['done']:
                        if request['description'] != '':
                            cur.execute('''INSERT INTO todo (done, title, description, due_date, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)''', ('S', request['title'], request['description'], date, date2, date2))
                        else:
                            cur.execute('''INSERT INTO todo (done, title, description, due_date, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)''', ('S', request['title'], None, date, date2, date2))
                except:
                    if request['description'] != '':
                        cur.execute('''INSERT INTO todo (title, description, due_date, created_at, updated_at) VALUES (?, ?, ?, ?, ?)''', (request['title'], request['description'], date, date2, date2))
                    else:
                        cur.execute('''INSERT INTO todo (title, description, due_date, created_at, updated_at) VALUES (?, ?, ?, ?, ?)''', (request['title'], None, date, date2, date2))
                conn.commit()
            self.result['info'] = "Saved"
        except:
            if self.result['info'] == None:
                print('error')

    #Delete Task
    def deletTask(self, id:str):
        self.result = {'info': None, 'error': False}
        try:
            with sqlite3.connect(self.directory) as conn:
                cur = conn.cursor()
                cur.execute('''DELETE FROM todo WHERE id=?''', id)
                conn.commit()
            self.result['info'] == 'Deleted'
        except:
            if self.result['info'] == None:
                print('error')

    #Edit Task
    def editTask(self, id:str, request:list):
        self.result = {'info': None, 'error': False}
        try:
            with sqlite3.connect(self.directory) as conn:
                cur = conn.cursor()
                date = datetime.now()
                date = datetime.strftime(date, '%Y-%m-%d %H:%M:00')
                try:
                    if request['done']:
                        cur.execute('''UPDATE todo SET title=?, description=IFNULL(?, 'none'), done=?, due_date=IFNULL(?, 'none'), updated_at=? WHERE id=?''', (request['title'], request['description'], 'S', request['date'].split("T")[0], date, id))
                except:
                    cur.execute('''UPDATE todo SET title=?, description=IFNULL(?, 'none'), done=?, due_date=IFNULL(?, 'none'), updated_at=? WHERE id=?''', (request['title'], request['description'], 'N', request['date'].split("T")[0], date, id))
                conn.commit()
            self.result['info'] == 'Edited'
        except:
            if self.result['info'] == None:
                print('error')

    #Done Task
    def Done(self, id:str):
        self.result = {'info': None, 'error': False}
        try:
            with sqlite3.connect(self.directory) as conn:
                cur = conn.cursor()
                cur.execute('''UPDATE todo SET done=? WHERE id=?''', ('S', id))
                conn.commit()
            self.result['info'] == 'Done'
        except:
            if self.result['info'] == None:
                print('error')

    #NotDone Task
    def NotDone(self, id:str):
        self.result = {'info': None, 'error': False}
        try:
            with sqlite3.connect(self.directory) as conn:
                cur = conn.cursor()
                cur.execute('''UPDATE todo SET done=? WHERE id=?''', ('N', id))
                conn.commit()
            self.result['info'] == 'NotDone'
        except:
            if self.result['info'] == None:
                print('error')