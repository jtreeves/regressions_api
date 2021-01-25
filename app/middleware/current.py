from flask import request
from app.models import User

current = 'John'

# sent_key = request.args.get('key')
# current = User.query.filter_by(key=sent_key).first()