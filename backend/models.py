from app import db, bcrypt
from datetime import datetime


class User(db.Model):

    # User authentication
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120))

    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    receipts = db.relationship('Receipt', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('Passwords cannot be accessed!')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)



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
