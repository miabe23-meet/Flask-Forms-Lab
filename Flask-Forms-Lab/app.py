from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "mia"
password = "123"


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
	return render_template('home.html', facebook_friends=['gefen ', 'lia'])


@app.route('/friend_exists/<string:friend>',methods=['GET','POST'])
def friend_exists(friend):
	return render_template('friend_exists.html', f=friend)




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)