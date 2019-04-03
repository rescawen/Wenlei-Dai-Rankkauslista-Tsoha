from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
  
class TournamentForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=4)])
    playercount = IntegerField("Playercount", [validators.NumberRange(min=2, max=1028)])
  
    class Meta:
        csrf = False