from application import db

from sqlalchemy.sql import text

class Players(object):

    def __init__(self, account_id, tournament_id):
        self.account_id = account_id
        self.tournament_id = tournament_id
        
    @staticmethod
    def find_tour_with_user(account_id):
        stmt = text("SELECT tournament_id FROM players"
                   " WHERE account_id = :account_id").params(account_id=account_id)

        response = db.engine.execute(stmt)

        userstournaments = []
        for row in response:
            userstournaments.append(row[0])
        return userstournaments

    @staticmethod
    def find_users_of_tour(tournament_id):
        stmt = text("SELECT account_id FROM players"
                   " WHERE tournament_id = :tournament_id").params(tournament_id=tournament_id)

        response = db.engine.execute(stmt)

        tournamentplayers = []
        for row in response:
            tournamentplayers.append(row[0])
        return tournamentplayers

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
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    started = db.Column(db.Boolean, nullable=False)

    # players = db.relationship('User', secondary=players, backref=db.backref('tournaments', lazy=True))

    def __init__(self, name, playercount, account_id):
        self.name = name
        self.player_count = playercount
        self.account_id = account_id
        self.started = False

    def is_started(self):
        return self.started



