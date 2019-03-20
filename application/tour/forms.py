from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
  
class TournamentForm(FlaskForm):
    name = StringField("Name")
    playercount = IntegerField("Playercount")
  
    class Meta:
        csrf = False