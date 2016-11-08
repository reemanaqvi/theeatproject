from flask import render_template, redirect, request, session, url_for, escape, json
from app import app, models, db
from .forms import UserForm, TripForm, LoginForm
from .models import *
# from models import *    # all functions in model are now accessible here
# Access the models file to use SQL functions


@app.route('/')
@app.route('/index')
def index():
    username = ''
    if 'username' in session:
        username = escape(session['username'])
        return render_template('trips.html', name=username)
    else:
        return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        session["username"] = request.form.get("username")
        session["email"] = request.form.get("email")
        models.insert_user(session["username"], session["email"])
        return redirect(url_for('trips'))


# def authenticate_user(user_name, email):
#     users = models.retrieve_users()
#     for user in users:
#         if user['username'] == user_name and user['email'] == email:
#             return True
#     return False

# @app.route('/trips')
# def trips():
#     #Retreive data from database to display
#     trips = models.retrieve_trips()
#     users = models.retrieve_users()
#     return render_template('trips.html', trips=trips, users=users)

@app.route('/')
@app.route('/trips', methods=['GET', 'POST'])
def trips():
    #
    current_user = ""
    if 'username' in session:
        current_user = escape(session['username'])
        users = models.retrieve_users()
        trips = models.retrieve_trip_data(current_user)
        return render_template('trips.html', trips=trips, user=users)
    else:
        return redirect('login')

# we removed value
@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    if 'username' in session:
        form = TripForm()
        friends = models.retrieve_friends()
        form.friends.choices = [(friend['user_id'], friend['username']) for friend in friends]
        if form.validate_on_submit():
            trip_name = form.trip_name.data
            destination = form.destination.data
            friend = form.friends.data
            username = escape(session['username'])
            models.insert_trip(trip_name, destination, friend, username)
            return redirect('/trips')
        return render_template('create_trip.html', form=form)
    return render_template('login.html')

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        models.insert_user(username, email)
        return redirect('/trips')
    return render_template('create_user.html', form=form)

@app.route('/delete_trip', methods=['GET', 'POST'])
def delete_trip():
    # trip_name = request.form['trip_name']
    # destination = request.form['destination']
    data = json.loads(request.form.get('data'))
    val = int(data['value'].encode('ascii','ignore'))
    models.delete_trip(val)
    return True


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))
