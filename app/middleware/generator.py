from strgen import StringGenerator

def generator():
    return StringGenerator('[a-zA-Z\d]{50}').render()