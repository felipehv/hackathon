"""
Api
"""
#import flask
from flask import render_template, request, Flask, session, redirect, send_from_directory, jsonify, url_for
from bd import 
import time
import hashlib

app = Flask(__name__)
app.secret_key = "123456"
"""
ROUTING
"""
#request.form[atributo]
#request.method = metodo (GET, POST etc)

#### Home #### Coming soon
"""
@app.route("/", methods = ["GET", "POST"])
def homepage():
    return render_template("index.html")
"""
##############

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        return request.form["nombre"]
    else:
        return 0

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        #db = DBConsults()
        user = request.form["user"]
        password = request.form["password"].encode()
        password = hashlib.md5(password).hexdigest()
        #db.new_user(user,password)
        #db.close()
        print(user,password)
        return True


"""
Errores de request
"""
#Error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


"""
API
"""
@app.route("/add_ingredient/<string:username>/<string:ing>", methods = ["POST"])
def add_ingredient(user,ing):
    pass

@app.route("/add_ingredient/<string:username>/<string:ing>", methods = ["POST"])
def remove_ingredient(user,ing):
    pass

@app.route("/user/<string:name>")
def refresh_user(username):
    pass
    
@app.route("/recipes", methods = ["GET", "POST"])
def recipes():
    #TODO  - Returns all recipes
    aux = []
    return jsonify(events = aux)

@app.route("/recipes/<string:name>")
def recipes_by_name(name):
    #TODO
    aux = []
    return jsonify(events = aux)

@app.route("/recipes/<int:ni>") #ni = number of ingredients
def caca(id):
    #TODO
    aux = []
    return jsonify(events = aux)





### Route de recursos web ###
@app.route("/img/<path:path>")
def send_img(path):
    return send_from_directory("img",path)

if __name__ == "__main__":
    app.run(host = "192.168.0.43",port = 6969, debug = True)
