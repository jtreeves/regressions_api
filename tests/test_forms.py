import pytest
from datetime import datetime
from app import db
from app.models import User, Regression
from app.forms import SignUpForm as signup

class TestValidateEmail:
    def test_validates_email_new(self):
        new_user = User(
            name = 'test_validate',
            email = 'an@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        class Email(object):
            pass

        other_user_email = Email()
        other_user_email.data = 'another@email.com'

        try:
            signup.validate_email(
                self, 
                other_user_email
            )
        
        except Exception as exception_info:
            assert False, exception_info

        found_user = User.query.filter_by(
            email = 'an@email.com'
        ).first()

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_validate_email_old(self):
        new_user = User(
            name = 'test_validate',
            email = 'an@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        class Email(object):
            pass

        same_user_email = Email()
        same_user_email.data = 'an@email.com'

        with pytest.raises(Exception) as exception_info:
            signup.validate_email(
                self, 
                same_user_email
            )

        assert 'ValidationError' in str(exception_info.type)

        found_user = User.query.filter_by(
            email = 'an@email.com'
        ).first()

        db.session.delete(found_user)
        db.session.commit()

class TestSignUpForm:
    pass