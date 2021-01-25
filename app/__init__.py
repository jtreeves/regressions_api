from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configurations import Configurations
import os

app = Flask(__name__)
app.config.from_object(Configurations)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models