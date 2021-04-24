from flask import render_template, flash, redirect, url_for, request
from datetime import datetime
from app import app, db
from app.models import User, Regression
from app.forms import SignUpForm
from regressions.execute import run_all
from .middleware.generator import generator
from .middleware.available import available
from .middleware.decorators import require_apikey
from .middleware.current import current_user, current_regression

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    test_key = generator()
    key_available = available(test_key)
    if key_available:
        form = SignUpForm(key=test_key)
        if form.validate_on_submit():
            new_user = User(
                name=form.name.data,
                email=form.email.data,
                key=form.key.data,
                date=datetime.now()
            )
            db.session.add(new_user)
            db.session.commit()
            flash(f'API Key for user {form.key.data}')
            return redirect(url_for('index'))
        return render_template('signup.html', form=form)
    else:
        return signup()

@app.route('/api', methods=['GET', 'POST'])
@require_apikey
def regression_access():
    if request.method == 'POST':
        user_id = current_user()['id']
        source = request.args.get('source')
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
        return 'Regression models created and added to table'
    if request.method == 'GET':
        return current_regression()