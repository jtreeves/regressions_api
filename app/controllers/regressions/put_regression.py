from app.utilities.request_query import request_query
from app.utilities.request_submission import request_submission
from app.services.regressions.update_regression import update_regression

def put_regression():
    query = request_query()
    submission = request_submission()

    return update_regression(
        query['user_id'], 
        query['source'], 
        submission
    ), 200