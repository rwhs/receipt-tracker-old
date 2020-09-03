from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import POSTGRES_URL, POSTGRES_DATABASE, POSTGRES_USERNAME, POSTGRES_PASSWORD

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_URL}/{POSTGRES_DATABASE}'
db = SQLAlchemy(app)

from api.users import users

app.register_blueprint(users)


@app.route('/')
def hello_world():
    return 'Hello world'
