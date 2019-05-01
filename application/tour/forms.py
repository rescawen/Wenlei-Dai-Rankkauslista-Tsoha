from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators
from flask_wtf.html5 import NumberInput
  
class TournamentForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired(message='Must not be a string containing only whitespace'), validators.Length(min=4, max=144)]) 
    playercount = IntegerField("Playercount", [validators.AnyOf(values=[2,4,8,16,32,64,128])], widget=NumberInput())
    description = TextAreaField("Tournament description")

    class Meta:
        csrf = False