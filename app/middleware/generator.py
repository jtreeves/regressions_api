import random
import string

def generator(length):
    characters = string.ascii_letters + string.digits
    result = ''.join(random.choice(characters) for i in range(length))