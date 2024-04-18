from flask_login import UserMixin

from app import db


# Create a table in the database

class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    description = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User: {self.username}, Role {self.role}>'
    
    def get_id(self):
        return self.uid
    