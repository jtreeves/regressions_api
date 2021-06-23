from datetime import datetime
from app import db
from app.models import User

def create_user(form):
    """ Create new user from form data """

    # Pass form data into User model
    new_user = User(
        name = form.name.data,
        email = form.email.data,
        key = form.key.data,
        date = datetime.now()
    )

    # Add new user to database
    db.session.add(new_user)
    db.session.commit()
    
    # Return new user's key
    return form.key.data