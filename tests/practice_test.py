from app import app, db
from app.models import User
from datetime import datetime

# from flask import render_template, flash, redirect, url_for, request
# from datetime import datetime
# from app.models import User, Regression
# from app.forms import SignUpForm
# from regressions.execute import run_all
# from .middleware.generator import generator
# from .middleware.available import available
# from .middleware.decorators import require_apikey
# from .middleware.current import current_user, current_regression

def test_create_user():
    new_user = User(
        name='Michael',
        email='michael@email.com',
        key='ABC123',
        date=datetime.now()
    )
    db.session.add(new_user)
    db.session.commit()

    assert new_user.name == 'Michael'
    assert new_user.email == 'michael@email.com'
    assert new_user.key == 'ABC123'

def incrementing(num):
    return num + 1

def test_incrementing():
    assert incrementing(3) == 5

def decrementing(num):
    return num - 1

def test_decrementing():
    assert decrementing(3) == 1