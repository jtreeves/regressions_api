from app.models import Regression

def find_regression(user_id, source):
    if source:
        found_regression = Regression.query.filter_by(
            user_id = user_id, 
            source = source
        ).first()

        if found_regression:
            return found_regression
        
        else:
            return False
    
    else:
        return 'Source must be provided', 403