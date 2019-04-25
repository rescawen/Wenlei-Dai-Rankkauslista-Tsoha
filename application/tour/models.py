from application import db
from application.auth.models import User

from sqlalchemy.sql import text

class Players(object):

    def __init__(self, account_id, tournament_id):
        self.account_id = account_id
        self.tournament_id = tournament_id
        
    @staticmethod
    def find_tour_with_user(account_id):
        stmt = text("SELECT * FROM tournament"
                     " LEFT JOIN players ON players.tournament_id = tournament.id"
                     " WHERE (players.account_id = :account_id)").params(account_id=account_id)

        # stmt = text("SELECT tournament_id FROM players"
        #            " WHERE account_id = :account_id").params(account_id=account_id)

        response = db.engine.execute(stmt)

        # userstournaments = []

        # for row in response:
        #     userstournaments.append(Tournament.query.get(row[0]))

        return response

    @staticmethod
    def find_users_of_tour(tournament_id):
        stmt = text("SELECT * FROM account"
                     " LEFT JOIN players ON players.account_id = account.id"
                     " WHERE (players.tournament_id = :tournament_id)").params(tournament_id=tournament_id)

        # stmt = text("SELECT account_id FROM players"
        #            " WHERE tournament_id = :tournament_id").params(tournament_id=tournament_id)

        response = db.engine.execute(stmt)

        # tournamentplayers = []

        # for row in response:
        #     tournamentplayers.append(User.query.get(row[0])) # should only get users non sensitive information

        return response
    
    @staticmethod
    def find_user_id_of_tour(tournament_id):
        stmt = text("SELECT account_id FROM players"
                   " WHERE tournament_id = :tournament_id").params(tournament_id=tournament_id)

        response = db.engine.execute(stmt)

        tournamentplayers = []

        for row in response:
            tournamentplayers.append(row[0]) # should only get users non sensitive information

        return tournamentplayers

    @staticmethod
    def find_user_count_of_tour(tournament_id):
        stmt = text("SELECT COUNT(*) FROM account"
                     " LEFT JOIN players ON players.account_id = account.id"
                     " WHERE (players.tournament_id = :tournament_id)").params(tournament_id=tournament_id)

        response = db.engine.execute(stmt)

        count = 0

        for row in response:
            count = row[0]

        return count

    @staticmethod
    def find_tour_count_of_user(account_id):
        stmt = text("SELECT COUNT(*) FROM tournament"
                     " LEFT JOIN players ON players.tournament_id = tournament.id"
                     " WHERE (players.account_id = :account_id)").params(account_id=account_id)

        response = db.engine.execute(stmt)

        count = 0

        for row in response:
            count = row[0]

        return count

    @staticmethod
    def delete_rows_with_tour(tournament_id):
        stmt = text("DELETE FROM players"
                    " WHERE tournament_id = :tournament_id").params(tournament_id=tournament_id)
        
        db.engine.execute(stmt)


players = db.Table('players',
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True),
    db.Column('tournament_id', db.Integer, db.ForeignKey('tournament.id'), primary_key=True)
)

db.mapper(Players, players)

class Tournament(db.Model):

    __tablename__ = "tournament"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    player_count = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    started = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, playercount, account_id, description):
        self.name = name
        self.player_count = playercount
        self.account_id = account_id
        self.description = description
        self.started = False

    def is_started(self):
        return self.started



