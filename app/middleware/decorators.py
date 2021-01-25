from functools import wraps
from flask import request, abort
from .searching import searching

def require_apikey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        sent_key = request.args.get('key')
        print(f'SENT_KEY: {sent_key}')
        if sent_key is not None:
            found_key = searching(sent_key)
            print(f'FOUND_KEY: {found_key}')
            if found_key:
                return view_function(*args, **kwargs)
            else:
                abort(401)
        else:
            abort(401)
    return decorated_function