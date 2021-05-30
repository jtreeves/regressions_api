from datetime import datetime
from app import db
from app.models import User

def create_user(form):
    new_user = User(
        name = form.name.data,
        email = form.email.data,
        key = form.key.data,
        date = datetime.now()
    )

    db.session.add(new_user)
    db.session.commit()
    
    return form.key.data