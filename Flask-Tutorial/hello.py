# $ export FLASK_APP=hello.py           lets the terminal know to use flask app
# $ flask run OR python -m flask run    optional flag --host=0.0.0.0 to listen to other IPs
# $ export FLASK_ENV=development        code changes refreshed

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

# <variable_name> allows you to create dynamic URLs
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user=request.form['name']
        age=request.form['age']
        return redirect(url_for('user', username=user, age=age))
    else :
        return render_template('login.html')

@app.route('/admin')
def admin():
    return 'Hello, admin!'

@app.route('/guest/<guest_name>/<int:age>')
def guest(guest_name, age):
    return render_template('guest.html', jinjaname=guest_name, jinjaage=age)

@app.route('/user/<username>/<int:age>')
def user(username, age):
    if username == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest_name=username, age=age))

@app.route('/result')
def result():
    dict = {'phys':60, 'chem':70, "math":90}
    sum = 0.0
    for key, val in dict.items():
        sum += val
    dict['avg'] = sum/len(dict)
    return render_template('result.html', jinjadict=dict)