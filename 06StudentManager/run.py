import pymysql
pymysql.install_as_MySQLdb()
from app import app
from app import db


from app.models import Teacher
from app.models import Score
from app.models import Student
from app.models import Course

from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell
from flask_script import Manager

manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command("db",MigrateCommand)

manager.run()
