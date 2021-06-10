from app.utilities.request_query import request_query
from app.services.regressions.read_regression import read_regression

def get_regression():
    query = request_query()
    received_regression = read_regression(
        query['user_id'], 
        query['source']
    )
    
    if not isinstance(received_regression, tuple):
        return received_regression, 200
    
    else:
        return received_regression