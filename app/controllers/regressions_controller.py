from .regressions.get_regression import get_regression
from .regressions.post_regression import post_regression
from .regressions.put_regression import put_regression
from .regressions.delete_regression import delete_regression

# Create dictionary to store references relevant functions
regressions_controller = {
    'get_regression': get_regression,
    'post_regression': post_regression,
    'put_regression': put_regression,
    'delete_regression': delete_regression
}