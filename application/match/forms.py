from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, BooleanField, validators
from flask_wtf.html5 import NumberInput

  
class MatchForm(FlaskForm):
    player1_score = IntegerField("Player1 Score", [validators.Length(min=0, max=99)], widget=NumberInput())
    player2_score = IntegerField("Player2 Score", [validators.NumberRange(min=0, max=99)], widget=NumberInput())
    winner_boolean = RadioField("Winner", choices=[('player1','top win'),('player2','bottom win')])
    player1_id = IntegerField("Player1")
    player2_id = IntegerField("Player2")
    
  
    class Meta:
        csrf = False