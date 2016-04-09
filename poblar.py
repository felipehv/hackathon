import sqlite3


class Generator:
    def __init__(self, dbname):
        self.db = sqlite3.connect(dbname)
        self.c = self.db.cursor()

    def create_tables(self):
        self.c.execute(
            '''CREATE TABLE has (userid int, ingredient varchar(20), PRIMARY KEY(userid, ingredient)) ''')
        self.c.execute(
            '''CREATE TABLE recipes (recid int, name varchar(20), n int, ingredients varchar(255), pic varchar(20), PRIMARY KEY(recid))''')
        self.c.execute(
            '''CREATE TABLE users (userid int, username varchar(20), password varchar(20), PRIMARY KEY(userid))''')

    def test(self):
        self.c.execute("INSERT INTO users VALUES (0,'tamy','t')")
        self.c.execute("INSERT INTO users VALUES (1,'benja','b')")
        self.c.execute("INSERT INTO users VALUES (2,'pipe','p')")
        self.c.execute("INSERT INTO has VALUES (0,'tomate')")
        self.c.execute("INSERT INTO has VALUES (1, 'palta')")
        self.c.execute("INSERT INTO has VALUES (2, 'pan')")
        self.c.execute(
            "INSERT INTO recipes VALUES (0,'Completo Italiano', 3, 'tomate,palta,pan', './pics/0')")
        self.c.execute(
            "INSERT INTO recipes VALUES (1,'Completo Tomate', 2, 'tomate,pan', './pics/1')")

    def close(self):
        self.db.commit()
        self.c.close()

gen = Generator("food.db")
gen.create_tables()
gen.test()
gen.close()
