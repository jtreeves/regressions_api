from flask import render_template

def get_signup(form):
    return render_template(
        'signup.html', 
        form = form
    )