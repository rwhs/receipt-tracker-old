from app import db
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    receipts = db.relationship('Receipt', backref='user', lazy=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.email


class Receipt(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('Item', backref='receipt', lazy=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    receipt_id = db.Column(db.Integer, db.ForeignKey('receipt.id'), nullable=False)