# Import DB object and models
from .src.app import db
from .src.models.user import User

# Drop all tables
db.drop_all()

# Recreate all tables
db.create_all()

# Add dummy users
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

