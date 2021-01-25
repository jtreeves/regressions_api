from functools import wraps
from flask import request, abort
from .hashing import hashing
from .searching import searching

def require_apikey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        sent_key = request.args.get('key')
        print(f'SENT_KEY: {sent_key}')
        hash_key = hashing(sent_key)
        print(f'HASH_KEY: {hash_key}')
        found_key = searching(hash_key)
        print(f'FOUND_KEY: {found_key}')
        if found_key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function