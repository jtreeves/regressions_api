from flask import request

def request_submission():
    submission = {
        'title': request.json.get('title'),
        'independent': request.json.get('independent'),
        'dependent': request.json.get('dependent'),
        'data_set': request.json.get('data_set'),
        'precision': request.json.get('precision')
    }

    if submission['title'] and submission['independent'] and submission['dependent'] and submission['data_set'] and submission['precision']:
        return submission
    
    else:
        return 'Title, independent, dependent, data set, and precision fields must all be provided', 403