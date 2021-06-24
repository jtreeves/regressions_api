import pytest
import json
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
                assert 'input id="email" name="email" required type="email"' in str(email)
                assert 'input id="key" name="key" required type="hidden"' in str(key)
                assert 'input id="submit" name="submit" type="submit" value="Submit"' in str(submit)
                assert name.data == None
                assert email.data == None
                assert key.data == 'ABC123'
                assert submit.data == False

    def test_submit_validates_new_signup_form(self, app, client):
        @app.route("/new_form", methods=["POST"])
        def new_form_route():
            app.config['WTF_CSRF_ENABLED'] = False
            new_form = signup(
                name = 'unique',
                email = 'unique@email.com',
                key = 'ABC123'
            )
            new_form_statuses = {
                'submitted': new_form.is_submitted(),
                'validated': new_form.validate_on_submit()
            }
            return new_form_statuses

        res = client.post("/new_form")
        res_statuses = json.loads(res.data.decode())
        assert res_statuses['submitted']
        assert res_statuses['validated']
    
    def test_submit_fails_validate_empty_signup_form(self, app, client):
        @app.route("/empty_form", methods=["POST"])
        def empty_form_route():
            app.config['WTF_CSRF_ENABLED'] = False
            empty_form = signup()
            empty_form_statuses = {
                'submitted': empty_form.is_submitted(),
                'validated': empty_form.validate_on_submit(),
                'errors': empty_form.errors
            }
            return empty_form_statuses

        res = client.post("/empty_form")
        res_statuses = json.loads(res.data.decode())
        assert res_statuses['submitted']
        assert not res_statuses['validated']
        assert 'This field is required.' in res_statuses['errors']['name']
        assert 'This field is required.' in res_statuses['errors']['email']
        assert 'This field is required.' in res_statuses['errors']['key']
    
    def test_submit_fails_validate_partial_signup_form(self, app, client):
        @app.route("/partial_form", methods=["POST"])
        def partial_form_route():
            app.config['WTF_CSRF_ENABLED'] = False
            partial_form = signup(
                email = 'partial@email.com'
            )
            partial_form_statuses = {
                'submitted': partial_form.is_submitted(),
                'validated': partial_form.validate_on_submit(),
                'errors': partial_form.errors
            }
            return partial_form_statuses

        res = client.post("/partial_form")
        res_statuses = json.loads(res.data.decode())
        assert res_statuses['submitted']
        assert not res_statuses['validated']
        assert 'This field is required.' in res_statuses['errors']['name']
        assert 'email' not in res_statuses['errors']
    
    def test_submit_fails_validate_improper_email_signup_form(self, app, client):
        @app.route("/improper_email_form", methods=["POST"])
        def improper_email_form_route():
            app.config['WTF_CSRF_ENABLED'] = False
            improper_email_form = signup(
                name = 'bad email',
                email = 'improper',
                key = 'ABC123'
            )
            improper_email_form_statuses = {
                'submitted': improper_email_form.is_submitted(),
                'validated': improper_email_form.validate_on_submit(),
                'errors': improper_email_form.errors
            }
            return improper_email_form_statuses

        res = client.post("/improper_email_form")
        res_statuses = json.loads(res.data.decode())
        assert res_statuses['submitted']
        assert not res_statuses['validated']
        assert 'Invalid email address.' in res_statuses['errors']['email']
    
    def test_submit_fails_validate_old_signup_form(self, app, client):
        new_user = User(
            name = 'test_submit',
            email = 'an@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        @app.route("/old_form", methods=["POST"])
        def old_form_route():
            old_form = signup(
                name = 'test_submit',
                email = 'an@email.com',
                key = 'ABC123'
            )
            old_form_statuses = {
                'submitted': old_form.is_submitted(),
                'validated': old_form.validate_on_submit(),
                'errors': old_form.errors
            }
            return old_form_statuses

        res = client.post("/old_form")
        res_statuses = json.loads(res.data.decode())
        assert res_statuses['submitted']
        assert not res_statuses['validated']
        assert "email" in res_statuses['errors']

        found_user = User.query.filter_by(
            email = 'an@email.com'
        ).first()

        db.session.delete(found_user)
        db.session.commit()