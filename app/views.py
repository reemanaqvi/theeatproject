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
		return render_template('signup.html')

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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	userForm = SignupForm()
	if userForm.validate_on_submit():
		fullname = userForm.fullname.data
		username = userForm.username.data
		street_address = userForm.street_address.data
		city = userForm.city.data
		state = userForm.state.data
		zip_code = userForm.zip_code.data
		country = userForm.country.data
		password = userForm.password.data
		print ("userForm.username")
		userid = escape(session["username"])
		insert_user(username, street_address, city, state, zip_code, password)
		return redirect('/index')
	return render_template('home.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))


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

# @app.route('/trip')
# def display_trip():
#     userid = escape(session['id'])
#     trips = retrieve_trips(userid)
#     print trips
#     return render_template('trip.html', trips=trips)

# @app.route('/delete_trip', methods=['GET','POST'])
# def delete_trip():
#     data = json.loads(request.form.get('data'))
#     id = int(data['id'].encode('ascii','ignore'))
#     remove_trips(id)
#     return True

@app.route('/add_item', methods=['GET', 'POST'])
def create_food():
    foodForm = FoodForm()
    if foodForm.validate_on_submit():
        food_name = foodForm.food_name.data
        ingredients = foodForm.ingredients.data
        diet_restriction = foodForm.diet_restriction.data
        cuisine_type = foodForm.cuisine_type.data
        price = foodForm.price.data
        phone_num = foodForm.phone_num.data
        image = foodForm.image.data
        # print("tripForm.friend")
        # print tripForm
        userid = escape(session['id'])
        insert_food(food_name, ingredients, diet_restriction, cuisine_type, price, phone_num, image, user_id)
        return redirect('/index')
    return render_template('create_food.html', form=foodForm)
