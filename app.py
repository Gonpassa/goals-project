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
@app.route("/", methods =['GET', 'POST'])
def index():
    if request.method == 'GET' or request.method == 'POST':
        if session:
            username = db.execute("SELECT username FROM users WHERE id = (?)", session['user_id'])
            return render_template('index.html', username=username[0]['username'])


        return render_template('index.html')


#Dashboard
@app.route("/dashboard", methods = ['GET', 'POST'])
def dashboard():
    if session['user_id']:
        rows = db.execute("SELECT goal_id FROM goal WHERE id IN (?)", session["user_id"])
        rows = len(rows)
        goals = db.execute("SELECT goal, deadline, goal_id FROM goal WHERE id IN (?)", session['user_id'])
        
        return render_template('dashboard.html', rows=rows, goals=goals)
    return redirect('login')


#CREATE GOAL
@app.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        goal = request.form.get("goal")
        deadline = request.form.get("deadline")
        success = request.form.get("success")
        failure = request.form.get('failure')
        now = datetime.date.today()
        db.execute("INSERT INTO goal (goal, success, failure, date_created, deadline, id) VALUES (?, ?, ? ,? ,?, ?)", goal, success, failure, now, deadline, session['user_id'])

        return redirect('dashboard')
    if session["user_id"]:
        return render_template('create.html')
    return render_template('login.html')
    
#PURSUE GOAL
@app.route("/pursue", methods=['GET', 'POST'])
def pursue():
    if request.method == 'POST':
        goal_id = request.get_json()

        goal = db.execute('SELECT goal, failure FROM goal WHERE goal_id = (?)', goal_id)

        return render_template('pursue.html', goal=goal)
    return render_template('pursue.html')

#LOGIN PAGE
@app.route('/login', methods = ["GET", "POST"])
def login():
    error = None
    #forget any user id
    session.clear()

    if request.method == "POST":
        
        #Ensure username
        if not request.form.get('username'):
            error = 'Invalid username'
            return render_template('login.html', error=error, retry=1)
        elif not request.form.get('password'):
            error = 'Invalid password'
            return render_template('login.html', error=error, retry=1)

        #Query database for username
        username = request.form.get('username')
        password = request.form.get('password')
    
        rows = db.execute("SELECT * FROM users WHERE username = ?", username.lower())
        
        #Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]['hash'], password):
            error = 'Invalid username or password'
            return render_template('login.html', error=error, retry=1)
        
        # Remember user that logged in
        session['user_id'] = rows[0]['id']

        
        return render_template('index.html')
    return render_template('login.html')


@app.route('/logout')
def logout():

    session.clear()
    return redirect("/")

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
