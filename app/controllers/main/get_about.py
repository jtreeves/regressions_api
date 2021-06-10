from flask import render_template

def get_about():
    return render_template('pages/about.html'), 200