from app.utilities.request_query import request_query
from app.services.regressions.destroy_regression import destroy_regression

def delete_regression():
    query = request_query()
    deletion = destroy_regression(
        query['user_id'], 
        query['source']
    )

    if not isinstance(deletion, tuple):
        return deletion, 204
    
    else:
        return deletion