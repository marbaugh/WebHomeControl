from flask import Flask, render_template, flash, request, jsonify
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
    hardware=db.Column(db.String, index = True, unique = False)
    time=db.Column(db.DateTime, index = True, unique = False)
    status=db.Column(db.String, index = True, unique = False)
    
    __mapper_args__ = {
            'polymorphic_on':hardware,
            'polymorphic_identity':'none'
    }

    def __init__(self, time, status):
        # Initializes the fields with entered data
        self.time = datetime.now()
        self.status = status

class DoorStatus(Status):
    __mapper_args__ = {
            'polymorphic_identity':'door'
    }

class MotionStatus(Status):
    __mapper_args__ = {
            'polymorphic_identity':'motionSensor'
    }

class MotorStatus(Status):
    duration = db.Column(db.Integer, index = False, unique = False)

    def __init__(self, time, status, duration):
        super(MotorStatus, self).__init__(hardware, time, status)
        self.duration = duration

# The default route for the app
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/doorSensor/status/<status>', methods = ['POST'])
def doorStatus(status):
    if request.method == 'POST':
        insert_door = None
        if status == 'opened':
            insert_door = DoorStatus(datetime.now(), status)
        elif status == 'closed':
            insert_door = DoorStatus(datetime.now(), status)
        else:
            pass
    db.session.add(insert_door)
    db.session.commit()
    return 'success' 

@app.route('/doorSensor/history')
@app.route('/doorSensor/history/<int:history>')
def doorSensor_history(history=1):
	return jsonify(DoorStatus.query.order_by(DoorStatus.time).limit(history))

@app.route('/motionSensor/status/<status>', methods = ['POST'])
def motionStatus(status):
    if request.method == 'POST':
        insert_motion = None
        if status == 'motion':
            insert_motion = MotionStatus(datetime.now(), status)
        else:
            pass
    db.session.add(insert_motion)
    db.session.commit()
    return 'success' 

@app.route('/motionSensor/history')
@app.route('/motionSensor/history/<int:history>')
def motionSensor_history(history=1):
	return jsonify(MotionStatus.query.order_by(MotionStatus.time).limit(history))

if __name__ == '__main__':
  app.run(host='192.168.3.107', debug=True)
