from flask import request
from app.models import User, Regression

def current_user(*args):
    sent_key = request.args.get('key')
    found_user = User.query.filter_by(key=sent_key).first()
    dict_user = {
        'id': found_user.id,
        'name': found_user.name,
        'email': found_user.email,
        'key': found_user.key,
        'date': found_user.date
    }
    return dict_user

def current_regression(*args):
    sent_id = request.args.get('id')
    found_regression = Regression.query.filter_by(id=sent_id).first()
    dict_regression = {
        'id': found_regression.id,
        'user_id': found_regression.user_id,
        'title': found_regression.title,
        'independent': found_regression.independent,
        'dependent': found_regression.dependent,
        'data_set': found_regression.data_set,
        'linear_coefficients': found_regression.linear_coefficients,
        'linear_error': found_regression.linear_error,
        'quadratic_coefficients': found_regression.quadratic_coefficients,
        'quadratic_error': found_regression.quadratic_error,
        'cubic_coefficients': found_regression.cubic_coefficients,
        'cubic_error': found_regression.cubic_error,
        'hyperbolic_coefficients': found_regression.hyperbolic_coefficients,
        'hyperbolic_error': found_regression.hyperbolic_error,
        'exponential_coefficients': found_regression.exponential_coefficients,
        'exponential_error': found_regression.exponential_error,
        'logarithmic_coefficients': found_regression.logarithmic_coefficients,
        'logarithmic_error': found_regression.logarithmic_error,
        'best_fit': found_regression.best_fit,
        'date': found_regression.date
    }
    return dict_regression