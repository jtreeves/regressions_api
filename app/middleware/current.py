from flask import request
from json import dumps
from app.models import User

current = 'John'

def current(*args):
    sent_key = request.args.get('key')
    print(f'SENT_KEY: {sent_key}')
    found_user = User.query.filter_by(key=sent_key).first()
    print(f'FOUND_USER: {found_user}')
    json_user = dumps(found_user)
    print(f'JSON_USER: {json_user}')
    return json_user