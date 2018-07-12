# $ export FLASK_APP=hello.py           lets the terminal know to use flask app
# $ flask run OR python -m flask run    optional flag --host=0.0.0.0 to listen to other IPs
# $ export FLASK_ENV=development        code changes refreshed

from flask import Flask
app = Flask(__name__)

@app.route('/')
def greet():
    name = 'Du'
    return 'Hello, ' + name + '!'

# <variable_name> allows you to create dynamic URLs
@app.route('/user/<username>')
def show_profile(username):
    return 'User name: %s' %username

# <converter:variable_name> with no spaces allows you to convert from string type
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Viewing post #%d' %post_id

