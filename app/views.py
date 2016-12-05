from flask import render_template, redirect, request, session, url_for, escape, json
from app import app, models, db
from .forms import SignupForm, LoginForm, FoodForm
from .models import *

@app.route('/')
@app.route('/index')
def index():
	username = ''
	if 'username' in session:
		username = escape(session['username'])
		return redirect(url_for('display_user_foods'))
	else:
		userForm = SignupForm()
		return redirect(url_for('sign_up'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        user = request.form.get("username")
        password = request.form.get("password")
		# print "type of user is: "
		# print user
        if authenticate(user, password):
            myid = retrieve_user_id(user)
            session["id"] = myid[0][0]
            session["username"] = user
            session["password"] = password
            return redirect(url_for('display_user_foods'))
        else:
            return redirect(url_for('index'))

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
	userForm = SignupForm()
	# if request.method=='POST':
	if userForm.validate_on_submit():
		username = userForm.username.data
		password = userForm.password.data
		insert_user(username, password)
		print(username)
		return render_template('home.html')
	return render_template('signup.html', form=userForm)

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('password', None)
	return redirect(url_for('login'))


@app.route('/display_user_foods')
def display_user_foods():
    userid = escape(session['user_id'])
    foods = retrieve_foods(userid)
    print (foods)
    return render_template('trip.html', trips=trips)

def retrieve_foods(userid):
    query = []
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result_cur = cur.execute("select food from user_foods where user =?",(userid,)).fetchall()
        for item in result_cur:
            print ("retrieving foods for this user")
            print (item[0])
        for item in result_cur:
            result = cur.execute("select * from foods where food_id = ?",(item[0],)).fetchall()
            query.append(result[0])
    return query


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
	foodForm = FoodForm()
	print('meh')
	if foodForm.validate_on_submit():
		print("here")
		food_name = foodForm.food_name.data
		ingredients = foodForm.ingredients.data
		diet_restriction = foodForm.diet_restriction.data
		cuisine_type = foodForm.cuisine_type.data
		price = foodForm.price.data
		phone_num = foodForm.phone_num.data
		street_address = foodForm.street_address.data
		city = foodForm.city.data
		state = foodForm.state.data
		zip_code = foodForm.zip_code.data
		country = foodForm.country.data
		userid = escape(session['user_id'])
		insert_food(food_name,ingredients,diet_restriction, cuisine_type, price, phone_num, userid, street_address, city, state, zip_code)
		return render_template('home.html')
	return render_template('add_item.html', form=foodForm)



@app.route('/delete_food', methods=['GET','POST'])
def delete_food():
    data = json.loads(request.form.get('data'))
    id = int(data['id'].encode('ascii','ignore'))
    remove_food(id)
    return True
