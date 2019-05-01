from flask import render_template
from flask_login import login_required, current_user

from application import app
from application.auth.forms import LoginForm
from application.tour.models import Tournament, Players

@app.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        return render_template("/index/index.html", 
        tournaments = Tournament.query.order_by(Tournament.date_modified.desc()).limit(8), 
        ownedtournaments = Tournament.query.filter_by(account_id=current_user.id).order_by(Tournament.date_modified.desc()).limit(8),
        joinedtournaments = Tournament.query.join(Players, Tournament.id==Players.tournament_id).filter_by(account_id=current_user.id).order_by(Tournament.date_modified.desc()).limit(8),
        Players=Players)
    else:
        return render_template("/index/index.html", form = LoginForm(), tournaments = Tournament.query.order_by(Tournament.date_modified.desc()).limit(8),Players=Players)    

@app.route("/all_tournaments/<int:page_num>", methods=["GET"])
@login_required
def all_tour(page_num):
    tournaments = Tournament.query.order_by(Tournament.date_modified.desc()).paginate(per_page=5, page=page_num, error_out=True)
    return render_template("/index/all.html",tournaments=tournaments, Players=Players)

@app.route("/joined_tournaments/<int:page_num>", methods=["GET"])
@login_required
def joined_tour(page_num):
    joinedtournaments = Tournament.query.join(Players, Tournament.id==Players.tournament_id).filter_by(account_id=current_user.id).order_by(Tournament.date_modified.desc()).paginate(per_page=5, page=page_num, error_out=True)
    return render_template("/index/joined.html", joinedtournaments = joinedtournaments, Players=Players)

@app.route("/owned_tournaments/<int:page_num>", methods=["GET"])
@login_required
def owned_tour(page_num):
    ownedtournaments = Tournament.query.filter_by(account_id=current_user.id).order_by(Tournament.date_modified.desc()).paginate(per_page=5, page=page_num, error_out=True)
    return render_template("/index/owned.html", ownedtournaments=ownedtournaments, Players=Players)
