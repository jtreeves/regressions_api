from .generator import generator
from app.models import User

def available(string):
    found_user = User.query.filter_by(key=string).first()
    if found_user is not None:
        return False
    else:
        return True