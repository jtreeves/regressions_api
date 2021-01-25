from flask import request, jsonify
from json import dumps
from app.models import User

current = 'John'

def current(*args):
    sent_key = request.args.get('key')
    print(f'SENT_KEY: {sent_key}')
    found_user = User.query.filter_by(key=sent_key).first()
    print(f'FOUND_USER: {found_user}')
    dict_user = {
        'name': found_user.name,
        'email': found_user.email,
    }
    # json_user = dumps(found_user.serialize())
    # print(f'JSON_USER: {json_user}')
    return dict_user