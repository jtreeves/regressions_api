from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import User, Regression
from app.forms import SignUpForm
from .middleware.generator import generator
from .middleware.available import available
from datetime import datetime
from .middleware.decorators import require_apikey
from .middleware.current import current
from regressions.run_all import run_all

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

@app.route('/api/user', methods=['GET', 'POST'])
@require_apikey
def user_access():
    current_user = current()
    return current_user

@app.route('/api/regression', methods=['GET', 'POST'])
@require_apikey
def regression_access():
    if request.method == 'POST':
        user_id = current()['id']
        title = request.json.get('title')
        independent = request.json.get('independent')
        dependent = request.json.get('dependent')
        data_set = request.json.get('data_set')
        results = run_all(data_set)
        linear_coefficients = results['options']['linear']['constants']
        linear_error = results['options']['linear']['error']
        quadratic_coefficients = results['options']['quadratic']['constants']
        quadratic_error = results['options']['quadratic']['error']
        cubic_coefficients = results['options']['cubic']['constants']
        cubic_error = results['options']['cubic']['error']
        hyperbolic_coefficients = results['options']['hyperbolic']['constants']
        hyperbolic_error = results['options']['hyperbolic']['error']
        exponential_coefficients = results['options']['exponential']['constants']
        exponential_error = results['options']['exponential']['error']
        logarithmic_coefficients = results['options']['logarithmic']['constants']
        logarithmic_error = results['options']['logarithmic']['error']
        best_fit = results['optimal']['function']
        new_regression = Regression(
            user_id=user_id,
            title=title,
            independent=independent,
            dependent=dependent,
            data_set=data_set,
            linear_coefficients=linear_coefficients,
            linear_error=linear_error,
            quadratic_coefficients=quadratic_coefficients,
            quadratic_error=quadratic_error,
            cubic_coefficients=cubic_coefficients,
            cubic_error=cubic_error,
            hyperbolic_coefficients=hyperbolic_coefficients,
            hyperbolic_error=hyperbolic_error,
            exponential_coefficients=exponential_coefficients,
            exponential_error=exponential_error,
            logarithmic_coefficients=logarithmic_coefficients,
            logarithmic_error=logarithmic_error,
            best_fit=best_fit,
            date=datetime.now()
        )
        db.session.add(new_regression)
        db.session.commit()
        return redirect(url_for('index'))
    if request.method == 'GET':
        sent_id = request.args.get('id')
        found_regression = Regression.query.filter_by(id=sent_id).first()
        return found_regression