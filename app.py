import os
import datetime
from flask import Flask
from flask import request, render_template, redirect, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)


#HOME PAGE
@app.route("/")
def index():
    return render_template('index.html')

#LOGIN PAGE
@app.route('/login', methods = ["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        
        #Ensure username
        if not request.form.get('username'):
            error = 'Invalid username'
            return render_template('login.html', error=error)
        elif not request.form.get('password'):
            error = 'Invalid password'
            return render_template('login.html', error=error)

        username = request.form.get('username')

        return do_the_login()
    return render_template('login.html')

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.method.get('username')
        password = request.method.get('password')
        confirm_password = request.method.get('confirm')
        
        if not username or not password or not confirm_password:
            error = "Please fill in all fields"
            return render_template('register.html', error=error)
        if password != confirm_password:
            error = "Passwords don't match"
            return render_template('register.html', error=error)
        

    return render_template('register.html')
