from flask import render_template

def get_about():
    return render_template('about.html'), 200