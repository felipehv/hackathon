import sqlite3


class DB:

    def __init__(self):
        self.db = sqlite3.connect("food.db")
        self.c = self.db.cursor()

    def close(self):
        self.db.commit()
        self.c.close()

    def check_log(self, username, password):
        passw = self.c.execute(
            "SELECT password from users where username = '{}'".format(username)).fetchone()
        if passw:
            passw = passw[0]
            if passw == password:
                return True
            else:
                return False
        else:
            return False

    def add_user(self, username, password, fbid):
        # userid = self.c.execute("SELECT MAX(userid) FROM users").fetchone()[0]
        # userid = int(userid) + 1
        self.c.execute(
            "INSERT INTO users VALUES ({0}, '{1}','{2}')".format(int(fbid), username, password))

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

    def get_user_ingredients(self, username):
        ingredients = self.c.execute(
            "SELECT ingredient, ingid from has,ingredients where userid = {} and ingredient = name".format(self.get_user_id(username))).fetchall()
        ing = [(i[0], i[1]) for i in ingredients]
        return ing

    def get_ingredientes(self):
        return self.c.execute("SELECT * FROM ingredients").fetchall()

    def get_recipes(self):
        return self.c.execute("SELECT recid,name from recipes")

    def cook_recipe(self, username, rec_name):
        mis_ing = [i[0] for i in self.get_user_ingredients(username)]
        rec_ing = self.c.execute(
            "SELECT ingredients from recipes where name='{}'".format(rec_name)).fetchone()[0]
        rec_ing = rec_ing.split(",")
        return mis_ing


db = DB()
print(db.cook_recipe("tamy", "Completo Italiano"))
# db.add_user("jesse","j")
# print(db.get_ingredients("tamy"))
# db.close()
