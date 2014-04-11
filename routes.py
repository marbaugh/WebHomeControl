from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__) 
app.config.from_pyfile('hello.cfg')
db = SQLAlchemy(app)

class Status(db.model):
	id = db.Column(db.Integer, primary_key = True)
	time=db.Column(db.DateTime, index = True, unique = False)
    status=db.Column(db.String, index = True, unique = False)

class DoorStatus(Status):
    pass

class MotionStatus(Status):
    pass

class MotorStatus(Status):
    duration = db.Column(db.Integer, index = False, unique = False)


@app.route('/')
def home():
  return render_template('home.html')
 
if __name__ == '__main__':
  app.run(host='192.168.3.107', debug=True)
