from app.models import Regression

def find_regression(user_id, source):
    """ Search database for an existing collection of regression models by its user_id and source """

    # Proceed if source provided
    if source:
        # Search database
        found_regression = Regression.query.filter_by(
            user_id = user_id, 
            source = source
        ).first()

        # Return collection if found
        if found_regression:
            return found_regression
        
        # Return false if not found
        else:
            return False
    
    # Return error code if source not provided
    else:
        return 'Source must be provided', 403