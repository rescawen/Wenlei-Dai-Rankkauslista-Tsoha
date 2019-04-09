from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tour.models import Tournament, Players
from application.tour.forms import TournamentForm

from application.match.models import Match
from application.match.forms import MatchForm

@app.route("/tournament/<string:tournament_id>/match/<string:id>/<string:match_id>", methods=["POST"])
@login_required
def match_submit(id, tournament_id, match_id):
    
    form = MatchForm(request.form)

    editM = Match.query.get(id)

    editM.player1_score = form.player1_score.data
    editM.player2_score = form.player2_score.data
    # editM.winner_id = form.winner_id.data

    db.session().commit()

    return redirect(url_for('tournament', id=tournament_id))  