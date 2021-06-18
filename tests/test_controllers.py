# from flask import request
# from werkzeug import ImmutableMultiDict
from datetime import datetime
from app import db
from app.models import User, Regression
from app.forms import SignUpForm
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
    def test_home_controller_renders_html(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                home = get_home()
                assert '<!DOCTYPE html>' in home[0]
    
    def test_home_controller_displays_template(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                home = get_home()
                assert 'gives you an easy way to determine multiple regression models from a single data set' in home[0]
    
    def test_home_controller_returns_status(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                home = get_home()
                assert home[1] == 200

class TestAboutController:
    def test_about_controller_renders_html(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                about = get_about()
                assert '<!DOCTYPE html>' in about[0]
    
    def test_about_controller_displays_template(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                about = get_about()
                assert 'Using our API, you can finally answer various important questions' in about[0]
    
    def test_about_controller_returns_status(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                about = get_about()
                assert about[1] == 200

class TestUsageController:
    def test_usage_controller_renders_html(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                usage = get_usage()
                assert '<!DOCTYPE html>' in usage[0]
    
    def test_usage_controller_displays_template(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                usage = get_usage()
                assert 'guide for how to use the API' in usage[0]
    
    def test_usage_controller_returns_status(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                usage = get_usage()
                assert usage[1] == 200

class TestMathController:
    def test_math_controller_renders_html(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                math = get_math()
                assert '<!DOCTYPE html>' in math[0]
    
    def test_math_controller_displays_template(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                math = get_math()
                assert 'some explanations of mathematical concepts relevant to the output from the API' in math[0]
    
    def test_math_controller_returns_status(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                math = get_math()
                assert math[1] == 200

class TestMainController:
    def test_main_controller_loads_home(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                home = main_controller['get_home']()
                assert '<!DOCTYPE html>' in home[0]
                assert 'gives you an easy way to determine multiple regression models from a single data set' in home[0]
                assert home[1] == 200
    
    def test_main_controller_loads_about(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                about = main_controller['get_about']()
                assert '<!DOCTYPE html>' in about[0]
                assert 'Using our API, you can finally answer various important questions' in about[0]
                assert about[1] == 200
    
    def test_main_controller_loads_usage(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                usage = main_controller['get_usage']()
                assert '<!DOCTYPE html>' in usage[0]
                assert 'guide for how to use the API' in usage[0]
                assert usage[1] == 200
    
    def test_main_controller_loads_math(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                math = main_controller['get_math']()
                assert '<!DOCTYPE html>' in math[0]
                assert 'some explanations of mathematical concepts relevant to the output from the API' in math[0]
                assert math[1] == 200

class TestLinearGraphController:
    def test_creates_linear_graph_visible(self):
        graph = create_linear_graph()
        assert graph._visible
    
    def test_creates_linear_graph_tight(self):
        graph = create_linear_graph()
        assert graph._tight
    
    def test_creates_linear_graph_dimensions(self):
        graph = create_linear_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestQuadraticGraphController:
    def test_creates_quadratic_graph_visible(self):
        graph = create_quadratic_graph()
        assert graph._visible
    
    def test_creates_quadratic_graph_tight(self):
        graph = create_quadratic_graph()
        assert graph._tight
    
    def test_creates_quadratic_graph_dimensions(self):
        graph = create_quadratic_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestCubicGraphController:
    def test_creates_cubic_graph_visible(self):
        graph = create_cubic_graph()
        assert graph._visible
    
    def test_creates_cubic_graph_tight(self):
        graph = create_cubic_graph()
        assert graph._tight
    
    def test_creates_cubic_graph_dimensions(self):
        graph = create_cubic_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestHyperbolicGraphController:
    def test_creates_hyperbolic_graph_visible(self):
        graph = create_hyperbolic_graph()
        assert graph._visible
    
    def test_creates_hyperbolic_graph_tight(self):
        graph = create_hyperbolic_graph()
        assert graph._tight
    
    def test_creates_hyperbolic_graph_dimensions(self):
        graph = create_hyperbolic_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestExponentialGraphController:
    def test_creates_exponential_graph_visible(self):
        graph = create_exponential_graph()
        assert graph._visible
    
    def test_creates_exponential_graph_tight(self):
        graph = create_exponential_graph()
        assert graph._tight
    
    def test_creates_exponential_graph_dimensions(self):
        graph = create_exponential_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestLogarithmicGraphController:
    def test_creates_logarithmic_graph_visible(self):
        graph = create_logarithmic_graph()
        assert graph._visible
    
    def test_creates_logarithmic_graph_tight(self):
        graph = create_logarithmic_graph()
        assert graph._tight
    
    def test_creates_logarithmic_graph_dimensions(self):
        graph = create_logarithmic_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestLogisticGraphController:
    def test_creates_logistic_graph_visible(self):
        graph = create_logistic_graph()
        assert graph._visible
    
    def test_creates_logistic_graph_tight(self):
        graph = create_logistic_graph()
        assert graph._tight
    
    def test_creates_logistic_graph_dimensions(self):
        graph = create_logistic_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestSinusoidalGraphController:
    def test_creates_sinusoidal_graph_visible(self):
        graph = create_sinusoidal_graph()
        assert graph._visible
    
    def test_creates_sinusoidal_graph_tight(self):
        graph = create_sinusoidal_graph()
        assert graph._tight
    
    def test_creates_sinusoidal_graph_dimensions(self):
        graph = create_sinusoidal_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestRootGraphController:
    def test_creates_root_graph_visible(self):
        graph = create_root_graph()
        assert graph._visible
    
    def test_creates_root_graph_tight(self):
        graph = create_root_graph()
        assert graph._tight
    
    def test_creates_root_graph_dimensions(self):
        graph = create_root_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestMaximumGraphController:
    def test_creates_maximum_graph_visible(self):
        graph = create_maximum_graph()
        assert graph._visible
    
    def test_creates_maximum_graph_tight(self):
        graph = create_maximum_graph()
        assert graph._tight
    
    def test_creates_maximum_graph_dimensions(self):
        graph = create_maximum_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestMinimumGraphController:
    def test_creates_minimum_graph_visible(self):
        graph = create_minimum_graph()
        assert graph._visible
    
    def test_creates_minimum_graph_tight(self):
        graph = create_minimum_graph()
        assert graph._tight
    
    def test_creates_minimum_graph_dimensions(self):
        graph = create_minimum_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestInflectionGraphController:
    def test_creates_inflection_graph_visible(self):
        graph = create_inflection_graph()
        assert graph._visible
    
    def test_creates_inflection_graph_tight(self):
        graph = create_inflection_graph()
        assert graph._tight
    
    def test_creates_inflection_graph_dimensions(self):
        graph = create_inflection_graph()
        assert graph.get_figheight() == 5.0
        assert graph.get_figwidth() == 5.0

class TestImagesController:
    def test_images_controller_linear(self):
        graph = images_controller('linear.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_quadratic(self):
        graph = images_controller('quadratic.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_cubic(self):
        graph = images_controller('cubic.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_hyperbolic(self):
        graph = images_controller('hyperbolic.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_exponential(self):
        graph = images_controller('exponential.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_logarithmic(self):
        graph = images_controller('logarithmic.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_logistic(self):
        graph = images_controller('logistic.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_sinusoidal(self):
        graph = images_controller('sinusoidal.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_root(self):
        graph = images_controller('root.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_maximum(self):
        graph = images_controller('maximum.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_minimum(self):
        graph = images_controller('minimum.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200
    
    def test_images_controller_inflection(self):
        graph = images_controller('inflection.png')
        assert b'Matplotlib' in graph.data
        assert graph.content_type == 'image/png'
        assert graph.status_code == 200

class TestGetSignupController:
    def test_get_signup_renders_form(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                new_form = SignUpForm(
                    key = 'ABC123'
                )
                signup = get_signup(new_form)
                signup_html = signup[0]
                assert '<form action=\'\' method=\'post\'>' in signup_html
    
    def test_get_signup_renders_empty_fields(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                new_form = SignUpForm(
                    key = 'ABC123'
                )
                signup = get_signup(new_form)
                signup_html = signup[0]
                assert '<input id="name" name="name" required type="text" value="">' in signup_html
                assert '<input id="email" name="email" required type="text" value="">' in signup_html
    
    def test_get_signup_contains_hidden_key(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                new_form = SignUpForm(
                    key = 'ABC123'
                )
                signup = get_signup(new_form)
                signup_html = signup[0]
                assert '<input id="key" name="key" required type="hidden" value="ABC123">' in signup_html
    
    def test_get_signup_contains_submit(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                new_form = SignUpForm(
                    key = 'ABC123'
                )
                signup = get_signup(new_form)
                signup_html = signup[0]
                assert '<input id="submit" name="submit" type="submit" value="Submit">' in signup_html
    
    def test_get_signup_status_success(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                new_form = SignUpForm(
                    key = 'ABC123'
                )
                signup = get_signup(new_form)
                assert signup[1] == 200

class TestPostSignupController:
    def test_post_signup_renders_page(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                app.config['WTF_CSRF_ENABLED'] = False
                filled_form = SignUpForm(
                    name = 'Test Post Signup Renders Page',
                    email = 'test_post_signup_renders_page@email.com',
                    key = 'ABC123'
                )

                def overwrite_validate():
                    return True

                filled_form.validate_on_submit = overwrite_validate
                signup = post_signup(filled_form)
                assert 'ABC123' in signup[0]
                assert '<form action=\'\' method=\'post\'>' not in signup[0]
                assert signup[1] == 201

                found_user = User.query.filter_by(
                    email = 'test_post_signup_renders_page@email.com'
                ).first()

                db.session.delete(found_user)
                db.session.commit()
    
    # def test_signup_loads_error_post_old(self, client):
    #     new_user = User(
    #         name = 'test fail signup route',
    #         email = 'test_fail_signup_route@email.com',
    #         key = 'ABC123',
    #         date = datetime.now()
    #     )

    #     db.session.add(new_user)
    #     db.session.commit()

    #     res = client.post(
    #         '/signup',
    #         data = {
    #             'name': 'test fail signup route',
    #             'email': 'test_fail_signup_route@email.com',
    #             'key': 'ABC123'
    #         }
    #     )

    #     assert res.status_code == 409
    #     assert b'<h1>Error</h1>' in res.data
    #     assert b'Email already in use' in res.data

    #     found_user = User.query.filter_by(
    #         email = 'test_fail_signup_route@email.com'
    #     ).first()

    #     db.session.delete(found_user)
    #     db.session.commit()
    
    # def test_signup_fails_put(self, client):
    #     res = client.put('/signup')
    #     assert res.status_code == 405
    
    # def test_signup_fails_delete(self, client):
    #     res = client.delete('/signup')
    #     assert res.status_code == 405

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