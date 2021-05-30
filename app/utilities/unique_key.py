from app.services.users.read_user import read_user
from .generate_key import generate_key

def unique_key():
    key = generate_key()
    found_user = read_user(key)

    if found_user is False:
        return key
    
    else:
        return unique_key()