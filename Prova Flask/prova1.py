from flask import Flask, redirect, url_for, render_template, request, session
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import importlib
from datetime import timedelta

model = importlib.import_module("models")


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:progettooobd@localhost:5432/prova_flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if model.db.init_app(app) is None:
        
    print("appis")
    db = SQLAlchemy(app)

else: 

    db = model.db.init_app(app)

migrate = Migrate(app, db)

app.secret_key = "prova_flask"
app.permanent_session_lifetime = timedelta(hours=5)

prova = json.dumps('{"nome": "Jhon", "età" : 29, "isSingle": True}')

dizionarioDaJson = json.loads(prova)


@app.route("/")
def home():
    return render_template("template1.html")

@app.route("/user")
def user():
    return render_template("user.html", user = session["name"])

@app.route("/admin")
def admin():
        
    session["name"] = "Admin"
    session["psw"] = "superSecretPassword"

    return redirect(url_for("user", user = session["name"]))


@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':

            return render_template("login_utente.html")

    else:
        
            cars = model.Aeroporto.query.all()
            session["name"] = request.form["name"]
            session["psw"] = request.form["psw"]
            return redirect( url_for ('user', user = request.form["name"]))

@app.route("/aeroporti", methods = ['POST', 'GET'])
def aeroporto():
    
    if request.method == 'GET':

        return render_template("insert_aeroporto.html")
    
    elif (request.method == 'POST'):

        post = model.Post(post_id = request.form["id_aeroporto"], descrizione = request.form["name_aeroporto"], utente_id = request.form["città_aeroporto"], data_pubblicazione = None)
        db.session.add(post)
        db.session.commit()
        lista = model.Aeroporto.query.all()
        return render_template("base.html", content = lista)

app.static_folder = 'static'

if __name__ == "__main__":
    app.run(debug = True)