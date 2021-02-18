from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template1.html", content="prova contenuto dinamica riuscita")

@app.route("/<name><cognome>")
def user(name, cognome):
    return f"Hello {name} {cognome}!"

@app.route("/admin")
def admin():
	return redirect(url_for("user", name= "Admin", cognome = "di questo sito"))

if __name__ == "__main__":
    app.run()