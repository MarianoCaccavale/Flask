from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def home():
    return render_template("template1.html", content="prova contenuto dinamica riuscita")

@app.route("/admin")
def admin():
	return redirect(url_for("user", name= "Admin"))

@app.route("/culo")
def culo():
    return f"<h1>CULO</h1>"



@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
            
            return render_template("login.html")
    else:
            return redirect( url_for ('culo'))


app.static_folder = 'static'

if __name__ == "__main__":
    app.run(debug = True)