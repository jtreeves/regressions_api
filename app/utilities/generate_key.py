from strgen import StringGenerator

def generate_key():
    key = StringGenerator('[a-zA-Z\d]{32}').render()
    return key