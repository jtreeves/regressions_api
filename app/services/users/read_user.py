from app.models import User

def read_user(key):
    """ Get information on an existing user by their key """

    # Find user in database by their key
    found_user = User.query.filter_by(
        key = key
    ).first()

    # Return user data if found
    if found_user:
        user_data = {
            'id': found_user.id,
            'name': found_user.name,
            'email': found_user.email,
            'key': found_user.key,
            'date': found_user.date
        }

        return user_data
    
    # Return false if user not found
    else:
        return False