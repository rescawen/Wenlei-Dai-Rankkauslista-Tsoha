from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tour.models import Tournament, Players
from application.tour.forms import TournamentForm
from application.match.models import Match
from application.match.forms import MatchForm

@app.route("/tournament/<string:id>", methods=["GET", "POST"])
@login_required
def tournament(id):

    T = Tournament.query.get(id)

    if not T:
        flash('The following tournament your looking for does not exist')
        return redirect(url_for("index"))  

    players = Players.find_users_of_tour(id)

    if T.started == True:
        tm = Match.query.filter_by(tournament_id=id).order_by('match_id')
        
        maximum_rounds = 0

        for player in players:
            for m in tm:
                if m.round_number > maximum_rounds:
                    maximum_rounds = m.round_number
                if player.id == m.player1_id:
                    m.player1_name = player.name
                elif player.id == m.player2_id:
                    m.player2_name = player.name
        
        if maximum_rounds == 0:
            T.started = False
            db.session().commit()
            return redirect(url_for('tournament', id=id))

        return render_template("tournament/tournament.html", id=id, tournament = Tournament.query.get(id), tournamentplayers = players, matches = tm, form = MatchForm(), maximum_rounds = maximum_rounds)
    
    if T.started == False:
        return render_template("tournament/tournament.html", id=id, tournament = Tournament.query.get(id), tournamentplayers = players)

@app.route("/tournament/new/")
@login_required
def tour_new():
    return render_template("tournament/createform.html", form = TournamentForm())

@app.route("/tournament/create", methods=["POST"])
@login_required
def tour_create():
    form = TournamentForm(request.form)

    if not form.validate():
        return render_template("tournament/createform.html", form = form)

    newT = Tournament(form.name.data, form.playercount.data, current_user.id, form.description.data)
    db.session().add(newT)
    db.session().commit()

    return redirect(url_for("index"))  

@app.route("/tournament/<string:id>/editpage", methods=["GET"])
@login_required
def tour_edit_page(id):
    editT = Tournament.query.get(id)

    if not editT:
        flash('The tournament your trying to edit for does not exist')
        return redirect(url_for("index")) 

    if not editT.account_id == current_user.id:
        flash('you are trying to edit a tournament you do not have permission for')
        return redirect(url_for('tournament', id=id))

    form = TournamentForm()
    form.name.data = editT.name
    form.playercount.data = editT.player_count
    form.description.data = editT.description

    return render_template("tournament/editform.html", id=id, tournament=editT, form=form)

@app.route("/tournament/<string:id>/edit", methods=["POST"])
@login_required
def tour_edit(id):

    editT = Tournament.query.get(id)

    if not editT:
        flash('The tournament your trying to edit for does not exist')
        return redirect(url_for("index"))  

    if not editT.account_id == current_user.id:
        flash('you are trying to edit a tournament you do not have permission for')
        return redirect(url_for('tournament', id=id))

    form = TournamentForm(request.form)

    if not form.validate():
        return render_template("tournament/editform.html", id=id, tournament = Tournament.query.get(id), form = form)
    
    editT.name = form.name.data
    editT.player_count = form.playercount.data 
    editT.description = form.description.data

    db.session().commit()

    return redirect(url_for('tournament', id=id))  

@app.route("/tournament/<string:id>/delete", methods=["POST"])
@login_required
def tour_delete(id):

    deleteT = Tournament.query.get(id)

    if not deleteT:
        flash('The tournament your trying to delete does not exist')
        return redirect(url_for("index"))  

    if not deleteT.account_id == current_user.id:
        flash('You are trying to delete a tournament that you do not have permission for')
        return redirect(url_for('tournament', id=id))

    if deleteT.started == True:
        flash('You are trying to delete a tournament that has already started')
        return redirect(url_for('tournament', id=id))

    Players.delete_rows_with_tour(id)

    db.session.delete(deleteT) 
    db.session().commit()

    return redirect(url_for("index")) 

@app.route("/tournament/<string:id>/join", methods=["POST"])
@login_required
def tour_join(id):

    joinT = Tournament.query.get(id)

    if not joinT:
        flash('The tournament your trying to join does not exist')
        return redirect(url_for("index"))  

    players = Players.find_user_id_of_tour(id)

    for player in players:
        if player == current_user.id:
            flash('You have already signed up for the tournament')
            return redirect(url_for('tournament', id=id))

    if len(players) == joinT.player_count:
        flash('The tournament you want to sign up for is full')
        return redirect(url_for('tournament', id=id))

    newP = Players(current_user.id, id)

    db.session().add(newP)
    db.session().commit()

    return redirect(url_for('tournament', id=id))  

@app.route("/tournament/<string:id>/start", methods=["POST"])
@login_required
def tour_start(id):

    startT = Tournament.query.get(id)

    if not startT:
        flash('The tournament your trying to start does not exist')
        return redirect(url_for("index")) 

    if not startT.account_id == current_user.id:
        flash('You are trying to start a tournament that you do not have permission for')
        return redirect(url_for('tournament', id=id))

    players = Players.find_user_id_of_tour(id)

    if len(players) == 0:
        flash('You must have at least one player to start a tournament')
        return redirect(url_for('tournament', id=id)) 

    # Below starts the algorithm for generating the matches

    minimum_player_count = 2
    bracket_size = 0
    round_number = 1
    round_counter = 1
    round_multiplier = 2

    # Creating theoretical maximum amount of matches, for example 5,6,7 amount of players in a tournament all get bumped -> 8
    # This allows us to retain the single elimination bracket balance.

    while True:
        if len(players) <= minimum_player_count:
            bracket_size = minimum_player_count
            break
        else:
            minimum_player_count = minimum_player_count * 2

    player1_list = players[:bracket_size//2] # Dividing our player list 
    player2_list = players[bracket_size//2:] # into two separate ones 

    for i in range(bracket_size-1):

        if i > (bracket_size/2)-2: # theoretically should be -1, but -2 gives correct result in practice

            # Here we are creating the left most round of the bracket, in the other the first rounds to be played

            if not player2_list:
                newM = Match(id, i+1, round_number, player1_list.pop(), None)
            else:
                newM = Match(id, i+1, round_number, player1_list.pop(), player2_list.pop())
        else:

            # Creating the rest of the matches which obviously do not have players yet.

            newM = Match(id, i+1, round_number, None, None)

        db.session().add(newM)
        db.session().commit()

        if i+1 == round_counter:
            round_counter = round_counter + round_multiplier
            round_number += 1
            round_multiplier = round_multiplier * 2

    
    startT.started = True
    db.session().commit()

    return redirect(url_for('tournament', id=id))  



