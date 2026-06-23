from extensions import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.String(), primary_key=True, default =str(uuid4()))
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.Text())

    