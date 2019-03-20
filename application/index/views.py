from flask import render_template
from application import app

from application.auth.forms import LoginForm
from application.tour.models import Tournament

@app.route("/", methods=["GET"])
def index():
    return render_template("/index/index.html", form = LoginForm(), tournaments = Tournament.query.all())