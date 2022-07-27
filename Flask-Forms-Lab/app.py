from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "mia"
password = "123"
facebook_friends=['gefen', 'lia', 'maya ']

@app.route('/', methods=['GET','POST'])  
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		username=request.form['username']
		password=request.form['password']
		return redirect(url_for('home',u=username, p=password))


@app.route('/home')
def home():
	return render_template('home.html', facebook_friends= facebook_friends)


@app.route('/friend_exists/<string:friend>',methods=['GET','POST'])
def friend_exists(friend):
	if friend in facebook_friends:
		return render_template('friend_exists.html', f=friend, person='True')
	else:
		return render_template('friend_exists.html', f=friend, person='False')





if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)