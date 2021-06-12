import pytest
from datetime import datetime
from app import db
from app.models import User
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
                name = blank_form.name
                email = blank_form.email
                key = blank_form.key
                submit = blank_form.submit
                assert 'input id="name" name="name" required type="text"' in str(name)
                assert 'input id="email" name="email" required type="text"' in str(email)
                assert 'input id="key" name="key" required type="hidden"' in str(key)
                assert 'input id="submit" name="submit" type="submit" value="Submit"' in str(submit)
                assert name.data == None
                assert email.data == None
                assert key.data == 'ABC123'
                assert submit.data == False
    
    def test_submit_validates_new_signup_form(self, app, client):
        with app.app_context():
            with app.test_request_context(
                '/signup'
            ):
                new_form = signup(
                    name = 'unique',
                    email = 'unique@email.com',
                    key = 'ABC123',
                    submit = True
                )
                res = client.post('/signup')
                print('NEW FORM: ', new_form)
                print('KEYS IN NEW FORM: ', dir(new_form))
                print('INVOCATION OF VALIDATE ON SUBMIT: ', new_form.validate_on_submit())
                print('RES: ', res)
                print('KEYS IN RES: ', dir(res))
                print('RES.DATA: ', res.data)
                assert new_form.validate_on_submit() == True