from flask import render_template

def get_usage():
    """ Render Usage page, and provide status code """
    return render_template('pages/usage.html'), 200