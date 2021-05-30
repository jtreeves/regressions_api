from app.models import User

def read_user(key):
    found_user = User.query.filter_by(
        key = key
    ).first()
    
    user_data = {
        'id': found_user.id,
        'name': found_user.name,
        'email': found_user.email,
        'key': found_user.key,
        'date': found_user.date
    }

    return user_data