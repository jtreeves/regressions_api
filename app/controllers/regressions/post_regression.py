from app.utilities.request_query import request_query
from app.utilities.request_submission import request_submission
from app.services.regressions.create_regression import create_regression

def post_regression():
    """ Create new collection of regression models, and provide status code """
    query = request_query()
    submission = request_submission()

    # Pass data into function after vetting
    if not isinstance(submission, tuple):
        new_regression = create_regression(
            query['user_id'], 
            query['source'], 
            submission
        )

        # Return 201 on success
        if not isinstance(new_regression, tuple):
            return new_regression, 201
        
        # Return error code if could not create
        else:
            return new_regression
    
    # Return error code if problem with submission
    else:
        return submission