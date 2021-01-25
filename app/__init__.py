from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configurations import Configurations
import os

app = Flask(__name__)
app.config.from_object(Configurations)
db = SQLAlchemy(app)

from app import routes