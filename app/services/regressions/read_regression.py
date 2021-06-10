from .find_regression import find_regression

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