from flask import request
from app import app
from .forms import SignUpForm
from .middleware.generator import generator
from .middleware.available import available
from .middleware.decorators import require_apikey
from .controllers.main_controller import main_controller
from .controllers.users_controller import users_controller
from .controllers.regressions_controller import regressions_controller

@app.route('/')
def home_route():
    return main_controller['get_home']()

@app.route('/about')
def about_route():
    return main_controller['get_about']()

@app.route('/usage')
def usage_route():
    return main_controller['get_usage']()

@app.route('/math')
def math_route():
    return main_controller['get_math']()

@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
    test_key = generator()
    key_available = available(test_key)
    if key_available:
        form = SignUpForm(key = test_key)
        if request.method == 'GET':
            return users_controller['get_signup'](form)
        if request.method == 'POST':
            return users_controller['post_signup'](form)
    else:
        return signup_route()

@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
@require_apikey
def api_route():
    if request.method == 'POST':
        return regressions_controller['post_regressions']()
    if request.method == 'GET':
        return regressions_controller['get_regressions']()
    if request.method == 'PUT':
        return regressions_controller['put_regressions']()
    if request.method == 'DELETE':
        return regressions_controller['delete_regressions']()