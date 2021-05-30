from functools import wraps
from flask import request, abort, make_response
from app.services.users.read_user import read_user

def require_key(view_function):
    @wraps(view_function)

    def decorated_function(*args, **kwargs):
        sent_key = request.args.get('key')
        
        if sent_key:
            found_user = read_user(sent_key)
            
            if found_user:
                return view_function(*args, **kwargs)
            
            else:
                abort(make_response('Key not found', 404))
        
        else:
            abort(make_response('Key must be sent', 403))
    
    return decorated_function