from strgen import StringGenerator

def generate_key():
    """ Use tool to create random string of characters """
    key = StringGenerator('[a-zA-Z0-9\d]{32}').render()
    return key