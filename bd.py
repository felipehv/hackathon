#Funciones para la base de datos
import sqlite3
"""
Schema
Evento(id: int, nombre: str, lugar: str, region_id: int, ciudad_id: int, admin_id: int)
Users(id: int, username: str, hash_password: ?)
Favs(event_id: int, user_id: int)
"""

class DBConsults:
    def __init__(self):
        self.connection = sqlite3.connect("./maindb.db")
        self.c = self.connection.cursor()

    def close(self):
        self.connection.close()

    def get_user_id(self,username):
        user_id = self.c.execute("""SELECT id from Users where username = "{}"; """.format(username)).fetchone()[0]
        return user_id[0]

    def get_fav_events(self,user_id):
        #Obtener id de eventos

        #Obtener eventos segun el id
        pass

    def new_user(self,username,hashpass):
        if "," in username:
            return False
        users_list = self.c.execute("""SELECT username from Users where username != "{}" """.format(username)).fetchall()
        max_id = self.c.execute("""SELECT MAX(id) from Users""").fetchone()[0]
        max_id += 1
        if len(users_list) == 0:
            return False
        tup = (max_id, username, hashpass)
        add_user = self.c.execute("""INSERT into Users VALUES({},"{}","{}");""".format(*tup))
        self.connection.commit()
        return True

    def create_event(self, nombre, lugar, region_id, ciudad_id, admin_id, descripcion):
        pass

    def get_events(self):
        events = self.c.execute("""SELECT * from """) 

if __name__ == "__main__":
    a = DBConsults()
    a.new_user("felipe","")
    a.close()