from flask import request

def request_submission():
    """ Store submission from request """

    # Grab JSON elements from body of request, and store them in dictionary
    submission = {
        'title': request.json.get('title'),
        'independent': request.json.get('independent'),
        'dependent': request.json.get('dependent'),
        'data_set': request.json.get('data_set'),
        'precision': request.json.get('precision')
    }

    # Return dictionary if all keys contain nonempty values
    if submission['title'] and submission['independent'] and submission['dependent'] and submission['data_set'] and submission['precision']:
        return submission
    
    # Return error code if any key contains an empty value
    else:
        return 'Title, independent, dependent, data set, and precision fields must all be provided', 403