import sqlite3


class DB:

    def __init__(self):
        self.db = sqlite3.connect("food.db")
        self.c = self.db.cursor()

    def close(self):
        self.db.commit()
        self.c.close()

    def add_user(self, username, password):
        userid = self.c.execute("SELECT MAX(userid) FROM users").fetchone()[0]
        userid = int(userid) + 1
        self.c.execute(
            "INSERT INTO users VALUES ({0}, '{1}','{2}')".format(userid, username, password))

    def add_ingredient(self, userid, ingname):
        self.c.execute(
            "INSERT INTO has VALUES ({0}, '{1}')".format(int(userid), ingname))

    def del_ingredient(self, userid, ingname):
        self.c.execute("DELETE FROM has WHERE userid={0} and ingredient='{1}'".format(
            int(userid), ingname))

    def match(self, *ids):
        recetas = []
        ingredients = []
        for i in ids:
            ingredients.append(self.c.execute(
                "SELECT has.ingredient FROM has WHERE userid={}".format(i)).fetchall())
        group_ingredients = []
        for i in ingredients:
            for j in i:
                group_ingredients.append(j[0])
        for j in self.c.execute("SELECT * FROM recipes"):
            uses = j[3].split(",")
            filtro = list(filter(lambda x: x not in group_ingredients, uses))
            if len(filtro) == 0:
                recetas.append((j[1], "./img/recipes/{}.jpg".format(j[0])))
        return recetas

    def get_user_id(self, username):
        user_id = self.c.execute(
            "SELECT userid from users where username = '{}'".format(username)).fetchone()[0]
        return int(user_id)

    def get_ingredientes(self):
        return self.c.execute("SELECT * FROM ingredients").fetchall()

# db = DB()
# db.add_user("jesse","j")
# db.close()
