from flask_wtf import FlaskForm
from wtfoorms import Stringfield, Submitfield, Selectfield, Integerfield
from wtforms.validators import DataRequired, ValidationError

class AddGame(FlaskForm):
    G_name = StringField('Name of game', validators = [DataRequired(message= "This field needs to be populated")])
    G_price = DecimalField("Age")
    G_age = SelectField("Game gae rating", choices=[
        ("U", "U"), 
        ("PG", "PG"), 
        ("12", "12"),
        ("15", "15"),
        ("18", "18")])
    submit = SubmitField('Add game name')

class UpdateGame(FlaskForm):
    G_name = StringField('Name of game', validators = [DataRequired(message= "This field needs to be populated")])
    G_price = DecimalField("Age")
    G_age = SelectField("Game gae rating", choices=[
        ("U", "U"), 
        ("PG", "PG"), 
        ("12", "12"),
        ("15", "15"),
        ("18", "18")])
    submit = SubmitField('Update Question')

