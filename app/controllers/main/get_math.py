from flask import render_template

def get_math():
    return render_template('pages/math.html'), 200