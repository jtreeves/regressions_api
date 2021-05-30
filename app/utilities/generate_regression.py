from regressions.execute import run_all

def generate_regression(data_set, precision):
    results = run_all(data_set, precision)

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
    
    return new_regression