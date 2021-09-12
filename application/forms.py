from flask_wtf import FlaskForm
from wtfoorms import Stringfield, Submitfield, Selectfield, Integerfield
from wtforms.validators import DataRequired, ValidationError

class AddGame(FlaskForm):
    G_name = StringField('Name of game', validators = [DataRequired(message= "This field needs to be populated")])
    G_price = DecimalField("Age")
    G_age = SelectField("Game game rating", choices=[
        ("U", "U"), 
        ("PG", "PG"), 
        ("12", "12"),
        ("15", "15"),
        ("18", "18")])
    submit = SubmitField('Add game name')

class AddStore(FlaskForm):
    SE_address = StringField('Address of store', validators = [DataRequired(message= "This field needs to be populated")])
    SE_phone_number = StringField('Phone number of store', validators = [DataRequired(message= "This field needs to be populated")])
    submit = SubmitField('Add new store')

class AddStore(FlaskForm):
    SE_name = StringField('Name of staff', validators = [DataRequired(message= "This field needs to be populated")])
    SE_address = StringField('Address of staff', validators = [DataRequired(message= "This field needs to be populated")])
    SE_phone_number = StringField('Phone number of staff', validators = [DataRequired(message= "This field needs to be populated")])
    submit = SubmitField('Add new staff member')

class UpdateGame(FlaskForm):
    G_name = StringField('Name of game', validators = [DataRequired(message= "This field needs to be populated")])
    G_price = DecimalField("Age")
    G_age = SelectField("Game game rating", choices=[
        ("U", "U"), 
        ("PG", "PG"), 
        ("12", "12"),
        ("15", "15"),
        ("18", "18")])
    submit = SubmitField('Update Question')

class SelectGame(FlaskForm):
    G_id = SelectField('Game', choices=[])
    submit = SubmitField('Choose Game')
