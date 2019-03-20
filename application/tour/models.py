from application import db

class Tournament(db.Model):

    __tablename__ = "tournament"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    player_count = db.Column(db.Integer, nullable=False)

    def __init__(self, name, playercount):
        self.name = name
        self.player_count = playercount

