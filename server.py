from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "SecretAdmirer"
import re

@app.route('/')
def index ():
	return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	confirm_pw = request.form['confirm_pw']

	name_check = re.compile(r'^[0-9]+$')
	email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

	errors = 0

	if len(first_name) < 1:
		flash('First Name is a required field')
		errors += 1
	elif name_check.match(first_name):
		flash('First Name cannot contain numbers')
		errors += 1
	else:
		pass
	if len(last_name) < 1:
		flash('Last Name is a required field')
		errors += 1
	elif name_check.match(last_name):
		errors += 1
		flash('Last Name cannot contain numbers')
	else:
		pass
	if len(email) < 1:
		flash('Email is a required field')
		errors += 1
	elif not email_check.match(email):
		flash("Please enter a valid email address")
		errors += 1
	if len(password) < 1:
		flash('Password is a required field')
		errors += 1
	elif password != confirm_pw:
		flash('Password not confirmed, please try again. ')
		errors += 1

	if errors == 0:
		flash('Thank you for submitting your information.')

	return redirect('/')

app.run(debug=True)
