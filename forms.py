from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RoomForm(FlaskForm):
    campusname = SelectField('Campus', choices=[('admin', 'admin'), ('khs', 'khs'), ('kms', 'kms'),
    	('kis', 'kis'), ('kes', 'kes'), ('kps', 'kps')], validators=[DataRequired()])
    primaryuse = SelectField('Primary users',choices=[('cte', 'cte'), ('sped', 'sped'), ('staff', 'staff'), ('generaled', 'generaled')], validators=[DataRequired()])
    roomname = StringField('Room Name', validators=[DataRequired()])
    submit = SubmitField('Add Room')