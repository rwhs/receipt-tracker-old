from flask import Blueprint, request, jsonify
from app import db
from models import User

users = Blueprint('users', __name__)


@users.route('/api/users', methods=['POST'])
def register():
    user = request.get_json()

    new_user = User(email=user['email'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'response': 'testing'})