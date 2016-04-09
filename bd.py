#Funciones para la base de datos
import sqlite3

"""has(userid int, ingredient varchar(20), PRIMARY KEY(userid, ingredient)) """
""" recipes (recid int, name varchar(20), n int, ingredients varchar(255), pic varchar(20), PRIMARY KEY(recid))''') """
'''users (userid int, username varchar(20), password varchar(20), PRIMARY KEY(userid))'''

class DBConsults:
    def __init__(self):
        self.connection = sqlite3.connect("./1.db")
        self.c = self.connection.cursor()

    def close(self):
        self.connection.close()

    def get_user_id(self,username):
        user_id = self.c.execute("""SELECT userid from Users where username = "{}"; """.format(username)).fetchone()[0]
        return user_id

    def get_ingredients(self,user_id):
        pass

    def new_user(self,username,hashpass,fb_id):
        if "," in username:
            return False
        #Evita sql injection

        users_list = self.c.execute("""SELECT username from Users where username != "{}" """.format(username)).fetchall()
        if len(users_list) == 0:
            return False
        tup = (fb_id, username, hashpass)
        add_user = self.c.execute("""INSERT into Users VALUES({},"{}","{}");""".format(*tup))
        self.connection.commit()
        return True

    def add_match(self, username, ingredient):
        user_id = self.get_user_id(username)
        tup = user_id,ingredient
        a = self.c.execute("""INSERT into has VALUES({},"{}");""".format(*tup))
        self.connection.commit()
        self.close()
        return str(user_id)

    def remove_match(self, username, ingredient):
        user_id = self.get_user_id(username) #DELETE
        #a = self.c.execute("""INSERT into Users VALUES({},{});""".format(*tup))
        #self.connection.commit() 

if __name__ == "__main__":
    a = DBConsults()
    a.add_match("pipe","caca")
    a.close()