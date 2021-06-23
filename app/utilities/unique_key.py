from app.services.users.read_user import read_user
from .generate_key import generate_key

def unique_key():
    """ Ensure new key not already in use in database """

    # Use helper function to create initial key
    key = generate_key()

    # Use helper function to find any user in database with newly created key
    found_user = read_user(key)

    # Return key if no user currently has it
    if found_user is False:
        return key
    
    # Recursively call function again if key already in use by another user
    else:
        return unique_key()