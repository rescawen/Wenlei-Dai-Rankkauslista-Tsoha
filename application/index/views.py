from flask import render_template
from flask_login import login_required, current_user
from application import app

from application.auth.forms import LoginForm
from application.tour.models import Tournament, Players

@app.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        joined = Players.find_tour_with_user(current_user.id)
        return render_template("/index/index.html", form = LoginForm(), 
        tournaments = Tournament.query.all(), 
        ownedtournaments = Tournament.query.filter_by(account_id=current_user.id),
        joinedtournaments = joined,
        Players=Players)
    else:
        return render_template("/index/index.html", form = LoginForm(), tournaments = Tournament.query.all(),Players=Players)    

@app.route("/all_tournaments/<int:page_num>", methods=["GET"])
@login_required
def all_tour(page_num):

    tournaments = Tournament.query.paginate(per_page=5, page=page_num, error_out=True)

    return render_template("/index/all.html", tournaments = tournaments, Players=Players)

@app.route("/joined_tournaments", methods=["GET"])
@login_required
def joined_tour():
    joined = Players.find_tour_with_user(current_user.id)
    return render_template("/index/joined.html", joinedtournaments = joined, Players=Players)

@app.route("/owned_tournaments", methods=["GET"])
@login_required
def owned_tour():
    return render_template("/index/owned.html", ownedtournaments = Tournament.query.filter_by(account_id=current_user.id), Players=Players)
