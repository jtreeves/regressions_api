from app.utilities.request_query import request_query
from app.utilities.request_submission import request_submission
from app.services.regressions.create_regression import create_regression

def post_regression():
    query = request_query()
    submission = request_submission()

    return create_regression(
        query['user_id'], 
        query['source'], 
        submission
    ), 201