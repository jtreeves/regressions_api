from app.utilities.request_query import request_query
from app.services.regressions.read_regression import read_regression

def get_regression():
    """ Get existing collection of regression models, and provide status code """
    query = request_query()
    received_regression = read_regression(
        query['user_id'], 
        query['source']
    )
    
    # Return 200 on success
    if not isinstance(received_regression, tuple):
        return received_regression, 200
    
    # Return error code on failure
    else:
        return received_regression