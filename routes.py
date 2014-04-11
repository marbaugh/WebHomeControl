from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) 
app.config.from_pyfile('webHomeControl.cfg')
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
db = SQLAlchemy(app)

class Status(db.Model):
	# Setting the table name and
	# creating columns for various fields
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key = True)
    time=db.Column(db.DateTime, index = True, unique = False)
    status=db.Column(db.String, index = True, unique = False)
    
    def __init__(self, time, status):
        # Initializes the fields with entered data
        self.time = datetime.now()
        self.status = status

class DoorStatus(Status):
    pass

class MotionStatus(Status):
    pass

class MotorStatus(Status):
    duration = db.Column(db.Integer, index = False, unique = False)

    def __init__(self, time, status, duration):
        super(MotorStatus, self).__init__(time, status)
        self.duration = duration

# The default route for the app
@app.route('/')
def home():
    return render_template('home.html')

# This view method responds to the URL /motionStatus
@app.route('/motionStatus')
def motion():
    insert_motion = MotionStatus(datetime.now(), 'I See Motion')
    db.session.add(insert_motion)
    db.session.commit()
    flash('Comment was successfully submitted')

    get_motion = MotionStatus.query.all()
    for i in get_motion:
        print i.time
    return render_template('motionStatus.html')

# This view method responds to the URL /doorStatus
@app.route('/doorStatus')
def door():
    return render_template('doorStatus.html')

# This view method responds to the URL /motorStatus
@app.route('/motorStatus')
def motor():
    return render_template('motorStatus.html')

if __name__ == '__main__':
  app.run(host='192.168.3.107', debug=True)
