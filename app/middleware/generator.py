from strgen import StringGenerator

def generator():
    key = StringGenerator('[a-zA-Z\d]{32}').render()
    return key