# ACHIEVE
#### Video Demo: 
<video width="320" height="240" controls>
  <source src="goals_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
#### Description:

The objective is to create a web application where one can record the goals they have. 
The application will encourage the use of tools that are based on the science of setting & achieving goals to assist the user in achieving his/her goals.
The tools used will be based on the research analyzed by Andrew Huberman on episode 55 of his podcast. 

## How It's Made:
**Tech used:** 
Flask, SQLite, HTML, CSS, JavaScript, Bootstrap

**Packages/Dependencies used:**
datetime, cs50, flask, jinja2, flask-session, flash, sql, mongodb, werkzeug

### Lessons Learned: 
First fullstack application, so learned every step of the way. DOM manipulation, database structuring, template rendering, and styling are a few of the things I learned. 

### Design

Homepage (index.html)- Webpage to display welcome message once user logged in, as well as a description of the project when the user is not logged in.

Register (register.html) - Allows user to register, sends data to backend, and encrypts passwords.

Login (login.html)- Checks database for username, and hashpassword, if they match up with someone in the database the user is logged in and taken to index.html.

Pursue (pursue.html)- Purpose of this webpage is to set the individual into pursue mode whenever he clicks on a goal to pursue. Once the button to pursue was clicked the webpage should first ask the user to focus on a spot in the webpage for 60 seconds, afterwards the user will be reminded of the results of his failure to futher motivate him. Then the user can begin goal pursuit. 

Create (create.html) - This is where the user will create their goals. They are encouraged to make moderately lofty goals, because those are best according to the studies reported by Huberman. Users will also be asked to imagine what it would be like to fail and succeed at the goal

Dashboard (dashboard.html) - This is where the user will be able to decided whether to create a new goal or puruse an existing goal. All goals will be listed on cards and the data from the database will return each goal in order, as well as the deadline for each goal. 

App(app.py) - This is where the backend code lives. This is how I am able to store the user's inputs and manipulate it to generate content on the website. 

Styles(styles.css) - This is where I configured the styles of the website. How I made it look pretty(kinda). 