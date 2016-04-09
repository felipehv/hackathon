"""
Api
"""
#import flask
from flask import render_template, request, Flask, session, redirect, send_from_directory, jsonify, url_for
from bd import DBConsults
import time
import hashlib

app = Flask(__name__)
app.secret_key = "123456"
"""
ROUTING
"""
#request.form[atributo]
#request.method = metodo (GET, POST etc)

#### Home ####
@app.route("/", methods = ["GET", "POST"])
def homepage():
    return render_template("index.html")
##############

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        return request.form["nombre"]
    else:
        return render_template("caca.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        db = DBConsults()
        user = request.form["user"]
        password = request.form["password"].encode()
        password = hashlib.md5(password).hexdigest()
        db.new_user(user,password)
        db.close()
        return redirect("/login")
    
    elif request.method == "GET":
        #TODO
        return render_template("caca.html")

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
@app.route("/recipes", methods = ["GET", "POST"])
def eventos():
    #TODO
    aux = []
    return jsonify(events = aux)

@app.route("/recipes/<string:name>")
def evento_n(id):
    #TODO
    aux = []
    return jsonify(events = aux)




###########


### Route de recursos web ###
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/pages/<path:path>')
def send_page(path):
    return send_from_directory('pages', path)

@app.route('/font-awesome/css/<path:path>')
def send_font_awesome_css(path):
    return send_from_directory('font-awesome/css', path)

@app.route('/font-awesome/fonts/<path:path>')
def send_font_awesome_fonts(path):
    return send_from_directory('font-awesome/fonts', path)

@app.route('/font-awesome/scss/<path:path>')
def send_font_awesome_scss(path):
    return send_from_directory('font-awesome/scss', path)

@app.route('/font-awesome/less/<path:path>')
def send_font_awesome_less(path):
    return send_from_directory('font-awesome/less', path)

@app.route('/dist/css/<path:path>')
def send_dist_css(path):
    return send_from_directory('dist/css', path)

#Bowercomponents folder
@app.route('/bower_components/bootstrap/dist/css/<path:path>')
def send_bc_bs_dist_css(path):
    return send_from_directory('/bower_components/bootstrap/dist/css/', path)

@app.route('/bower_components/bootstrap/dist/<path:path>')
def send_bc_bs_dist(path):
    return send_from_directory('/bower_components/bootstrap/dist/', path)

@app.route('/bower_components/morrisjs/<path:path>')
def send_bc_bs_morrisjs(path):
    return send_from_directory('/bower_components/morrisjs/', path)

@app.route('/bower_components/font-awesome/<path:path>')
def send_bc_bs_dist_css(path):
    return send_from_directory('/bower_components/morrisjs/', path)
############################################################

"""
ADMIN SITE pronto muajaja
"""


if __name__ == "__main__":
    app.run(host = "192.168.0.43",port = 6969, debug = True)
