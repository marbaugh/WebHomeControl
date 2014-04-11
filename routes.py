from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) 
app.config.from_pyfile('hello.cfg')
db = SQLAlchemy(app)

class Status(db.model):
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
@app.route('/motionStatus', methods=['GET', 'POST'])
def new():
	pass

# This view method responds to the URL /doorStatus
@app.route('/doorStatus', methods=['GET', 'POST'])
def new():
	pass

# This view method responds to the URL /motorStatus
@app.route('/motorStatus', methods=['GET', 'POST'])
def new():
	pass

if __name__ == '__main__':
  app.run(host='192.168.3.107', debug=True)
