from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SignUpForm
from .middleware.generator import generator

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(key=generator())
    if form.validate_on_submit():
        flash(f'API Key for user {form.key.data}')
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)