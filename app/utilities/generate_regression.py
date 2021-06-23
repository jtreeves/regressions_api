from regressions.execute import run_all
from .vet_data_set import vet_data_set
from .vet_precision import vet_precision

def generate_regression(data_set, precision):
    """ Use Regressions library to generate all regression models for a data set """

    # Validate both data set and precision before proceeding
    vetted_data_set = vet_data_set(data_set)
    vetted_precision = vet_precision(precision)

    # Proceed if data set meets criteria
    if not isinstance(vetted_data_set, tuple):

        # Proceed if precision meets criteria
        if not isinstance(vetted_precision, tuple):
            # Use imported library to generate models
            results = run_all(vetted_data_set, vetted_precision)

            # Assign results to new variables
            linear_coefficients = results['models']['linear']['constants']
            linear_points = results['models']['linear']['points']
            linear_correlation = results['models']['linear']['correlation']
            quadratic_coefficients = results['models']['quadratic']['constants']
            quadratic_points = results['models']['quadratic']['points']
            quadratic_correlation = results['models']['quadratic']['correlation']
            cubic_coefficients = results['models']['cubic']['constants']
            cubic_points = results['models']['cubic']['points']
            cubic_correlation = results['models']['cubic']['correlation']
            hyperbolic_coefficients = results['models']['hyperbolic']['constants']
            hyperbolic_points = results['models']['hyperbolic']['points']
            hyperbolic_correlation = results['models']['hyperbolic']['correlation']
            exponential_coefficients = results['models']['exponential']['constants']
            exponential_points = results['models']['exponential']['points']
            exponential_correlation = results['models']['exponential']['correlation']
            logarithmic_coefficients = results['models']['logarithmic']['constants']
            logarithmic_points = results['models']['logarithmic']['points']
            logarithmic_correlation = results['models']['logarithmic']['correlation']
            logistic_coefficients = results['models']['logistic']['constants']
            logistic_points = results['models']['logistic']['points']
            logistic_correlation = results['models']['logistic']['correlation']
            sinusoidal_coefficients = results['models']['sinusoidal']['constants']
            sinusoidal_points = results['models']['sinusoidal']['points']
            sinusoidal_correlation = results['models']['sinusoidal']['correlation']
            best_fit = results['optimal']['option']
            
            # Store variables in dictionary
            new_regression = {
                'linear_coefficients': linear_coefficients,
                'linear_points': linear_points,
                'linear_correlation': linear_correlation,
                'quadratic_coefficients': quadratic_coefficients,
                'quadratic_points': quadratic_points,
                'quadratic_correlation': quadratic_correlation,
                'cubic_coefficients': cubic_coefficients,
                'cubic_points': cubic_points,
                'cubic_correlation': cubic_correlation,
                'hyperbolic_coefficients': hyperbolic_coefficients,
                'hyperbolic_points': hyperbolic_points,
                'hyperbolic_correlation': hyperbolic_correlation,
                'exponential_coefficients': exponential_coefficients,
                'exponential_points': exponential_points,
                'exponential_correlation': exponential_correlation,
                'logarithmic_coefficients': logarithmic_coefficients,
                'logarithmic_points': logarithmic_points,
                'logarithmic_correlation': logarithmic_correlation,
                'logistic_coefficients': logistic_coefficients,
                'logistic_points': logistic_points,
                'logistic_correlation': logistic_correlation,
                'sinusoidal_coefficients': sinusoidal_coefficients,
                'sinusoidal_points': sinusoidal_points,
                'sinusoidal_correlation': sinusoidal_correlation,
                'best_fit': best_fit
            }
            
            # Return dictionary
            return new_regression
        
        # Return error code if precision fails criteria
        else:
            return vetted_precision

    # Return error code if data set fails criteria
    else:
        return vetted_data_set