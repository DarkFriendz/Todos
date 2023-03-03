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

    #Get Table
    def getAll(self, lang):
        try:
            with sqlite3.connect(self.directory) as conn:
                cur = conn.cursor()
                cur.execute('''SELECT * FROM todo''')
                data = []
                for row in cur.fetchall():
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
                            'expired': False
                        }
                    data.append(rows)
                conn.close()
                self.result['info'] = data
                return self.result
        except:
            if self.result['info'] == None:
                print('error')