# Regressionz API

This is the respository for the RΣGRΣSSIONZ API. It contains all the pertinent code for the frontend and backend of the Flask app. To use the API, visit the [RΣGRΣSSIONZ](https://regressionz.herokuapp.com) site, publicly deployed on Heroku.

**Contents**

1. [About](https://github.com/jtreeves/regressions_api#about)
2. [Installation](https://github.com/jtreeves/regressions_api#installation)
3. [Features](https://github.com/jtreeves/regressions_api#features)
4. [Dependencies](https://github.com/jtreeves/regressions_api#dependencies)
5. [Models](https://github.com/jtreeves/regressions_api#models)
6. [Routes](https://github.com/jtreeves/regressions_api#routes)
7. [File Structure](https://github.com/jtreeves/regressions_api#file-structure)
8. [User Stories](https://github.com/jtreeves/regressions_api#user-stories)
9. [Designs](https://github.com/jtreeves/regressions_api#designs)
10. [Code Examples](https://github.com/jtreeves/regressions_api#code-examples)
11. [Future Goals](https://github.com/jtreeves/regressions_api#future-goals)

## About

I wanted to create an API that could be used as an intermediary between [my Python library](https://pypi.org/project/regressions/) for generating regression models and [my more user-friendly JavaScript app](https://tiresias-predictions.herokuapp.com) for seeing the results. Unlike the full-blown app, which allows users to input data sets and see results in graphical form in a browser window, I wanted this API to merely provide users with an API key, which they could then use independently for their own projects. The intent was to be less visual-oriented and more data-oriented. It is particulary ideal for anyone who wants to use the output from a Python library without needing to code in Python.

By using the Regressions library, the RΣGRΣSSIONZ API can provide users with a data-rich object containing coefficients, points, and correlations of 8 different models:
- linear
- quadratic
- cubic
- hyperbolic
- exponential
- logarithmic
- logistic
- sinusoidal

## Installation

### Create Local Repository

1. Fork and clone this repository to your local computer
2. Run `pip3 install requirements.txt` to install all necessary dependencies
3. Set up a `.env` file to hold the `FLASK_APP`, `SECRET_KEY`, and `DATABASE_URL` variables (set the first to `manage.py`, the secret to whatever string you like, and the last to your local database)

### Set Up Local Database

1. Verify that you have Postgres installed on your computer by typing `psql` into your terminal to launch the PSQL shell (install Postgres if necessary)
2. Run `flask db init` to create a database named `regressionz` in your local Postgres (confirm by typing `\c` while in the PSQL shell)
3. Run `flask db migrate` to create the necessary tables within your new database

### Run Locally

1. Run `flask run` to start the app
2. View the live version of the site at `http://localhost:5000` in the browser of your choosing

Alternatively, you may use the live version of the [RΣGRΣSSIONZ](https://regressionz.herokuapp.com) API.

## Features

- Flask app
- Postgres database
- API with full CRUD functionality
- Documentation of usage
- Graphs of function types
- LaTeX equations
- Error handling to weed out invalid submissions
- 269 tests
- Mobile-responsive design

## Dependencies

- Regressions: Python library for generating regression models from data sets, which I [built previously](https://github.com/jtreeves/regressions_library) (used to create models for users)
- SQLAlchemy: Python ORM for working with SQL (used for database)
- WTForms: Python library for form validation (used for sign up form)
- Matplotlib: Python library for creating visualizations (used to create graphs)
- NumPy: Python library for sophisticated mathematical computation (used to accurately provide data to graphs)
- PyTest: Python testing tool (used for all 269 tests)

## Models

![ERD](/images/erd.png)

## Routes

| Method | Model | Path | File | Description | 
| ------ | ----- | ---- | ---- | ----------- |
| POST | regressions | /api?key=\<str:key\>&source=\<str:source\> | routes.py | Create new collection |
| GET | regressions | /api?key=\<str:key\>&source=\<str:source\> | routes.py | Read existing collection |
| PUT | regressions | /api?key=\<str:key\>&source=\<str:source\> | routes.py | Update existing collection |
| DELETE | regressions | /api?key=\<str:key\>&source=\<str:source\> | routes.py | Delete existing collection |

## File Structure

An overview of the project's file structure. Note: Not all files are included, merely a representative sampling.

```
regressions_api
|-- .env
|-- .gitignore
|-- Procfile
|-- requirements.txt
|-- configurations.py
|-- manage.py
|-- setup.py
|-- app
|   |-- __init__.py
|   |-- routes.py
|   |-- models.py
|   |-- forms.py
|   |-- utilities
|   |   |-- generate_key.py
|   |   |-- request_query.py
|   |   |-- vet_data_set.py
|   |-- services
|   |   |-- users
|   |   |   |-- create_user.py
|   |   |   |-- read_user.py
|   |   |-- regressions
|   |   |   |-- create_regression.py
|   |   |   |-- find_regression.py
|   |   |   |-- read_regression.py
|   |   |   |-- update_regression.py
|   |   |   |-- destroy_regression.py
|   |-- controllers
|   |   |-- main_controller.py
|   |   |-- images_controller.py
|   |   |-- users_controller.py
|   |   |-- regressions_controller.py
|   |   |-- main
|   |   |   |-- get_home.py
|   |   |   |-- get_about.py
|   |   |   |-- get_usage.py
|   |   |   |-- get_math.py
|   |   |-- images
|   |   |   |-- create_root_graph.py
|   |   |   |-- create_maximum_graph.py
|   |   |   |-- create_minimum_graph.py
|   |   |   |-- create_inflection_graph.py
|   |   |-- users
|   |   |   |-- get_signup.py
|   |   |   |-- post_signup.py
|   |   |-- regressions
|   |   |   |-- get_regression.py
|   |   |   |-- post_regression.py
|   |   |   |-- put_regression.py
|   |   |   |-- delete_regression.py
|   |-- static
|   |   |-- style
|   |   |   |-- main.css
|   |   |   |-- about.css
|   |   |   |-- usage.css
|   |   |   |-- math.css
|   |   |   |-- signup.css
|   |   |-- scripts
|   |   |   |-- latex.js
|   |-- templates
|   |   |-- base.html
|   |   |-- partials
|   |   |   |-- header.html
|   |   |   |-- navigation.html
|   |   |   |-- footer.html
|   |   |-- pages
|   |   |   |-- home.html
|   |   |   |-- about.html
|   |   |   |-- usage.html
|   |   |   |-- math.html
|   |   |   |-- signup.html
|   |   |-- sections
|   |   |   |-- creating.html
|   |   |   |-- deleting.html
|   |   |   |-- interpreting.html
|   |   |-- articles
|   |   |   |-- roots.html
|   |   |   |-- maxima.html
|   |   |   |-- minima.html
|   |   |   |-- inflections.html
|   |   |-- snippets
|   |   |   |-- get_url.html
|   |   |   |-- post_body.html
|   |   |   |-- response_object.html
|   |   |-- subheads
|   |   |   |-- aspects.html
|   |   |   |-- icons.html
|   |   |   |-- settings.html
|-- tests
|   |-- conftest.py
|   |-- test_models.py
|   |-- test_templates.py
|   |-- test_routes.py
|   |-- test_forms.py
|   |-- test_services.py
|   |-- test_controllers.py
|   |-- test_utilities.py
|-- migrations
|   |-- env.py
|   |-- alembic.ini
```

## User Stories

- As a potential user, I want to know about its appeal, so I have a reason to sign up.
- As a potential user, I want to see specific examples of how it can be used by customers, so I know how I can implement it.
- As a potential user, I want to understand the mathematical logic that it implements and how it differs from any competitors, so I can understand the logic.
- As a potential user, I want to be able to sign up for an API key, so I can use it.
- As a user, I want to be able to upload my data to their database by using my API key, so I can access it.
- As a user, I want to be able to view my data stored in their database by using my API key, so I can access it.
- As a user, I want to know that no one else can access my data, so I know it is secure.
- As a user, I want to get extensive info from the API, so I know that it was worth signing up for.
- As a user, I want to get the data in a raw format, so I can easily customize it to my needs.

## Designs

**Home Page**
![Home Page](/images/design1.png)

**Math Explanation**
![Math Explanation](/images/design2.png)

**Usage Guide**
![Usage Guide](/images/design3.png)

**Sign Up**
![Sign Up](/images/design4.png)

## Code Examples

**Use helper functions to simplify routing**
```python
def api_route():
    if request.method == 'POST':
        return regressions_controller['post_regression']()
    if request.method == 'GET':
        return regressions_controller['get_regression']()    
    if request.method == 'PUT':
        return regressions_controller['put_regression']()
    if request.method == 'DELETE':
        return regressions_controller['delete_regression']()
```

**Access regression models in database**
```python
def read_regression(user_id, source):
    try:
        found_regression = find_regression(user_id, source)
        if not isinstance(found_regression, tuple):
            regression_analysis = {
                'source': found_regression.source,
                'title': found_regression.title,
                'independent': found_regression.independent,
                'dependent': found_regression.dependent,
                'data_set': found_regression.data_set,
                'precision': found_regression.precision,
                'linear_coefficients': found_regression.linear_coefficients,
                'linear_points': found_regression.linear_points,
                'linear_correlation': found_regression.linear_correlation,
                'quadratic_coefficients': found_regression.quadratic_coefficients,
                'quadratic_points': found_regression.quadratic_points,
                'quadratic_correlation': found_regression.quadratic_correlation,
                'cubic_coefficients': found_regression.cubic_coefficients,
                'cubic_points': found_regression.cubic_points,
                'cubic_correlation': found_regression.cubic_correlation,
                'hyperbolic_coefficients': found_regression.hyperbolic_coefficients,
                'hyperbolic_points': found_regression.hyperbolic_points,
                'hyperbolic_correlation': found_regression.hyperbolic_correlation,
                'exponential_coefficients': found_regression.exponential_coefficients,
                'exponential_points': found_regression.exponential_points,
                'exponential_correlation': found_regression.exponential_correlation,
                'logarithmic_coefficients': found_regression.logarithmic_coefficients,
                'logarithmic_points': found_regression.logarithmic_points,
                'logarithmic_correlation': found_regression.logarithmic_correlation,
                'logistic_coefficients': found_regression.logistic_coefficients,
                'logistic_points': found_regression.logistic_points,
                'logistic_correlation': found_regression.logistic_correlation,
                'sinusoidal_coefficients': found_regression.sinusoidal_coefficients,
                'sinusoidal_points': found_regression.sinusoidal_points,
                'sinusoidal_correlation': found_regression.sinusoidal_correlation,
                'best_fit': found_regression.best_fit,
                'date': found_regression.date
            }
            return regression_analysis
        else:
            return found_regression
    except Exception:
        return 'Data set not found', 404
```

**Add wrapper to protect private routes**
```python
def require_key(protected_function):
    @wraps(protected_function)
    def decorated_function(*args, **kwargs):
        sent_key = request.args.get('key')
        if sent_key:
            found_user = read_user(sent_key)
            if found_user:
                return protected_function(*args, **kwargs)
            else:
                abort(make_response('User not authenticated', 401))
        else:
            abort(make_response('Key must be provided', 403))
    return decorated_function
```

**Create cubic graph with marked maximum point using Matplotlib**
```python
def create_maximum_graph():
    fig = Figure(figsize=(5, 5))
    fig.set_tight_layout(True)
    graph = fig.add_subplot(1, 1, 1)
    xs = arange(0.0, 10.0, 0.1)
    ys = [(x**3 - 15 * x**2 + 63 * x - 31) for x in xs]
    graph.plot(xs, ys)
    graph.plot([3], [50], marker='o', markersize=10, mfc='none', color='red')
    graph.grid()
    return fig
```

## Future Goals

- Send data via headers instead of parameters to make it more secure
- Store hashed or otherwise encrypted version of API keys to better protect user data
- Improve design to make it more enticing to prospective users