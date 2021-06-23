from flask import request
from app.services.users.read_user import read_user

def request_query():
    """ Store parameters of query from request URL """

    # Grab arguments from URL
    key = request.args.get('key')
    source = request.args.get('source')
    user_id = read_user(key)['id']

    # Store data in dictionary
    query_data = {
        'user_id': user_id,
        'source': source
    }

    # Return dictionary
    return query_data