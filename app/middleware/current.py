from flask import request
from app.models import User

def current(*args):
    sent_key = request.args.get('key')
    print(f'SENT_KEY: {sent_key}')
    found_user = User.query.filter_by(key=sent_key).first()
    print(f'FOUND_USER: {found_user}')
    dict_user = {
        'id': found_user.id,
        'name': found_user.name,
        'email': found_user.email,
        'key': found_user.key,
        'date': found_user.date
    }
    return dict_user