# GOALS
#### Video Demo: <URL here>
#### Description:

The objective is to create a web application where one can record the goals they have. 
The application will encourage the use of tools that are based on the science of setting & achieving goals to assist the user in achieving his/her goals.
The tools used will be based on the research analyzed by Andrew Huberman on episode 55 of his podcast. 

### Tools 
1: Use Focal Vision to Initiate Goal Pursuit
Focusing vision on one point externally and fixing it there for 30-60 sec increases focus/drive to persue goals.

Implementation - Timer with a dot in the center of the page or something not hard to look at at. User will look at image for 30-60 sec

2: Use Aged Self-Images to Self-Motivate
People will persue goals more if they see themseleves aged to the time of the deadline for the goal. 

eg - I want to have graduate in 4 years. Users that visualize themselves mentally in 4 years will be less effective at persuing their goals in contrast to users that 
saw themselves in reality aged by four years by a computer program. 

Implementation - Application asks to use camera, user takes selfie, program ages picture according to the the deadline of their goal. 

3: Visualization of achieveing goal is only helpful at goal setting. 
Visualization of achievement is helpful to set goals, but bad at motivation for the continued persuit of the goal.

Implementation- When prompting users for goals, require them to first visualize them achieving the goal they desire.

4: Visualizing Failure is the Best Ongoing Motivator
Visualizing failure will encourage goal persuit.

Implementation - When users decide to persue goals, one task will be to write one to two sentences of what it will mean to fail at achieveing that goal, or
have them type that when they first are submitting their goals and simply have a reminder of it when they decide to persue the goal. 

5: Make goals moderately Lofty
Best goals are those that are not too easy and not too hard. 

Implementation - When users input their goal, first remind them of this fact. To encourage tough but achievable goals. 

6: Ensure Specificity of Goals, weekly Assessment
More specifc goals are better, but a specific and concrete plan is over 100% better. Having concrete action steps is essential. These action steps should be
modified over time, what does achievement look like in terms of ACTION STEPS? Assessment of progress and updating of ACTION STEPS should occur weekly. 

Implementation - Divide time frame of goal deadline by 2 and have user input what it would look like to have been successful in their goal persuit in that time frame (What skills would they have needed to learn? What must have they done to know that they made progress? etc.) Repeat until timeframe down to 1-3 months. Have user write down 2-3 action steps that they need to take weekly. Have users assign 30 minutes on a specific day of the week where they will sit down, assess their progress, and recalibrate action steps. 

### Design

Homepage (index.html)- Webpage to display welcome message once user logged in, as well as a description of the project when the user is not logged in.

Register (register.html) - Allows user to register, sends data to backend, and encrypts passwords.

Login (login.html)- Checks database for username, and hashpassword, if they match up with someone in the database the user is logged in and taken to index.html.

Pursue (pursue.html)- Purpose of this webpage is to set the individual into pursue mode whenever he clicks on a goal to pursue. Once the button to pursue was clicked the webpage should first ask the user to focus on a spot in the webpage for 60 seconds, afterwards the user will be reminded of the results of his failure to futher motivate him. Then the user can begin goal pursuit. 

Create (create.html) - This is where the user will create their goals. They are encouraged to make moderately lofty goals, because those are best according to the studies reported by Huberman. Users will also be asked to imagine what it would be like to fail and succeed at the goal

Dashboard (dashboard.html) - This is where the user will be able to decided whether to create a new goal or puruse an existing goal. All goals will be listed on cards and the data from the database will return each goal in order, as well as the deadline for each goal. 

App(app.py) - This is where the backend code lives. This is how I am able to store the user's inputs and manipulate it to generate content on the website. 

Styles(styles.css) - This is where I configured the styles of the website. How I made it look pretty(kinda). 