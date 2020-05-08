from flask import Flask,render_template,request, url_for ,redirect
from flask_mail import Mail
from kk import maill


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/register')
def register():

	maill(['___@gmail.com','___@gmail.com','___@gmail.com'],"<location>")
	return "Doneeeee"
