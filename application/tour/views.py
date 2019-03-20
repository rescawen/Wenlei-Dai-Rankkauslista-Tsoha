from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.tour.models import Tournament
from application.tour.forms import TournamentForm

# MOVED TO INDEX
# @app.route("/", methods=["GET"])
# def tour_index():
#     return render_template("index/index.html", tournaments = Tournament.query.all())

  
@app.route("/tour/new/")
@login_required
def tour_new():
    return render_template("tour/createform.html", form = TournamentForm())

@app.route("/tournament/<string:id>")
@login_required
def tournament(id):
    return render_template("tour/tournament.html", id=id, tournament = Tournament.query.get(id))

@app.route("/tournament/<string:id>/edit")
@login_required
def tour_edit_page(id):
    return render_template("tour/editform.html", id=id, tournament = Tournament.query.get(id), form = TournamentForm())

@app.route("/tour/create", methods=["POST"])
@login_required
def tour_create():
    form = TournamentForm(request.form)

    newT = Tournament(form.name.data, form.playercount.data)
    
    db.session().add(newT)
    db.session().commit()

    return redirect(url_for("index"))  

@app.route("/tournament/<string:id>/edit", methods=["POST"])
@login_required
def tour_edit(id):
    form = TournamentForm(request.form)

    T = Tournament.query.get(id)

    T.name = form.name.data
    T.playercount = form.playercount.data # this line maybe never even happening

    db.session().commit()

    return redirect(url_for('tournament', id=id))  
