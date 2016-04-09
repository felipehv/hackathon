import sqlite3
import hashlib
class DBConsults:
    def __init__(self):
        self.connection = sqlite3.connect("./maindb.db")
        self.c = self.connection.cursor()

if __name__ == "__main__":
	consult = "SELECT * from Users;"
	db = DBConsults()
	a = db.c.execute(consult)
	print(a.fetchall())
