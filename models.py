from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InterviewRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    domain = db.Column(db.String(100), nullable=False)
    time   = db.Column(db.String(100), nullable=False, default='10:00 AM - 11:00 AM')
    language = db.Column(db.String(50), nullable=False, default='English')


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    msg = db.Column(db.String(200), nullable=False)