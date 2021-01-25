from .generator import generator
from app.models import User
from werkzeug.security import generate_password_hash

def available(string):
    hash_string = generate_password_hash(string)
    search_hash = User.query.filter_by(key=hash_string).first()
    if search_hash is not None:
        string = generator()
    else:
        return True