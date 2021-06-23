from .main.get_home import get_home
from .main.get_about import get_about
from .main.get_usage import get_usage
from .main.get_math import get_math

# Create dictionary to store references relevant functions
main_controller = {
    'get_home': get_home,
    'get_about': get_about,
    'get_usage': get_usage,
    'get_math': get_math
}