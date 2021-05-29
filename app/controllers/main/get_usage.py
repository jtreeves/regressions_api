from flask import render_template

def get_usage():
    return render_template('usage.html')