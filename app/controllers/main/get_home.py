from flask import render_template

def get_home():
    """ Render Home page, and provide status code """
    return render_template('pages/home.html'), 200