from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tour.models import Tournament, Players
from application.tour.forms import TournamentForm

from application.match.models import Match
from application.match.forms import MatchForm

@app.route("/tournament/<string:tournament_id>/match/<string:id>/submit", methods=["POST"])
@login_required
def match_submit(id, tournament_id):

    editM = Match.query.get(id)

    if not editM:
        flash('The match your trying to submit does not exist')
        return redirect(url_for('tournament', id=tournament_id)) 

    T = Tournament.query.get(tournament_id)

    if not (editM.player1_id == current_user.id or editM.player2_id == current_user.id or T.account_id == current_user.id):
        flash('You are trying to submit score to a match you do not have permission for')
        return redirect(url_for('tournament', id=tournament_id))
    
    form = MatchForm(request.form)

    if not form.validate():
        flash('empty scores for your match result or did not select winner')
        return redirect(url_for('tournament', id=tournament_id))

    editM.player1_score = form.player1_score.data
    editM.player2_score = form.player2_score.data

    if form.winner_boolean.data == 'player1':
        editM.winner_id = form.player1_id.data
        Match.winner(form.player1_id.data, tournament_id, editM.match_id)
    elif form.winner_boolean.data == 'player2':
        editM.winner_id = form.player2_id.data
        Match.winner(form.player2_id.data, tournament_id, editM.match_id)

    db.session().commit()

    return redirect(url_for('tournament', id=tournament_id))  

@app.route("/tournament/<string:tournament_id>/match/<string:id>/delete", methods=["POST"])
@login_required
def match_delete(id, tournament_id):

    deleteM = Match.query.get(id)

    if not deleteM:
        flash('The match your trying to delete does not exist')
        return redirect(url_for('tournament', id=tournament_id))

    T = Tournament.query.get(tournament_id)

    if not T.account_id == current_user.id:
        flash('You are trying to delete a match that you do not have permission for')
        return redirect(url_for('tournament', id=tournament_id))

    if deleteM.round_number == Match.find_largest_round_by_tour(tournament_id):
        db.session.delete(deleteM) 
        db.session().commit()
    else:
        flash('If you want to delete a match, you must start at the leaflet of the bracket')

    return redirect(url_for('tournament', id=tournament_id))
