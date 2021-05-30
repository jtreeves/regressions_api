from app.utilities.request_query import request_query
from app.services.regressions.read_regression import read_regression

def get_regression():
    query = request_query()
    
    return read_regression(
        query['user_id'], 
        query['source']
    ), 200