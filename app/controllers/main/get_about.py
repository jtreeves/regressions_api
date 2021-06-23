from flask import render_template

def get_about():
    """ Render About page, and provide status code """
    return render_template(
        'pages/about.html'
    ), 200