from app.utilities.request_query import request_query
from app.utilities.request_submission import request_submission
from app.services.regressions.update_regression import update_regression

def put_regression():
    """ Update existing collection of regression models, and provide status code """
    query = request_query()
    submission = request_submission()

    # Pass data into function after vetting
    if not isinstance(submission, tuple):
        changed_regression = update_regression(
            query['user_id'], 
            query['source'], 
            submission
        )

        # Return 200 on success
        if not isinstance(changed_regression, tuple):
            return changed_regression, 200
        
        # Return error code if could not update
        else:
            return changed_regression
    
    # Return error code if problem with submissio
    else:
        return submission