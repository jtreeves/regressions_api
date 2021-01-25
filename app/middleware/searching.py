from app.models import User

def searching(string):
    found_user = User.query.filter_by(key=string).first()
    if found_user:
        return True
    else:
        return False