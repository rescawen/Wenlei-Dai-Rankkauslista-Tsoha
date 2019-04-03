from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tour.models import Tournament, Players
from application.tour.forms import TournamentForm

from application.match.models import Match

@app.route("/tournament/<string:id>")
@login_required
def tournament(id):
    players = Players.find_users_of_tour(id)

    if Tournament.query.get(id).started == True:
        tm = Match.query.filter_by(tournament_id=id)

        for player in players:
            for m in tm:
                if player.id == m.player1_id:
                    m.player1_name = player.name
                elif player.id == m.player2_id:
                    m.player2_name = player.name

        return render_template("tour/tournament.html", id=id, tournament = Tournament.query.get(id), tournamentplayers = players, matches = tm)
    else:
        return render_template("tour/tournament.html", id=id, tournament = Tournament.query.get(id), tournamentplayers = players)

@app.route("/tour/new/")
@login_required
def tour_new():
    return render_template("tour/createform.html", form = TournamentForm())

@app.route("/tour/create", methods=["POST"])
@login_required
def tour_create():
    form = TournamentForm(request.form)

    if not form.validate():
        return render_template("tour/createform.html", form = form)

    newT = Tournament(form.name.data, form.playercount.data, current_user.id)
    db.session().add(newT)
    db.session().commit()

    return redirect(url_for("index"))  

@app.route("/tournament/<string:id>/edit")
@login_required
def tour_edit_page(id):
    return render_template("tour/editform.html", id=id, tournament = Tournament.query.get(id), form = TournamentForm())

@app.route("/tournament/<string:id>/edit", methods=["POST"])
@login_required
def tour_edit(id):
    form = TournamentForm(request.form)

    if not form.validate():
        return render_template("tour/editform.html", id=id, tournament = Tournament.query.get(id), form = form)

    editT = Tournament.query.get(id)
    
    editT.name = form.name.data
    editT.player_count = form.playercount.data 

    db.session().commit()

    return redirect(url_for('tournament', id=id))  

@app.route("/tournament/<string:id>/delete", methods=["POST"])
@login_required
def tour_delete(id):

    T = Tournament.query.get(id)

    db.session.delete(T) 
    db.session().commit()

    return redirect(url_for("index")) 

@app.route("/tournament/<string:id>/join", methods=["POST"])
@login_required
def tour_join(id):

    newP = Players(current_user.id, id)

    db.session().add(newP)
    db.session().commit()

    return redirect(url_for('tournament', id=id))  

@app.route("/tournament/<string:id>/start", methods=["POST"])
@login_required
def tour_start(id):

    players = Players.find_user_id_of_tour(id) # might need to do this again, can be passed through tournament page
    minimum_player_count = 2
    bracket_size = 0

    while True:
        print('stuck')
        if len(players) <= minimum_player_count:
            bracket_size = minimum_player_count
            break
        else:
            minimum_player_count = minimum_player_count * 2

    player1_list = players[:bracket_size//2]
    player2_list = players[bracket_size//2:]

    for i in range(bracket_size-1):

        if i > (bracket_size/2)-2: # why is this -2 ??????

            if not player2_list:
                newM = Match(id, i+1, player1_list.pop(), 0)
            else:
                newM = Match(id, i+1, player1_list.pop(), player2_list.pop())
        else:
            newM = Match(id, i+1, 0, 0)

        db.session().add(newM)
        db.session().commit()

    startT = Tournament.query.get(id)
    startT.started = True
    db.session().commit()

    return redirect(url_for('tournament', id=id))  

