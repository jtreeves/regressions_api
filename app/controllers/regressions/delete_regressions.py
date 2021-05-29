from app.middleware.current import current_user
from flask import request
from app import db
from app.models import Regression

def delete_regressions():
    user_id = current_user()['id']
    source = request.args.get('source')
    try:
        found_regression = Regression.query.filter_by(
            user_id=user_id, 
            source=source
        ).first()
        db.session.delete(found_regression)
        db.session.commit()
        return 'Data set deleted', 204
    except Exception:
        return 'Data set not found', 404