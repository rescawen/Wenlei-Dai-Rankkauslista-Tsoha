from application import db

class Match(db.Model):

    __tablename__ = "match"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
    match_id = db.Column(db.Integer, nullable=False)
    player1_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False) # when creating all match elements instantly this
    player2_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False) # is empty for vast majorit of elements
    
    player1_score = db.Column(db.Integer, nullable=False)
    player2_score = db.Column(db.Integer, nullable=False)

    winner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False) 
    
    # players = db.relationship('User', secondary=players, backref=db.backref('tournaments', lazy=True))

    def __init__(self, tournament_id, match_id):
        self.tournament_id = tournament_id
        self.match_id = match_id
        self.player1_id = 0
        self.player2_id = 0
        self.player1_score = 0
        self.player2_score = 0
        self.winner_id = 0

    @staticmethod
    # whenever we select a winner for the match, this is the function we trigger
    def winner():
        if self.match_id != 1:
            if self.match_id % 2 == 0:
                stmt = text("SELECT winner_id FROM match"
                            " WHERE match_id = :match_id"
                            " AND tournament_id = :tournament_id").params(match_id=match_id, tournament_id=tournament_id)
                
                #INSERT WINNER ID WE JUST QUERIED INTO MATCHID DIVIDED BY TWO AS PLAYER 1

            else: 
                stmt = text("SELECT winner_id FROM match"
                            " WHERE match_id = :match_id"
                            " AND tournament_id = :tournament_id").params(match_id=match_id, tournament_id=tournament_id)

                #INSERT WINNER ID WE JUST QUERIED INTO MATCHID DIVIDED BY TWO ROUNDED DOWN AS PLAYER 2

