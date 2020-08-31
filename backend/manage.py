from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


#py manage.py db init
#py manage.py db migrate
#py manage.py db upgrade

if __name__ == '__main__':
    manager.run()