import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# This file contains the application factory, and tells Python the "saas" directory is a package

# This is the application factory function - that creates and configure the app
def create_app(test_config=None):
    # creates the Flask instance
    app = Flask(__name__, instance_relative_config=True)
    # default/test config
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='postgresql://postgres:password@127.0.0.1:5432/flaskapp1',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # this overrides the default config
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # OPTIONAL: handles SQLAlchemy database migrations for Flask applications
    # https://pypi.org/project/Flask-Migrate/
    db = SQLAlchemy(app)
    # migrate = Migrate(app, db)
    migrate = Migrate(app, db, directory="src/migrations")

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello REAL World!'

    return app
