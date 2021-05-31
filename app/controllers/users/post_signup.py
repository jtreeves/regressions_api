from flask import render_template
from app.services.users.create_user import create_user

def post_signup(form):
    if form.validate_on_submit():
        key = create_user(form)
        
        return render_template(
            'signup.html', 
            key = key
        ), 201
    
    else:
        return render_template(
            'signup.html', 
            error = 'Email already in use'
        ), 409