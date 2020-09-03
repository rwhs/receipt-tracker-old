from flask import Blueprint, request, jsonify
from app import db
from models import User
import re

users = Blueprint('users', __name__)


@users.route('/api/register', methods=['POST'])
def register():
    user = request.get_json()
    email = user['email']
    password = user['password']

    new_user = User(email=email, password=password)

    # Validate email format
    if re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == None:
        return jsonify({'response': 'Email is not valid!'})

    # Catch duplicate registered emails
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'response': 'Email is already registered!'})

    return jsonify({'response': f'Successfully registered {email}'})


# Testing login route
@users.route('/api/login', methods=['POST'])
def login_test():
    user = request.get_json()

    stored_user = User.query.filter_by(email=user['email']).first()

    if stored_user is not None:
        if stored_user.verify_password(user['password']):
            return jsonify({'response': 'Authenticated'})
        else:
            return jsonify({'response': 'Invalid credentials!'})
    else:
        return jsonify({'response': 'User does not exist'})