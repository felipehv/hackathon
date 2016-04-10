import sqlite3


class Generator:
    def __init__(self):
        self.db = sqlite3.connect("food.db")
        self.c = self.db.cursor()

    def create_tables(self):
        self.c.execute(
            '''CREATE TABLE has (userid int, ingredient varchar(20), PRIMARY KEY(userid, ingredient)) ''')
        self.c.execute(
            '''CREATE TABLE recipes (recid int, name varchar(20), n int, ingredients varchar(255), PRIMARY KEY(recid))''')
        self.c.execute(
            '''CREATE TABLE users (userid int, username varchar(20), password varchar(20), PRIMARY KEY(userid))''')
        self.c.execute(
            '''CREATE TABLE ingredients (ingid int, name varchar(20), PRIMARY KEY(ingid))''')

    def test(self):
        self.add_ingredients()
        self.c.execute("INSERT INTO users VALUES (0,'tamy','t')")
        self.c.execute("INSERT INTO users VALUES (1,'benja','b')")
        self.c.execute("INSERT INTO users VALUES (2,'pipe','p')")
        self.c.execute("INSERT INTO has VALUES (0,'Tomate')")
        self.c.execute("INSERT INTO has VALUES (0,'Palta')")
        self.c.execute("INSERT INTO has VALUES (1, 'HotDog')")
        self.c.execute("INSERT INTO has VALUES (1, 'Mayonesa')")
        self.c.execute("INSERT INTO has VALUES (2, 'Arroz')")
        self.c.execute(
            "INSERT INTO recipes VALUES (0,'Completo Italiano', 3, 'Tomate,Palta,HotDog,Mayonesa')")
        self.c.execute(
            "INSERT INTO recipes VALUES (1,'Pan con queso', 3, 'Pan,Queso')")
        self.c.execute(
            "INSERT INTO recipes VALUES (2,'Chorrillana', 3, 'Papas,Aceite,Huevos,Marraqueta,Bistecs')")
        self.c.execute(
            "INSERT INTO recipes VALUES (3,'Pisco', 3, 'Pisco,Coca Cola')")

    def close(self):
        self.db.commit()
        self.c.close()

    def add_ingredients(self):
        with open("ingredientes.txt", "r") as f:
            for i in f.readlines():
                if i != "\n":
                    data = i.split(",")
                    self.c.execute(
                        "INSERT INTO ingredients VALUES ({0},'{1}')".format(data[0], data[1].strip()))


gen = Generator()
gen.create_tables()
gen.test()
gen.close()
