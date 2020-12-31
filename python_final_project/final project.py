import sqlite3
import time
class Database:
    def __init__(self):
        self.db = sqlite3.connect('D.db')
        self.x = self.db.cursor()

    def create_users_table(self):
        self.x.execute('''CREATE TABLE if not exists users
        (rowid integer primary key,
        name text unique,
        password text);''')
        self.db.commit()

    def create_score_table(self):
        self.x.execute('''CREATE TABLE if not exists scores
        (rowid integer primary key,
        name text unique,
        difficulty text,
        time start game,
        time end game,
        score integer);''')
        self.db.commit()

    def create_user(self, name, password):
        try:
            if self.check(name):
                return False
            else:
                self.x.execute('INSERT INTO users (name,password) VALUES (?,?)', (name, password))
                self.db.commit()
                return True
        except:
            return False

    def check(self, name):
        self.x.execute('''SELECT*from users where name = ? ''', (name,))
        user = self.x.fetchone()
        return user is not None

    def check_password(self, name, password):
        self.x.execute('''SELECT password FROM users WHERE name = ?''', (name,))
        code = self.x.fetchone()
        if code[0] == password:
            return True
        else:
            return False

    def score_calc(self, difficulty, time):
        d = {"hard": 0.5, "mediume": 1, "easy": 2}
        return time * d[difficulty]

    def starting_game(self,name, difficulty):
        self.x.execute('''INSERT INTO scores(name,difficulty,time start game)
         VALUES(?,?,?)''', (name, difficulty, int(time.time())))
        self.db.commit()

    def add_scoring(self, name):
        self.x.execute('''SELECT * FROM scores WHERE name = ? AND end game = NULL ''', (name,))
        in_game = self.x.fetchone()
        self.x.execute('''UPDATE scores SET end game = ?, 
        score = ? WHERE name = ?''',
                       (time.time() - in_game[3], self.score_calc(in_game[2], time.time() - in_game[3]), name))

    def best_player(self):
        self.x.execute('''SELECT * FROM scores ORDER BY score''')
        self.db.commit()
        best_score = self.x.fetchall()
        return best_score


database = Database()
database.create_users_table()
database.create_user('adam', '1234')
database.starting_game('adam','easy')
input()
database.add_scoring('adam')
print(database.best_player())
