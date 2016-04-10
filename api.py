"""
Api
"""
#import flask
from socket import gethostname
from flask import render_template, request, Flask, session, redirect, send_from_directory, jsonify, url_for
from database import DB
import time
import hashlib
import fbsdk

app = Flask(__name__)
app.secret_key = "123456"
"""
ROUTING
"""
# request.form[atributo]
# request.method = metodo (GET, POST etc)

# Home #### Coming soon
"""
@app.route("/", methods = ["GET", "POST"])
def homepage():
    return render_template("index.html")
"""
##############


@app.route("/login/<username>/<password>", methods=["GET"])
def login(username, password):
    db = DB()
    ans = db.check_log(username, password)
    db.close()
    return jsonify(result=ans)


@app.route("/signup/<username>/<password>/<fbid>", methods=["GET"])
def signup(username, password, fbid):
    if request.method == "GET":
        db = DB()
        db.add_user(username, password, fbid)
        db.close()
        # user = request.form["user"]
        # password = request.url_forrm["password"].encode()
        # fbtoken = request.form["fbtoken"]
        # get_fb_id()
        #password = hashlib.md5(password).hexdigest()
        # db.new_user(user,password)
        # db.close()
        #print(user, password)
        return "1"


"""
Errores de request
"""
# Error 404


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


"""
API
"""


@app.route("/add_ingredient/<username>/<ingredient>", methods=["GET"])
def add_ingredient(username, ingredient):
    if request.method == "GET":
        # username = request.form["username"]
        # ing = reques.form["ingredient"]
        db = DB()
        db.add_ingredient(db.get_user_id(username), ingredient)
        db.close()
        return "1"


@app.route("/remove_ingredient/<username>/<ingredient>", methods=["GET"])
def remove_ingredient(username, ingredient):
    if request.method == "GET":
        # username = request.form["username"]
        # ing = reques.form["ingredient"]
        db = DB()
        db.del_ingredient(db.get_user_id(username), ingredient)
        db.close()
        return "1"


@app.route("/get_user_ingredients/<username>", methods=["GET"])
def get_user_ingredients(username):
    if request.method == "GET":
        # username = request.form["username"]
        # ing = reques.form["ingredient"]
        db = DB()
        ing = db.get_user_ingredients(username)
        send = [("./img/ingredients/{0}.jpg".format(i[1]), i[0])
                for i in ing]
        db.close()
        return jsonify(list=send)


@app.route("/add_user/<username>/<password>", methods=["GET"])
def add_user(username, password):
    if request.method == "GET":
        # username = request.form["username"]
        # ing = reques.form["ingredient"]
        db = DB()
        db.add_user(username, password)
        db.close()
        return jsonify(ans=1)


@app.route("/match_recipes/<id1>/<id2>", methods=["GET"])
def match_recipes(id1, id2):
    if request.method == "GET":
        db = DB()
        #id1 = db.get_user_id(request.form["username1"])
        #id2 = db.get_user_id(request.form["username2"])
        recipes = db.match(id1, id2)
        db.close()
        return jsonify(lista=recipes)


@app.route("/get_ingredients/", methods=["GET"])
def get_ingredients():
    if request.method == "GET":
        db = DB()
        ingredients = db.get_ingredientes()
        send = [("./img/ingredients/{0}.jpg".format(i[0]), i[1])
                for i in ingredients]
        db.close()
        return jsonify(lista=send)


@app.route("/get_recipes/", methods=["GET"])
def get_recipes():
    if request.method == "GET":
        db = DB()
        recipes = db.get_recipes()
        send = [("./img/recipes/{0}.jpg".format(i[0]), i[1])
                for i in recipes]
        db.close()
        return jsonify(lista=send)


@app.route("/cook_recipe/<username>/<rec_name>", methods=["GET"])
def cook_recipe(username, rec_name):
    if request.method == "GET":
        db = DB()
        link = db.cook_recipe(username, rec_name)
        db.close()
        return jsonify(result=link)


# @app.route("/recipes/<string:name>")
# def recipes_by_name(name):
# TODO
#     aux = []
#     return jsonify(events=aux)


# @app.route("/recipes/<int:ni>")  # ni = number of ingredients
# def caca(id):
# TODO
#     aux = []
#     return jsonify(events=aux)


### Route de recursos web ###
@app.route("/img/<path:path>")
def send_img(path):
    return send_from_directory("img", path)

if __name__ == "__main__":
    app.run(host="192.168.0.68", port=6970, debug=True)
