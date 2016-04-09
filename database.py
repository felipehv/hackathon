import sqlite3


class DB:

    def __init__(self, dbname):
        self.db = sqlite3.connect(dbname)
        self.c = self.db.cursor()

    def close(self):
        self.db.commit()
        self.c.close()

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
        group_ingredients = [i[0][0] for i in ingredients]
        for j in self.c.execute("SELECT * FROM recipes"):
            uses = j[3].split(",")
            filtro = list(filter(lambda x: x not in group_ingredients, uses))
            if len(filtro) == 0:
                recetas.append((j[1], j[4]))
        return recetas



db = DB("food.db")
print(db.match(0, 2, 1))
db.close()
