# $ export FLASK_APP=hello.py           lets the terminal know to use flask app
# $ flask run OR python -m flask run    optional flag --host=0.0.0.0 to listen to other IPs
# $ export FLASK_ENV=development        code changes refreshed

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

# <variable_name> allows you to create dynamic URLs
@app.route('/login')
def login():
    return 'login'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John%20Doe'))

@app.route('/admin')
def admin():
    return 'Hello, admin!'

@app.route('/guest/<guest_name>')
def guest(guest_name):
    return 'Hello, {} as Guest'.format(guest_name)

@app.route('/user/<username>')
def user(username):
    if username == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest_name = username))