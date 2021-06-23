from app import db
from .find_regression import find_regression

def destroy_regression(user_id, source):
    """ Delete an existing collection of regression models by its user_id and source """

    try:
        # Use helper function to search database for collection
        found_regression = find_regression(user_id, source)

        # Delete collection if found
        if not isinstance(found_regression, tuple):
            db.session.delete(found_regression)
            db.session.commit()
            
            return 'Data set deleted'
        
        # Return error code if source not provided
        else:
            return found_regression
    
    except Exception:
        # Return 404 if not found
        return 'Data set not found', 404