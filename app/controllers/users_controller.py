from .users.get_signup import get_signup
from .users.post_signup import post_signup

# Create dictionary to store references relevant functions
users_controller = {
    'get_signup': get_signup,
    'post_signup': post_signup
}