from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=144)])
    password = PasswordField("Password", [validators.Length(min=2, max=144)])
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField("Name", [validators.Regexp(r'^[\w.@+-]+$', message='Must contain only alphanumeric characters, dots, @, + and - without any whitespaces'), 
                                validators.Length(min=2, max=144)])
    username = StringField("Username", [validators.Regexp(r'^[\w.@+-]+$', message='Must contain only alphanumeric characters, dots, @, + and - without any whitespaces'), 
                                        validators.Length(min=2, max=144)])
    password = PasswordField("Password", [validators.Regexp(r'^[\w.@+-]+$', message='Must contain only alphanumeric characters, dots, @, + and - without any whitespaces'), 
                                        validators.Length(min=2, max=144)])
                                        
    class Meta:
        csrf = False