from flask import Flask, render_template
 
app = Flask(__name__)     
 
@app.route('/')
def home():
  return render_template('home.html')
 
if __name__ == '__main__':
  app.run(host='192.168.3.107', debug=True)
