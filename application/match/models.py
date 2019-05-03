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
    player1_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    player2_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True) 
    player1_name = db.Column(db.String(144), nullable=False)
    player2_name = db.Column(db.String(144), nullable=False)
    player1_score = db.Column(db.Integer, nullable=False)
    player2_score = db.Column(db.Integer, nullable=False)
    # winner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True) 

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
        # self.winner_id = None
    
    @staticmethod
    def winner(player_id, tournament_id, match_id):
        if match_id != 1:
            if int(match_id) % 2 == 0: # Check if match preceeding the one we are about to update is even 
                
                new_match_id = int(match_id)/2

                stmt = text("UPDATE match"
                            " SET player1_id = :player1_id"
                            " WHERE match_id = :match_id"
                            " AND tournament_id = :tournament_id").params(player1_id = player_id, tournament_id=tournament_id, match_id=new_match_id)
                
                # Insert the id of the winner we selected in radio field as player 1
            else: 
                new_match_id = int(match_id)//2 # Round the match_id down because this is odd

                stmt = text("UPDATE match"
                            " SET player2_id = :player2_id"
                            " WHERE match_id = :match_id"
                            " AND tournament_id = :tournament_id").params(player2_id = player_id, tournament_id=tournament_id, match_id=new_match_id)

               # Insert the id of the winner we selected in radio field as player 2
            db.engine.execute(stmt)

    @staticmethod
    def find_largest_round_by_tour(tournament_id):
        stmt = text("SELECT MAX(round_number) FROM match"
                    " WHERE tournament_id = :tournament_id").params(tournament_id=tournament_id)

        response = db.engine.execute(stmt)

        largest_round = 0

        for row in response:
            largest_round = row[0]

        return largest_round