from regressions.execute import run_all
from flask import request
from datetime import datetime
from app import db
from app.models import Regression
from app.middleware.current import current_user, current_regression

def post_regressions():
    user_id = current_user()['id']
    source = request.args.get('source')
    found_regression = Regression.query.filter_by(
        user_id = user_id, 
        source = source
    ).first()
    if not found_regression:
        title = request.json.get('title')
        independent = request.json.get('independent')
        dependent = request.json.get('dependent')
        data_set = request.json.get('data_set')
        precision = request.json.get('precision')
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
        new_regression = Regression(
            user_id=user_id,
            source=source,
            title=title,
            independent=independent,
            dependent=dependent,
            data_set=data_set,
            precision=precision,
            linear_coefficients=linear_coefficients,
            linear_points=linear_points,
            linear_correlation=linear_correlation,
            quadratic_coefficients=quadratic_coefficients,
            quadratic_points=quadratic_points,
            quadratic_correlation=quadratic_correlation,
            cubic_coefficients=cubic_coefficients,
            cubic_points=cubic_points,
            cubic_correlation=cubic_correlation,
            hyperbolic_coefficients=hyperbolic_coefficients,
            hyperbolic_points=hyperbolic_points,
            hyperbolic_correlation=hyperbolic_correlation,
            exponential_coefficients=exponential_coefficients,
            exponential_points=exponential_points,
            exponential_correlation=exponential_correlation,
            logarithmic_coefficients=logarithmic_coefficients,
            logarithmic_points=logarithmic_points,
            logarithmic_correlation=logarithmic_correlation,
            logistic_coefficients=logistic_coefficients,
            logistic_points=logistic_points,
            logistic_correlation=logistic_correlation,
            sinusoidal_coefficients=sinusoidal_coefficients,
            sinusoidal_points=sinusoidal_points,
            sinusoidal_correlation=sinusoidal_correlation,
            best_fit=best_fit,
            date=datetime.now()
        )
        db.session.add(new_regression)
        db.session.commit()
        return current_regression(), 201
    else:
        return 'Source already in use by other collection', 409