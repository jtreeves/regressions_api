from .generator import generator
from app.models import User
from werkzeug.security import generate_password_hash as hash_key

def available(string):
    hash_string = hash_key(string)
    search_hash = User.query.filter_by(key=hash_string).first()
    if search_hash is not None:
        return False
    else:
        return True