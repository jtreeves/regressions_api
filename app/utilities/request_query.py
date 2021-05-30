from flask import request
from app.services.users.read_user import read_user

def request_query():
    key = request.args.get('key')
    source = request.args.get('source')
    user_id = read_user(key)['id']

    query_data = {
        'user_id': user_id,
        'source': source
    }

    return query_data