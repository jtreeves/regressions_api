from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configurations import Configurations
import os

# def create_app():
app = Flask(__name__)
app.config.from_object(Configurations)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# return app

if __name__ == '__main__':
    app.run(debug=True)

from app import routes, models