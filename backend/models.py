from app import db
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    receipts = db.relationship('Receipt', backref='user', lazy=True)


class Receipt(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    items = db.relationship('Item', backref='receipt', lazy=True)



class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    receipt_id = db.Column(db.Integer, db.ForeignKey('receipt.id'), nullable=False)

    category = db.Column(db.String)
