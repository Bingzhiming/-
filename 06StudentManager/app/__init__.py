from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from  flask_mail import Mail,Message

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
mail = Mail(app)

from . import views