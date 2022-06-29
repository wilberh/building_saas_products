from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@127.0.0.1:5432/flaskapp1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# OPTIONAL: handles SQLAlchemy database migrations for Flask applications
# https://pypi.org/project/Flask-Migrate/
# migrate = Migrate(app, db)
migrate = Migrate(app, db, directory="src/migrations")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
