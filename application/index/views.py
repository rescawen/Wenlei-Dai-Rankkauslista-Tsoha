from flask import render_template
from flask_login import login_required, current_user
from application import app

from application.auth.forms import LoginForm
from application.tour.models import Tournament, Players

@app.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:

        joinedid = Players.find_tour_with_user(current_user.id)
        joined = []
        for id in joinedid:
            joined.append(Tournament.query.get(id))

        return render_template("/index/index.html", form = LoginForm(), 
        tournaments = Tournament.query.all(), 
        ownedtournaments = Tournament.query.filter_by(account_id=current_user.id),
        joinedtournaments = joined)
    else:
        return render_template("/index/index.html", form = LoginForm(), tournaments = Tournament.query.all())    
