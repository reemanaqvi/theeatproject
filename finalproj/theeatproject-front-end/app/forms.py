from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class UserForm(Form):
	username = StringField('username', validators=[DataRequired()])
	email = EmailField('email', validators=[DataRequired()])


class TripForm(Form):
	trip_name = StringField('trip_name', validators=[DataRequired()])
	destination = StringField('destination', validators=[DataRequired()])
	friends = SelectField('friends', choices=[], coerce=int, validators=[DataRequired()])

class LoginForm(Form):
	username = StringField('username', validators=[DataRequired()])
	email = EmailField('email', validators=[DataRequired()])
