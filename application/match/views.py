from flask import render_template, flash, request, redirect, url_for
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

    if not form.validate():
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',form.player1_score.data)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',form.player2_score.data)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',form.winner_boolean.data)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',form.player1_id.data)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',form.player2_id.data)

        flash('empty scores for your match result or did not select winner')
        return redirect(url_for('tournament', id=tournament_id))

    editM = Match.query.get(id)

    editM.player1_score = form.player1_score.data
    editM.player2_score = form.player2_score.data

    if form.winner_boolean.data == 'player1':
        editM.winner_id = form.player1_id.data
        Match.winner(form.player1_id.data, tournament_id, match_id)
    elif form.winner_boolean.data == 'player2':
        editM.winner_id = form.player2_id.data
        Match.winner(form.player2_id.data, tournament_id, match_id)

    db.session().commit()

    return redirect(url_for('tournament', id=tournament_id))  

@app.route("/tournament/<string:tournament_id>/match/<string:id>/<string:round_number>/<string:maximum_rounds>", methods=["POST"])
@login_required
def match_delete(id, tournament_id, round_number, maximum_rounds):

    if round_number == maximum_rounds:
        M = Match.query.get(id)

        db.session.delete(M) 
        db.session().commit()
    
    else:
        flash('If you want to delete a match, you must start at the leaflet of the bracket')

    return redirect(url_for('tournament', id=tournament_id))
