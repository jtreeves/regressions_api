from flask import render_template

def get_home():
    return render_template('pages/home.html'), 200