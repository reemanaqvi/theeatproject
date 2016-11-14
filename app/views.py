from flask import render_template, redirect, request, session, url_for, escape, json
from app import app, models, db
from .forms import UserForm, TripForm, LoginForm
from .models import *


@app.route('/')
@app.route('/index')
def index():
    username = ''
    if 'username' in session:
        username = escape(session['username'])
        return render_template('home.html', name=username)
    else:
        return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        session["username"] = request.form.get("username")
        session["email"] = request.form.get("email")
        models.insert_user(session["username"], session["email"])
        return redirect(url_for('login'))

@app.route('/signup')
def signup():
    
    return redirect(url_for('signup'))



@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))
