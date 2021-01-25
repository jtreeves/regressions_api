from flask import Flask
from configurations import Configurations

app = Flask(__name__)
app.config.from_object(Configurations)

from app import routes