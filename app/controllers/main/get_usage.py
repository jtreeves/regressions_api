from flask import render_template

def get_usage():
    return render_template('pages/usage.html'), 200