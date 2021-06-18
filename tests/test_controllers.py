import json
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
    def test_post_signup_new_renders_key(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                app.config['WTF_CSRF_ENABLED'] = False
                new_form = SignUpForm(
                    name = 'Test Post Signup New Renders Key',
                    email = 'test_post_signup_new_renders_key@email.com',
                    key = 'ABC123'
                )

                def overwrite_validate():
                    found_user = User.query.filter_by(
                        email = new_form.email.data
                    ).first()
                    if not found_user:
                        return True
                    else:
                        return False

                new_form.validate_on_submit = overwrite_validate
                signup = post_signup(new_form)
                assert 'ABC123' in signup[0]
                assert '<form action=\'\' method=\'post\'>' not in signup[0]
                assert signup[1] == 201

                found_user = User.query.filter_by(
                    email = 'test_post_signup_new_renders_key@email.com'
                ).first()

                db.session.delete(found_user)
                db.session.commit()
    
    def test_post_signup_old_renders_error(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                app.config['WTF_CSRF_ENABLED'] = False
                old_user = User(
                    name = 'Test Post Signup Old Renders Error',
                    email = 'test_post_signup_old_renders_error@email.com',
                    key = 'ABC123',
                    date = datetime.now()
                )

                db.session.add(old_user)
                db.session.commit()

                old_form = SignUpForm(
                    name = 'Test Post Signup Old Renders Error',
                    email = 'test_post_signup_old_renders_error@email.com',
                    key = 'ABC123'
                )

                def overwrite_validate():
                    found_user = User.query.filter_by(
                        email = old_form.email.data
                    ).first()
                    if not found_user:
                        return True
                    else:
                        return False

                old_form.validate_on_submit = overwrite_validate
                signup = post_signup(old_form)
                assert 'Email already in use' in signup[0]
                assert '<form action=\'\' method=\'post\'>' not in signup[0]
                assert signup[1] == 409

                found_user = User.query.filter_by(
                    email = 'test_post_signup_old_renders_error@email.com'
                ).first()

                db.session.delete(found_user)
                db.session.commit()
    
class TestUsersController:
    def test_users_controller_get(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                new_form = SignUpForm(
                    key = 'ABC123'
                )
                signup = users_controller['get_signup'](new_form)
                assert '<form action=\'\' method=\'post\'>' in signup[0]
                assert '<input id="key" name="key" required type="hidden" value="ABC123">' in signup[0]
                assert signup[1] == 200
    
    def test_users_controller_post(self, app):
        with app.app_context():
            with app.test_request_context('/'):
                app.config['WTF_CSRF_ENABLED'] = False
                new_form = SignUpForm(
                    name = 'Test Users Controller Post',
                    email = 'test_users_controller_post@email.com',
                    key = 'ABC123'
                )

                def overwrite_validate():
                    found_user = User.query.filter_by(
                        email = new_form.email.data
                    ).first()
                    if not found_user:
                        return True
                    else:
                        return False

                new_form.validate_on_submit = overwrite_validate
                signup = users_controller['post_signup'](new_form)
                assert 'ABC123' in signup[0]
                assert '<form action=\'\' method=\'post\'>' not in signup[0]
                assert signup[1] == 201

                found_user = User.query.filter_by(
                    email = 'test_users_controller_post@email.com'
                ).first()

                db.session.delete(found_user)
                db.session.commit()

class TestPostRegressionsController:
    def test_post_regression_new_adds(self, app, client):
        @app.route("/post_regression_new", methods=["POST"])
        def post_regression_new_route():
            post_regression_new = post_regression()
            return post_regression_new
        
        new_user = User(
            name = 'Test Post Regression New',
            email = 'test_post_regression_new@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_new@email.com'
        ).first()

        found_user_id = found_user.id

        title = 'Test Post Regression New Title'
        independent = 'Test Post Regression New Independent'
        dependent = 'Test Post Regression New Dependent'
        precision = 4
        data_set = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13, 14],
            [15, 16],
            [17, 18],
            [19, 20]
        ]

        res = client.post(
            "/post_regression_new?key=ABC123&source=TestPostRegressionNewSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        created_regression = json.loads(res.data.decode())
        found_regression = Regression.query.filter_by(
            user_id = found_user_id, 
            source = 'TestPostRegressionNewSource'
        ).first()

        assert created_regression['title'] == found_regression.title
        assert created_regression['best_fit'] == found_regression.best_fit
        assert res.status_code == 201

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_post_regression_old(self, app, client):
        @app.route("/post_regression_old", methods=["POST"])
        def post_regression_old_route():
            post_regression_old = post_regression()
            return post_regression_old
        
        new_user = User(
            name = 'Test Post Regression Fails Old',
            email = 'test_post_regression_fails_old@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_fails_old@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPostRegressionFailsOldSource',
            title = 'Test Post Regression Fails Old Title',
            independent = 'Test Post Regression Fails Old Independent',
            dependent = 'Test Post Regression Fails Old Dependent',
            precision = 4,
            data_set = [[1, 2], [3, 4], [5, 6]],
            linear_coefficients = [2, 3],
            linear_points = {'roots': [[1, 0]], 'inflections': [None]},
            linear_correlation = 0.5,
            quadratic_coefficients = [2, 3, 5],
            quadratic_points = {'roots': [[1, 0], [10, 0]], 'maxima': [[3, 57]]},
            quadratic_correlation = 0.5,
            cubic_coefficients = [2, 3, 5, 7],
            cubic_points = {'roots': [[1, 0], [5, 0], [10, 0]], 'maxima': [[3, 57]]},
            cubic_correlation = 0.5,
            hyperbolic_coefficients = [2, 3],
            hyperbolic_points = {'roots': [[1, 0]], 'maxima': [None]},
            hyperbolic_correlation = 0.5,
            exponential_coefficients = [2, 3],
            exponential_points = {'roots': [None], 'maxima': [None]},
            exponential_correlation = 0.5,
            logarithmic_coefficients = [2, 3],
            logarithmic_points = {'roots': [[1, 0]], 'maxima': [None]},
            logarithmic_correlation = 0.5,
            logistic_coefficients = [2, 3, 5],
            logistic_points = {'roots': [None], 'inflections': [[5, 7]]},
            logistic_correlation = 0.5,
            sinusoidal_coefficients = [2, 3, 5, 7],
            sinusoidal_points = {'roots': [[2, 0], [4, 0]], 'inflections': [[5, 7], [7, 7]]},
            sinusoidal_correlation = 0.5,
            best_fit = 'hyperbolic',
            date = datetime.now()
        )

        db.session.add(new_regression)
        db.session.commit()

        title = 'Test Post Regression Fails Old Title'
        independent = 'Test Post Regression Fails Old Independent'
        dependent = 'Test Post Regression Fails Old Dependent'
        precision = 4
        data_set = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13, 14],
            [15, 16],
            [17, 18],
            [19, 20]
        ]

        res = client.post(
            "/post_regression_old?key=ABC123&source=TestPostRegressionFailsOldSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        found_regression = Regression.query.filter_by(
            user_id = found_user_id, 
            source = 'TestPostRegressionFailsOldSource'
        ).first()

        assert res.data == b'Source already in use by other collection'
        assert res.status_code == 409

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_post_regression_without_source(self, app, client):
        @app.route("/post_regression_without_source", methods=["POST"])
        def post_regression_without_source_route():
            post_regression_without_source = post_regression()
            return post_regression_without_source

        new_user = User(
            name = 'Test Post Regression without Source Fails',
            email = 'test_post_regression_without_source_fails@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_without_source_fails@email.com'
        ).first()

        title = 'Test Post Regression Fails without Source Title'
        independent = 'Test Post Regression Fails without Source Independent'
        dependent = 'Test Post Regression Fails without Source Dependent'
        precision = 4
        data_set = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13, 14],
            [15, 16],
            [17, 18],
            [19, 20]
        ]

        res = client.post(
            "/post_regression_without_source?key=ABC123",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        assert res.data == b'Source must be provided'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()

    def test_fails_post_regression_decimal_precision(self, app, client):
        @app.route("/post_regression_decimal_precision", methods=["POST"])
        def post_regression_decimal_precision_route():
            post_regression_decimal_precision = post_regression()
            return post_regression_decimal_precision
        
        new_user = User(
            name = 'Test Post Regression Fails Decimal Precision',
            email = 'test_post_regression_fails_decimal_precision@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_fails_decimal_precision@email.com'
        ).first()

        title = 'Test Post Regression Fails Decimal Precision Title'
        independent = 'Test Post Regression Fails Decimal Precision Independent'
        dependent = 'Test Post Regression Fails Decimal Precision Dependent'
        precision = 4.5
        data_set = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13, 14],
            [15, 16],
            [17, 18],
            [19, 20]
        ]

        res = client.post(
            "/post_regression_decimal_precision?key=ABC123&source=TestPostRegressionFailsDecimalPrecisionSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        assert res.data == b'Precision must be a positive integer'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()

    def test_fails_post_regression_negative_precision(self, app, client):
        @app.route("/post_regression_negative_precision", methods=["POST"])
        def post_regression_negative_precision_route():
            post_regression_negative_precision = post_regression()
            return post_regression_negative_precision
        
        new_user = User(
            name = 'Test Post Regression Fails Negative Precision',
            email = 'test_post_regression_fails_negative_precision@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_fails_negative_precision@email.com'
        ).first()

        title = 'Test Post Regression Fails Negative Precision Title'
        independent = 'Test Post Regression Fails Negative Precision Independent'
        dependent = 'Test Post Regression Fails Negative Precision Dependent'
        precision = -4
        data_set = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13, 14],
            [15, 16],
            [17, 18],
            [19, 20]
        ]

        res = client.post(
            "/post_regression_negative_precision?key=ABC123&source=TestPostRegressionFailsNegativePrecisionSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        assert res.data == b'Precision must be a positive integer'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()

    def test_fails_post_regression_short_data_set(self, app, client):
        @app.route("/post_regression_short_data_set", methods=["POST"])
        def post_regression_short_data_set_route():
            post_regression_short_data_set = post_regression()
            return post_regression_short_data_set
        
        new_user = User(
            name = 'Test Post Regression Fails Short Data Set',
            email = 'test_post_regression_fails_short_data_set@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_fails_short_data_set@email.com'
        ).first()

        title = 'Test Post Regression Fails Short Data Set Title'
        independent = 'Test Post Regression Fails Short Data Set Independent'
        dependent = 'Test Post Regression Fails Short Data Set Dependent'
        precision = 4
        data_set = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]

        res = client.post(
            "/post_regression_short_data_set?key=ABC123&source=TestPostRegressionFailsShortDataSetSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        assert res.data == b'Data set must contain at least 10 points'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_post_regression_nonlist_data_set(self, app, client):
        @app.route("/post_regression_nonlist_data_set", methods=["POST"])
        def post_regression_nonlist_data_set_route():
            post_regression_nonlist_data_set = post_regression()
            return post_regression_nonlist_data_set
        
        new_user = User(
            name = 'Test Post Regression Fails Nonlist Data Set',
            email = 'test_post_regression_fails_nonlist_data_set@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_fails_nonlist_data_set@email.com'
        ).first()

        title = 'Test Post Regression Fails Nonlist Data Set Title'
        independent = 'Test Post Regression Fails Nonlist Data Set Independent'
        dependent = 'Test Post Regression Fails Nonlist Data Set Dependent'
        precision = 4
        data_set = {
            'first_point': [1, 2],
            'second_point': [3, 4],
            'third_point': [5, 6]
        }

        res = client.post(
            "/post_regression_nonlist_data_set?key=ABC123&source=TestPostRegressionFailsNonlistDataSetSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        assert res.data == b'Data set must be a list'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_post_regression_nonlist_points(self, app, client):
        @app.route("/post_regression_nonlist_points", methods=["POST"])
        def post_regression_nonlist_points_route():
            post_regression_nonlist_points = post_regression()
            return post_regression_nonlist_points
        
        new_user = User(
            name = 'Test Post Regression Fails Nonlist Points',
            email = 'test_post_regression_fails_nonlist_points@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_fails_nonlist_points@email.com'
        ).first()

        title = 'Test Post Regression Fails Nonlist Points Title'
        independent = 'Test Post Regression Fails Nonlist Points Independent'
        dependent = 'Test Post Regression Fails Nonlist Points Dependent'
        precision = 4
        data_set = [
            {'x': 1, 'y': 2},
            {'x': 3, 'y': 4},
            {'x': 5, 'y': 6}
        ]

        res = client.post(
            "/post_regression_nonlist_points?key=ABC123&source=TestPostRegressionFailsNonlistPointsSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        assert res.data == b'Each coordinate pair within data set must be a list'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_post_regression_long_points(self, app, client):
        @app.route("/post_regression_long_points", methods=["POST"])
        def post_regression_long_points_route():
            post_regression_long_points = post_regression()
            return post_regression_long_points
        
        new_user = User(
            name = 'Test Post Regression Fails Long Points',
            email = 'test_post_regression_fails_long_points@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_fails_long_points@email.com'
        ).first()

        title = 'Test Post Regression Fails Long Points Title'
        independent = 'Test Post Regression Fails Long Points Independent'
        dependent = 'Test Post Regression Fails Long Points Dependent'
        precision = 4
        data_set = [
            [1, 2, 3],
            [4, 5, 6]
        ]

        res = client.post(
            "/post_regression_long_points?key=ABC123&source=TestPostRegressionFailsLongPointsSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        assert res.data == b'Each coordinate pair within data set must contain exactly 2 numbers'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_post_regression_string_numbers(self, app, client):
        @app.route("/post_regression_string_numbers", methods=["POST"])
        def post_regression_string_numbers_route():
            post_regression_string_numbers = post_regression()
            return post_regression_string_numbers
        
        new_user = User(
            name = 'Test Post Regression Fails String Numbers',
            email = 'test_post_regression_fails_string_numbers@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_fails_string_numbers@email.com'
        ).first()

        title = 'Test Post Regression Fails String Numbers Title'
        independent = 'Test Post Regression Fails String Numbers Independent'
        dependent = 'Test Post Regression Fails String Numbers Dependent'
        precision = 4
        data_set = [
            [1, 2],
            ['3', 4],
            [5, 6]
        ]

        res = client.post(
            "/post_regression_string_numbers?key=ABC123&source=TestPostRegressionFailsStringNumbersSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        assert res.data == b'All numbers within coordinate pairs within data set must be integers or floats'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_post_regression_incomplete_submission(self, app, client):
        @app.route("/post_regression_incomplete_submission", methods=["POST"])
        def post_regression_incomplete_submission_route():
            post_regression_incomplete_submission = post_regression()
            return post_regression_incomplete_submission
        
        new_user = User(
            name = 'Test Post Regression Fails Incomplete Submission',
            email = 'test_post_regression_fails_incomplete_submission@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_post_regression_fails_incomplete_submission@email.com'
        ).first()

        title = 'Test Post Regression Fails Incomplete Submission Title'
        independent = 'Test Post Regression Fails Incomplete Submission Independent'
        dependent = 'Test Post Regression Fails Incomplete Submission Dependent'
        precision = ''
        data_set = ''

        res = client.post(
            "/post_regression_incomplete_submission?key=ABC123&source=TestPostRegressionFailsIncompleteSubmissionSource",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        assert res.data == b'Title, independent, dependent, data set, and precision fields must all be provided'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()

class TestGetRegressionsController:
    def test_get_regression_accesses(self, app, client):
        @app.route("/get_regression_accesses", methods=["GET"])
        def get_regression_accesses_route():
            get_regression_accesses = get_regression()
            return get_regression_accesses
        
        new_user = User(
            name = 'Test Get Regression Accesses',
            email = 'test_get_regression_accesses@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_get_regression_accesses@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestGetRegressionAccessesSource',
            title = 'Test Get Regression Accesses Title',
            independent = 'Test Get Regression Accesses Independent',
            dependent = 'Test Get Regression Accesses Dependent',
            precision = 4,
            data_set = [[1, 2], [3, 4], [5, 6]],
            linear_coefficients = [2, 3],
            linear_points = {'roots': [[1, 0]], 'inflections': [None]},
            linear_correlation = 0.5,
            quadratic_coefficients = [2, 3, 5],
            quadratic_points = {'roots': [[1, 0], [10, 0]], 'maxima': [[3, 57]]},
            quadratic_correlation = 0.5,
            cubic_coefficients = [2, 3, 5, 7],
            cubic_points = {'roots': [[1, 0], [5, 0], [10, 0]], 'maxima': [[3, 57]]},
            cubic_correlation = 0.5,
            hyperbolic_coefficients = [2, 3],
            hyperbolic_points = {'roots': [[1, 0]], 'maxima': [None]},
            hyperbolic_correlation = 0.5,
            exponential_coefficients = [2, 3],
            exponential_points = {'roots': [None], 'maxima': [None]},
            exponential_correlation = 0.5,
            logarithmic_coefficients = [2, 3],
            logarithmic_points = {'roots': [[1, 0]], 'maxima': [None]},
            logarithmic_correlation = 0.5,
            logistic_coefficients = [2, 3, 5],
            logistic_points = {'roots': [None], 'inflections': [[5, 7]]},
            logistic_correlation = 0.5,
            sinusoidal_coefficients = [2, 3, 5, 7],
            sinusoidal_points = {'roots': [[2, 0], [4, 0]], 'inflections': [[5, 7], [7, 7]]},
            sinusoidal_correlation = 0.5,
            best_fit = 'hyperbolic',
            date = datetime.now()
        )

        db.session.add(new_regression)
        db.session.commit()

        found_regression = Regression.query.filter_by(
            user_id = found_user_id, 
            source = 'TestGetRegressionAccessesSource'
        ).first()

        res = client.get(
            "/get_regression_accesses?key=ABC123&source=TestGetRegressionAccessesSource"
        )

        received_regression = json.loads(res.data.decode())
        assert received_regression['title'] == found_regression.title
        assert received_regression['best_fit'] == found_regression.best_fit
        assert res.status_code == 200

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_get_regression_without_source(self, app, client):
        @app.route("/get_regression_without_source", methods=["GET"])
        def get_regression_without_source_route():
            get_regression_without_source = get_regression()
            return get_regression_without_source
        
        new_user = User(
            name = 'Test Get Regression Fails without Source',
            email = 'test_get_regression_without_source@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_get_regression_without_source@email.com'
        ).first()

        res = client.get(
            "/get_regression_accesses?key=ABC123"
        )

        assert res.data == b'Source must be provided'
        assert res.status_code == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_get_regression_nonexistent_source(self, app, client):
        @app.route("/get_regression_nonexistent_source", methods=["GET"])
        def get_regression_nonexistent_source_route():
            get_regression_nonexistent_source = get_regression()
            return get_regression_nonexistent_source
        
        new_user = User(
            name = 'Test Get Regression Fails Nonexistent Source',
            email = 'test_get_regression_nonexistent_source@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_get_regression_nonexistent_source@email.com'
        ).first()

        res = client.get(
            "/get_regression_accesses?key=ABC123&source=TestGetRegressionFailsNonexistentSource"
        )

        assert res.data == b'Data set not found'
        assert res.status_code == 404

        db.session.delete(found_user)
        db.session.commit()

class TestPutRegressionsController:
    pass

class TestDeleteRegressionsController:
    def test_delete_regression_destroys(self, app, client):
        @app.route("/delete_regression_destroys", methods=["DELETE"])
        def delete_regression_destroys_route():
            delete_regression_destroys = delete_regression()
            return delete_regression_destroys
        
        new_user = User(
            name = 'Test Delete Regression Destroys',
            email = 'test_delete_regression_destroys@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_delete_regression_destroys@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestDeleteRegressionDestroysSource',
            title = 'Test Delete Regression Destroys Title',
            independent = 'Test Delete Regression Destroys Independent',
            dependent = 'Test Delete Regression Destroys Dependent',
            precision = 4,
            data_set = [[1, 2], [3, 4], [5, 6]],
            linear_coefficients = [2, 3],
            linear_points = {'roots': [[1, 0]], 'inflections': [None]},
            linear_correlation = 0.5,
            quadratic_coefficients = [2, 3, 5],
            quadratic_points = {'roots': [[1, 0], [10, 0]], 'maxima': [[3, 57]]},
            quadratic_correlation = 0.5,
            cubic_coefficients = [2, 3, 5, 7],
            cubic_points = {'roots': [[1, 0], [5, 0], [10, 0]], 'maxima': [[3, 57]]},
            cubic_correlation = 0.5,
            hyperbolic_coefficients = [2, 3],
            hyperbolic_points = {'roots': [[1, 0]], 'maxima': [None]},
            hyperbolic_correlation = 0.5,
            exponential_coefficients = [2, 3],
            exponential_points = {'roots': [None], 'maxima': [None]},
            exponential_correlation = 0.5,
            logarithmic_coefficients = [2, 3],
            logarithmic_points = {'roots': [[1, 0]], 'maxima': [None]},
            logarithmic_correlation = 0.5,
            logistic_coefficients = [2, 3, 5],
            logistic_points = {'roots': [None], 'inflections': [[5, 7]]},
            logistic_correlation = 0.5,
            sinusoidal_coefficients = [2, 3, 5, 7],
            sinusoidal_points = {'roots': [[2, 0], [4, 0]], 'inflections': [[5, 7], [7, 7]]},
            sinusoidal_correlation = 0.5,
            best_fit = 'hyperbolic',
            date = datetime.now()
        )

        db.session.add(new_regression)
        db.session.commit()

        res = client.delete(
            "/delete_regression_destroys?key=ABC123&source=TestDeleteRegressionDestroysSource"
        )

        found_regression = Regression.query.filter_by(
            user_id = found_user_id, 
            source = 'TestDeleteRegressionDestroysSource'
        ).first()

        assert res.status_code == 204
        assert not found_regression

        db.session.delete(found_user)
        db.session.commit()

class TestRegressionsController:
    pass