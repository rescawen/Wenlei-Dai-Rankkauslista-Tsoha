from flask import render_template
from application import app

from application.auth.forms import LoginForm

@app.route("/")
def index():
    return render_template("index.html", form = LoginForm())