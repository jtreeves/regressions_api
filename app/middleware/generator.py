import random
import string
from strgen import StringGenerator

testing = StringGenerator('[a-zA-Z\d]{50}').render()
print(testing)