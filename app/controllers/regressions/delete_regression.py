from app.utilities.request_query import request_query
from app.services.regressions.destroy_regression import destroy_regression

def delete_regression():
    """ Delete existing collection of regression models, and provide status code """
    query = request_query()
    deletion = destroy_regression(
        query['user_id'], 
        query['source']
    )

    # Return 204 on success
    if not isinstance(deletion, tuple):
        return deletion, 204
    
    # Return error code on failure
    else:
        return deletion