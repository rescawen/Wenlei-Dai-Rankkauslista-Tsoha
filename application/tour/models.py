from application import db

from sqlalchemy.sql import text

class Players(object):

    def __init__(self, account_id, tournament_id):
        self.account_id = account_id
        self.tournament_id = tournament_id
        
    @staticmethod
    def find_tour_with_user(user_id):
        stmt = text("SELECT tournament_id FROM players "
                    "WHERE account_id = account_id").params(account_id=user_id)

        response = db.engine.execute(stmt)

        print('AAAAAAAAAAAAAAAAAA', response)

        userstournaments = []
        for row in response:
            
            userstournaments.append(row[0])

        return userstournaments

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
    
    # players = db.relationship('User', secondary=players, backref=db.backref('tournaments', lazy=True))

    def __init__(self, name, playercount):
        self.name = name
        self.player_count = playercount




