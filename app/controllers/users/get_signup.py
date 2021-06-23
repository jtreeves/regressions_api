from flask import render_template

def get_signup(form):
    """ Render Signup page with empty form, and provide status code """
    return render_template(
        'pages/signup.html', 
        form = form
    ), 200