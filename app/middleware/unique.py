from .generator import generator
from .available import available

def unique():
    test_key = generator()
    key_available = available(test_key)
    if key_available:
        return test_key
    else:
        return unique()