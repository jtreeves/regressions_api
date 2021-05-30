from datetime import datetime
from app import db
from app.utilities.generate_regression import generate_regression
from .find_regression import find_regression
from .read_regression import read_regression

def update_regression(user_id, source, submission):
    try:
        found_regression = find_regression(user_id, source)
        
        updated_title = submission['title']
        updated_independent = submission['independent']
        updated_dependent = submission['dependent']
        updated_precision = submission['precision']
        updated_data_set = submission['data_set']
        
        if (updated_data_set != found_regression.data_set) or (updated_precision != found_regression.precision):
            results = generate_regression(updated_data_set, updated_precision)
            found_regression.linear_coefficients = results['linear_coefficients']
            found_regression.linear_points = results['linear_points']
            found_regression.linear_correlation = results['linear_correlation']
            found_regression.quadratic_coefficients = results['quadratic_coefficients']
            found_regression.quadratic_points = results['quadratic_points']
            found_regression.quadratic_correlation = results['quadratic_correlation']
            found_regression.cubic_coefficients = results['cubic_coefficients']
            found_regression.cubic_points = results['cubic_points']
            found_regression.cubic_correlation = results['cubic_correlation']
            found_regression.hyperbolic_coefficients = results['hyperbolic_coefficients']
            found_regression.hyperbolic_points = results['hyperbolic_points']
            found_regression.hyperbolic_correlation = results['hyperbolic_correlation']
            found_regression.exponential_coefficients = results['exponential_coefficients']
            found_regression.exponential_points = results['exponential_points']
            found_regression.exponential_correlation = results['exponential_correlation']
            found_regression.logarithmic_coefficients = results['logarithmic_coefficients']
            found_regression.logarithmic_points = results['logarithmic_points']
            found_regression.logarithmic_correlation = results['logarithmic_correlation']
            found_regression.logistic_coefficients = results['logistic_coefficients']
            found_regression.logistic_points = results['logistic_points']
            found_regression.logistic_correlation = results['logistic_correlation']
            found_regression.sinusoidal_coefficients = results['sinusoidal_coefficients']
            found_regression.sinusoidal_points = results['sinusoidal_points']
            found_regression.sinusoidal_correlation = results['sinusoidal_correlation']
            found_regression.best_fit = results['best_fit']
        
        found_regression.title = updated_title
        found_regression.independent = updated_independent
        found_regression.dependent = updated_dependent
        found_regression.precision = updated_precision
        found_regression.data_set = updated_data_set
        found_regression.date = datetime.now()
        db.session.commit()
        
        return read_regression(user_id, source), 200
    
    except Exception:
        return 'Data set not found', 404