from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from flask_wtf.html5 import NumberInput

  
class MatchForm(FlaskForm):
    player1_score = IntegerField("Player1 Score", [validators.Length(min=4)], widget=NumberInput())
    player2_score = IntegerField("Player2 Score", [validators.NumberRange(min=2, max=1028)], widget=NumberInput())
    #winner_id = IntegerField("Winner", [validators.NumberRange(min=2, max=1028)])
  
    class Meta:
        csrf = False