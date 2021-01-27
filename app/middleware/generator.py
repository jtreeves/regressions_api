from strgen import StringGenerator

def generator():
    return StringGenerator('[a-zA-Z\d]{32}').render()