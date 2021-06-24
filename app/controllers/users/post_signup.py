from flask import render_template
from app.services.users.create_user import create_user

def post_signup(form):
    """ Render Signup page after form submitted, and provide status code """
    
    # Display key and return 201 on successful submission
    if form.validate_on_submit():
        key = create_user(form)
        
        return render_template(
            'pages/signup.html', 
            key = key
        ), 201
    
    # Display error message and return 409 on unsuccessful submission
    else:
        return render_template(
            'pages/signup.html', 
            error = 'Sorry, the email you provided is already in use!'
        ), 409