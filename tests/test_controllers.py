from app.controllers.main.get_home import get_home
from app.controllers.main.get_about import get_about
from app.controllers.main.get_usage import get_usage
from app.controllers.main.get_math import get_math
from app.controllers.main_controller import main_controller
from app.controllers.images.create_linear_graph import create_linear_graph
from app.controllers.images.create_quadratic_graph import create_quadratic_graph
from app.controllers.images.create_cubic_graph import create_cubic_graph
from app.controllers.images.create_hyperbolic_graph import create_hyperbolic_graph
from app.controllers.images.create_exponential_graph import create_exponential_graph
from app.controllers.images.create_logarithmic_graph import create_logarithmic_graph
from app.controllers.images.create_logistic_graph import create_logistic_graph
from app.controllers.images.create_sinusoidal_graph import create_sinusoidal_graph
from app.controllers.images.create_root_graph import create_root_graph
from app.controllers.images.create_maximum_graph import create_maximum_graph
from app.controllers.images.create_minimum_graph import create_minimum_graph
from app.controllers.images.create_inflection_graph import create_inflection_graph
from app.controllers.images_controller import images_controller
from app.controllers.users.get_signup import get_signup
from app.controllers.users.post_signup import post_signup
from app.controllers.users_controller import users_controller
from app.controllers.regressions.post_regression import post_regression
from app.controllers.regressions.get_regression import get_regression
from app.controllers.regressions.put_regression import put_regression
from app.controllers.regressions.delete_regression import delete_regression
from app.controllers.regressions_controller import regressions_controller

class TestHomeController:
    def test_home_controller_success(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                practice = get_home()
                assert 'gives you an easy way to determine multiple regression models from a single data set' in practice[0]
                assert '<!DOCTYPE html>' in practice[0]
                assert practice[1] == 200

class TestAboutController:
    pass

class TestUsageController:
    pass

class TestMathController:
    pass

class TestMainController:
    pass

class TestLinearGraphController:
    pass

class TestQuadraticGraphController:
    pass

class TestCubicGraphController:
    pass

class TestHyperbolicGraphController:
    pass

class TestExponentialGraphController:
    pass

class TestLogarithmicGraphController:
    pass

class TestLogisticGraphController:
    pass

class TestSinusoidalGraphController:
    pass

class TestRootGraphController:
    pass

class TestMaximumGraphController:
    pass

class TestMinimumGraphController:
    pass

class TestInflectionGraphController:
    pass

class TestImagesController:
    pass

class TestGetSignupController:
    pass

class TestPostSignupController:
    pass

class TestUsersController:
    pass

class TestPostRegressionsController:
    pass

class TestGetRegressionsController:
    pass

class TestPutRegressionsController:
    pass

class TestDeleteRegressionsController:
    pass

class TestRegressionsController:
    pass