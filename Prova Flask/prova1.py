from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "prova_flask"
app.permanent_session_lifetime = timedelta(minutes=5)

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
            return render_template("login.html")
    else:
            session["name"] = request.form["name"]
            session["psw"] = request.form["psw"]
            return redirect( url_for ('user', user = request.form["name"]))



app.static_folder = 'static'

if __name__ == "__main__":
    app.run(debug = True)