from datetime import datetime
from app import db
from app.models import Regression
from app.utilities.generate_regression import generate_regression
from .find_regression import find_regression
from .read_regression import read_regression

def create_regression(user_id, source, submission):
    """ Create new collection of regression models from a user_id, source, and submission """

    # Use helper function to search database for any competing existing collection
    found_regression = find_regression(user_id, source)
    
    # Proceed if no collection already exists
    if not found_regression:
        # Grab keys from submission dictionary
        title = submission['title']
        independent = submission['independent']
        dependent = submission['dependent']
        data_set = submission['data_set']
        precision = submission['precision']

        # Use helper function to create collection
        results = generate_regression(data_set, precision)

        # Proceed if collection created
        if not isinstance(results, tuple):
            # Grab keys from results dictionary
            linear_coefficients = results['linear_coefficients']
            linear_points = results['linear_points']
            linear_correlation = results['linear_correlation']
            quadratic_coefficients = results['quadratic_coefficients']
            quadratic_points = results['quadratic_points']
            quadratic_correlation = results['quadratic_correlation']
            cubic_coefficients = results['cubic_coefficients']
            cubic_points = results['cubic_points']
            cubic_correlation = results['cubic_correlation']
            hyperbolic_coefficients = results['hyperbolic_coefficients']
            hyperbolic_points = results['hyperbolic_points']
            hyperbolic_correlation = results['hyperbolic_correlation']
            exponential_coefficients = results['exponential_coefficients']
            exponential_points = results['exponential_points']
            exponential_correlation = results['exponential_correlation']
            logarithmic_coefficients = results['logarithmic_coefficients']
            logarithmic_points = results['logarithmic_points']
            logarithmic_correlation = results['logarithmic_correlation']
            logistic_coefficients = results['logistic_coefficients']
            logistic_points = results['logistic_points']
            logistic_correlation = results['logistic_correlation']
            sinusoidal_coefficients = results['sinusoidal_coefficients']
            sinusoidal_points = results['sinusoidal_points']
            sinusoidal_correlation = results['sinusoidal_correlation']
            best_fit = results['best_fit']
            
            # Pass data into Regression model
            new_regression = Regression(
                user_id = user_id,
                source = source,
                title = title,
                independent = independent,
                dependent = dependent,
                precision = precision,
                data_set = data_set,
                linear_coefficients = linear_coefficients,
                linear_points = linear_points,
                linear_correlation = linear_correlation,
                quadratic_coefficients = quadratic_coefficients,
                quadratic_points = quadratic_points,
                quadratic_correlation = quadratic_correlation,
                cubic_coefficients = cubic_coefficients,
                cubic_points = cubic_points,
                cubic_correlation = cubic_correlation,
                hyperbolic_coefficients = hyperbolic_coefficients,
                hyperbolic_points = hyperbolic_points,
                hyperbolic_correlation = hyperbolic_correlation,
                exponential_coefficients = exponential_coefficients,
                exponential_points = exponential_points,
                exponential_correlation = exponential_correlation,
                logarithmic_coefficients = logarithmic_coefficients,
                logarithmic_points = logarithmic_points,
                logarithmic_correlation = logarithmic_correlation,
                logistic_coefficients = logistic_coefficients,
                logistic_points = logistic_points,
                logistic_correlation = logistic_correlation,
                sinusoidal_coefficients = sinusoidal_coefficients,
                sinusoidal_points = sinusoidal_points,
                sinusoidal_correlation = sinusoidal_correlation,
                best_fit = best_fit,
                date = datetime.now()
            )
            
            # Add new collection to database
            db.session.add(new_regression)
            db.session.commit()
            
            # Return new collection
            return read_regression(user_id, source)
        
        # Return error code if problem with submission
        else:
            return results
        
    # Return error code if problem arises from helper function
    else:
        # Return error code if source not provided
        if isinstance(found_regression, tuple):
            return found_regression
        
        # Return error code if element already exists in database
        else:
            return 'Source already in use by other collection', 409