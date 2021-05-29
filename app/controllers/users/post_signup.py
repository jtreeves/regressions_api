from flask import render_template
from datetime import datetime
from app import db
from app.models import User

def post_signup(form):
    if form.validate_on_submit():
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            key=form.key.data,
            date=datetime.now()
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template(
            'key.html', 
            key = form.key.data
        )