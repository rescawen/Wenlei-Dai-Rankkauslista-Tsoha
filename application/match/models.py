from application import db

from sqlalchemy.sql import text

class Match(db.Model):

    __tablename__ = "match"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
    match_id = db.Column(db.Integer, nullable=False)
    round_number = db.Column(db.Integer, nullable=False)
    player1_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True) # when creating all match elements instantly this
    player2_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True) # is empty for vast majorit of elements
    player1_name = db.Column(db.String(144), nullable=False)
    player2_name = db.Column(db.String(144), nullable=False)
    player1_score = db.Column(db.Integer, nullable=False)
    player2_score = db.Column(db.Integer, nullable=False)

    winner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True) 

    def __init__(self, tournament_id, match_id, round_number, player1_id, player2_id):
        self.tournament_id = tournament_id
        self.match_id = match_id
        self.round_number = round_number
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.player1_name = "Player 1"
        self.player2_name = "Player 2"
        self.player1_score = 0
        self.player2_score = 0
        self.winner_id = None
    
    # whenever we select a winner for the match, this is the function we trigger
    @staticmethod
    def winner(player_id, tournament_id, match_id):
        if match_id != 1:
            if int(match_id) % 2 == 0:
                
                new_match_id = int(match_id)/2

                stmt = text("UPDATE match"
                            " SET player1_id = :player1_id"
                            " WHERE match_id = :match_id"
                            " AND tournament_id = :tournament_id").params(player1_id = player_id, tournament_id=tournament_id, match_id=new_match_id)
                
                #INSERT WINNER ID WE JUST QUERIED INTO MATCHID DIVIDED BY TWO AS PLAYER 1

            else: 
                new_match_id = int(match_id)//2 

                stmt = text("UPDATE match"
                            " SET player2_id = :player2_id"
                            " WHERE match_id = :match_id"
                            " AND tournament_id = :tournament_id").params(player2_id = player_id, tournament_id=tournament_id, match_id=new_match_id)

                #INSERT WINNER ID WE JUST QUERIED INTO MATCHID DIVIDED BY TWO ROUNDED DOWN AS PLAYER 2

            db.engine.execute(stmt)

    # WE SHOULD ADD ANOTHER METHOD THAT USES THIS WINNER METHOD TO AUTOMATICALLY PUSH MATCHES THAT DON'T HAVE OPPONENTS ON THE FIRST ROUND FORWARD

