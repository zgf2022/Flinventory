from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RoomForm(FlaskForm):
    campusname = SelectField('Campus', validators=[DataRequired()])
    primaryuse = SelectField('Primary users', validators=[DataRequired()])
    roomname = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add Room')