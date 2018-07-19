# contain the application factory to hold the Flask instance
# tells python that blogit should be treated as a package

import os

from flask import Flask

def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY ='dev',
        DATABASE=os.path.join(app.instance_path, 'blogit.sqlite')
    )

    if test_config is None:
        # load the instance config when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try: 
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return "Hello!"

    # init_app is a function that takes the app as a parameter
    # then calls close_db() and adds init_db_command() as a command that can be
    # called as part of flask. 
    from . import db
    db.init_app(app)

    return app
