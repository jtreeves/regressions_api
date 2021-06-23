from functools import wraps
from flask import request, abort, make_response
from app.services.users.read_user import read_user

def require_key(protected_function):
    """ Ensure request included a valid key in order to use a private function """

    # Wrap the private function
    @wraps(protected_function)

    def decorated_function(*args, **kwargs):
        """ Establish checkpoints to pass before executing private function """

        # Grab key from URL arguments
        sent_key = request.args.get('key')
        
        # Proceed if key included in URL arguments
        if sent_key:
            # Use helper function to find user with provided key in database
            found_user = read_user(sent_key)
            
            # Execute private function if user exists
            if found_user:
                return protected_function(*args, **kwargs)
            
            # Return error code if no user in database with provided key
            else:
                abort(make_response('User not authenticated', 401))
        
        # Return error code if key not included in URL arguments
        else:
            abort(make_response('Key must be provided', 403))
    
    # Return either execution of private function or error code
    return decorated_function