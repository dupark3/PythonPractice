import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from blogit.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth/')

@bp.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Must enter a username'
        elif not password:
            error = 'Must enter a password'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'Username {} already exists.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)', 
                (username, generate_password_hash(password))
            )
            db.commit() # saves the database since we made an insertion
            return redirect(url_for('auth.login'))
        else:
            flash(error)

    # render register.html if it's a GET method OR 
    # if there was an error and user was not redirected to the login url
    return render_template('auth/register.html')

@bp.route('/login', methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone()

        if username is None:
            error = 'Must enter a username'
        elif password is None:
            error = 'Must enter a password'
        elif user is None:
            error = 'Invalid username'
        elif not check_password_hash(user['password'], password):
            error = 'Invalid password'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get.db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)
    return wrapped_view