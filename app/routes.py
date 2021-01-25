from flask import render_template
from app import app
from app.forms import SignUpForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html', form=SignUpForm())