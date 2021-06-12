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

        validation = signup.validate_email(
            self, 
            other_user_email
        )

        assert validation == None
    
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
    def test_creates_blank_signup_form(self, app):
        with app.app_context():
            with app.test_request_context(
                '/signup'
            ):
                blank_form = signup(key = 'ABC123')
                name_object = vars(blank_form)['_fields']['name']
                email_object = vars(blank_form)['_fields']['email']
                key_object = vars(blank_form)['_fields']['key']
                assert 'input id="name" name="name" required type="text"' in str(name_object)
                assert 'input id="email" name="email" required type="text"' in str(email_object)
                assert 'input id="key" name="key" required type="hidden"' in str(key_object)
                assert name_object.data == None
                assert email_object.data == None
                assert key_object.data == 'ABC123'