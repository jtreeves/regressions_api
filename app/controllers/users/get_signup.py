from flask import render_template

def get_signup(form):
    return render_template(
        'pages/signup.html', 
        form = form
    ), 200