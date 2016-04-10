"""
Api
"""
from socket import gethostname
from flask import render_template, request, Flask, session, redirect, send_from_directory, jsonify, url_for, ext, Response
from database import DB
import time
import hashlib
import fbsdk
from json import dumps


def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

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

    resp = Response(dumps(ans), status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


@app.route("/signup/<username>/<password>/<fbid>", methods=["GET"])
def signup(username, password, fbid):
    if request.method == "GET":
        db = DB()
        send = db.add_user(username, password, fbid)
        db.close()

        resp = Response(dumps(send), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp


"""
Errores de request
"""
# Error 404


@app.errorhandler(404)
def page_not_found(error):
    return "Error", 404


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

        send = 1

        resp = Response(dumps(send), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp


@app.route("/remove_ingredient/<username>/<ingredient>", methods=["GET"])
def remove_ingredient(username, ingredient):
    if request.method == "GET":

        db = DB()
        db.del_ingredient(db.get_user_id(username), ingredient)
        db.close()
        send = 1

        resp = Response(dumps(send), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp


@app.route("/get_user_ingredients/<username>", methods=["GET"])
def get_user_ingredients(username):
    if request.method == "GET":

        db = DB()
        ing = db.get_user_ingredients(username)
        send = [("./img/ingredients/{0}.jpg".format(i[1]), i[0])
                for i in ing]
        db.close()

        resp = Response(dumps(send), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp


@app.route("/add_user/<username>/<password>/<fbid>", methods=["GET"])
def add_user(username, password, fbid):
    if request.method == "GET":

        db = DB()
        db.add_user(username, password, fbid)
        db.close()

        send = 1

        resp = Response(dumps(send), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp


@app.route("/match_recipes/<u1>/<u2>", methods=["GET"])
def match_recipes(u1, u2):
    if request.method == "GET":
        db = DB()
        recipes = db.match(u1, u2)
        db.close()

        resp = Response(
            dumps(recipes), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp


@app.route("/get_ingredients/", methods=["GET"])
def get_ingredients():
    if request.method == "GET":
        db = DB()
        ingredients = db.get_ingredientes()
        send = [("./img/ingredients/{0}.jpg".format(i[0]), i[1])
                for i in ingredients]
        db.close()

        resp = Response(dumps(send), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp


@app.route("/get_recipes/", methods=["GET"])
def get_recipes():
    if request.method == "GET":
        db = DB()
        recipes = db.get_recipes()
        send = [("./img/recipes/{0}.jpg".format(i[0]), i[1])
                for i in recipes]
        db.close()

        resp = Response(dumps(send), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp


@app.route("/get_friends/<u>", methods=["GET"])
def get_friends(u):
    if request.method == "GET":
        db = DB()
        send = db.get_friends(u)
        db.close()

        resp = Response(dumps(send), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp

@app.route("/get_pic/<u>", methods=["GET"])
def get_pic(u):
    if request.method == "GET":
        db = DB()
        send = db.get_pic(u)
        db.close()

        resp = Response(dumps(send), status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp

# @app.route("/cook_recipe/<username>/<rec_name>", methods=["GET"])
# def cook_recipe(username, rec_name):
#     if request.method == "GET":
#         db = DB()
#         link = db.cook_recipe(username, rec_name)
#         db.close()
#         return jsonify(result=link)


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
    app.run(host="192.168.0.68", port=6969, debug=True)
