from flask import request
from app import app
from .forms import SignUpForm
from .utilities.unique_key import unique_key
from .utilities.require_key import require_key
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
    key = unique_key()
    form = SignUpForm(key = key)

    if request.method == 'GET':
        return users_controller['get_signup'](form)
    
    if request.method == 'POST':
        return users_controller['post_signup'](form)

@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
@require_key
def api_route():
    if request.method == 'POST':
        return regressions_controller['post_regression']()
    
    if request.method == 'GET':
        return regressions_controller['get_regression']()
    
    if request.method == 'PUT':
        return regressions_controller['put_regression']()
    
    if request.method == 'DELETE':
        return regressions_controller['delete_regression']()