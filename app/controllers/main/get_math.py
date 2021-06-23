from flask import render_template

def get_math():
    """ Render Math page, and provide status code """
    return render_template('pages/math.html'), 200