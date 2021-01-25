from flask import request
from app.models import User

current = 'John'

def current(*args):
    sent_key = request.args.get('key')
    found_user = User.query.filter_by(key=sent_key).first()
    return found_user