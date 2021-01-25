from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import User
from app.forms import SignUpForm
from .middleware.generator import generator
from .middleware.available import available
from datetime import datetime
from werkzeug.security import generate_password_hash as key_hash
from .middleware.decorators import require_apikey

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
            user = User(name=form.name.data, email=form.email.data, key=key_hash(form.key.data), date=datetime.now())
            db.session.add(user)
            db.session.commit()
            flash(f'API Key for user {form.key.data}')
            return redirect(url_for('index'))
        return render_template('signup.html', form=form)
    else:
        return signup()

@app.route('/api', methods=['GET', 'POST'])
@require_apikey
def get_phrase():
    return 'You have used the key correctly!'