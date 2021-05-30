from flask import request

def request_submission():
    submission = {
        'title': request.json.get('title'),
        'independent': request.json.get('independent'),
        'dependent': request.json.get('dependent'),
        'data_set': request.json.get('data_set'),
        'precision': request.json.get('precision')
    }

    return submission