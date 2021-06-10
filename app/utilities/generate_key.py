from strgen import StringGenerator

def generate_key():
    key = StringGenerator('[a-zA-Z0-9\d]{32}').render()
    return key