from werkzeug.security import generate_password_hash as hash_key

def hashing(string):
    return hash_key(string)