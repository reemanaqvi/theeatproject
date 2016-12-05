from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class SignupForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])


class FoodForm(Form):
	food_name = StringField('food_name', validators=[DataRequired()])
	ingredients = StringField('ingredients', validators=[DataRequired()])
	diet_restriction = StringField('diet_restriction', validators=[DataRequired()])
	cuisine_type = StringField('cuisine_type', validators=[DataRequired()])
	price = IntegerField('price', validators=[DataRequired()])
	phone_num = IntegerField('phone_num', validators=[DataRequired()])
	# image = BLOB('image', validators=[DataRequired()])
	street_address = StringField('street-address', validators=[DataRequired()])
	city = StringField('city', validators=[DataRequired()])
	state = StringField('state', validators=[DataRequired()])
	zip_code = StringField('zipcode', validators=[DataRequired()])
	country = StringField('country', validators=[DataRequired()])

class LoginForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])
