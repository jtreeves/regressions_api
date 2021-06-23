from flask import request
from flask import render_template
from app import app
from .forms import SignUpForm
from .utilities.unique_key import unique_key
from .utilities.require_key import require_key
from .controllers.main_controller import main_controller
from .controllers.images_controller import images_controller
from .controllers.users_controller import users_controller
from .controllers.regressions_controller import regressions_controller

@app.route('/')
def home_route():
    """ Create public route for Home page """
    return main_controller['get_home']()

@app.route('/about')
def about_route():
    """ Create public route for About page """
    return main_controller['get_about']()

@app.route('/usage')
def usage_route():
    """ Create public route for Usage page """
    return main_controller['get_usage']()

@app.route('/math')
def math_route():
    """ Create public route for Math page """
    return main_controller['get_math']()

@app.route('/images/<source>')
def images_route(source):
    """ Create public route for all images """
    return images_controller(source)

@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
    """ Create public route for Signup page """

    # Use helper function to create a unique key
    key = unique_key()

    # Use form class to create a form with the created key as a hidden field
    form = SignUpForm(key = key)

    # Render an empty form if GET request
    if request.method == 'GET':
        return users_controller['get_signup'](form)
    
    # Render the key or an error message if POST request
    if request.method == 'POST':
        return users_controller['post_signup'](form)

@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
@require_key
def api_route():
    """ Create private route for API requests """

    # Create a new collection if POST request
    if request.method == 'POST':
        return regressions_controller['post_regression']()
    
    # Get an existing collection if GET request
    if request.method == 'GET':
        return regressions_controller['get_regression']()
    
    # Update an existing collection if PUT request
    if request.method == 'PUT':
        return regressions_controller['put_regression']()
    
    # Delete an existing collection if DELETE request
    if request.method == 'DELETE':
        return regressions_controller['delete_regression']()