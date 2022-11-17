import json
import datetime
from cs50 import SQL
from flask import Flask
from flask import request, render_template, redirect, session, flash
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

#Configure application
app = Flask(__name__)

#Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Configure session to use filesystem instead of signed cookies
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Use SQLite
db = SQL("sqlite:///goals.db")

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


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

        #Query database for username
        username = request.form.get('username')
        password = request.form.get('password')
    
        rows = db.execute("SELECT * FROM users WHERE username = ?", username.lower())
        
        #Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]['hash'], password):
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
        
        # Remember user that logged in
        session['user_id'] = rows[0]['id']

        
        return render_template('index.html')
    return render_template('login.html')

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get('password')
        confirm_password = request.form.get('confirm')

        if not request.form.get("username") or not request.form.get('password') or not request.form.get('confirm'):
            error = "Error: Please fill in all fields"
            return render_template('register.html', error=error, retry=1)
        if password != confirm_password:
            error = "Error: Passwords don't match"
            return render_template('register.html', error=error, retry=1)

        
        usernames = []
        usernames = db.execute("SELECT username FROM users")
        username = username.lower()
        for i in usernames:
            if username in i['username']:
                error = 'Error: Username taken'
                return render_template('register.html', error=error, retry=1)

        hash = generate_password_hash(password)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        return render_template("login.html")

    return render_template('register.html')
