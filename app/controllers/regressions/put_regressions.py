from regressions.execute import run_all
from flask import request
from datetime import datetime
from app import db
from app.models import Regression
from app.middleware.current import current_user, current_regression

def put_regressions():
    user_id = current_user()['id']
    source = request.args.get('source')
    try:
        found_regression = Regression.query.filter_by(
            user_id=user_id, 
            source=source
        ).first()
        updated_title = request.json.get('title')
        updated_independent = request.json.get('independent')
        updated_dependent = request.json.get('dependent')
        updated_precision = request.json.get('precision')
        updated_data_set = request.json.get('data_set')
        if (updated_data_set != found_regression.data_set) or (updated_precision != found_regression.precision):
            results = run_all(updated_data_set, updated_precision)
            found_regression.linear_coefficients = results['models']['linear']['constants']
            found_regression.linear_points = results['models']['linear']['points']
            found_regression.linear_correlation = results['models']['linear']['correlation']
            found_regression.quadratic_coefficients = results['models']['quadratic']['constants']
            found_regression.quadratic_points = results['models']['quadratic']['points']
            found_regression.quadratic_correlation = results['models']['quadratic']['correlation']
            found_regression.cubic_coefficients = results['models']['cubic']['constants']
            found_regression.cubic_points = results['models']['cubic']['points']
            found_regression.cubic_correlation = results['models']['cubic']['correlation']
            found_regression.hyperbolic_coefficients = results['models']['hyperbolic']['constants']
            found_regression.hyperbolic_points = results['models']['hyperbolic']['points']
            found_regression.hyperbolic_correlation = results['models']['hyperbolic']['correlation']
            found_regression.exponential_coefficients = results['models']['exponential']['constants']
            found_regression.exponential_points = results['models']['exponential']['points']
            found_regression.exponential_correlation = results['models']['exponential']['correlation']
            found_regression.logarithmic_coefficients = results['models']['logarithmic']['constants']
            found_regression.logarithmic_points = results['models']['logarithmic']['points']
            found_regression.logarithmic_correlation = results['models']['logarithmic']['correlation']
            found_regression.logistic_coefficients = results['models']['logistic']['constants']
            found_regression.logistic_points = results['models']['logistic']['points']
            found_regression.logistic_correlation = results['models']['logistic']['correlation']
            found_regression.sinusoidal_coefficients = results['models']['sinusoidal']['constants']
            found_regression.sinusoidal_points = results['models']['sinusoidal']['points']
            found_regression.sinusoidal_correlation = results['models']['sinusoidal']['correlation']
            found_regression.best_fit = results['optimal']['option']
        found_regression.title = updated_title
        found_regression.independent = updated_independent
        found_regression.dependent = updated_dependent
        found_regression.precision = updated_precision
        found_regression.data_set = updated_data_set
        found_regression.date = datetime.now()
        db.session.commit()
        return current_regression(), 200
    except Exception:
        return 'Data set not found', 404