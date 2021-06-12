import pytest
# import asyncio

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
                assert 'input id="email" name="email" required type="text"' in str(email)
                assert 'input id="key" name="key" required type="hidden"' in str(key)
                assert 'input id="submit" name="submit" type="submit" value="Submit"' in str(submit)
                assert name.data == None
                assert email.data == None
                assert key.data == 'ABC123'
                assert submit.data == False
    
    # @pytest.mark.asyncio
    def test_submit_validates_new_signup_form(self, app, client):
        # new_form = None

        @app.route("/form", methods=["POST"])
        def form_route():
            app.config['WTF_CSRF_ENABLED'] = False
            new_form = signup(
                name = 'unique',
                email = 'unique@email.com',
                key = 'ABC123'
            )
            print('NEW FORM: ', new_form)
            print('NEW FORM KEYS: ', dir(new_form))
            print('NEW FORM VALIDATE ON SUBMIT: ', new_form.validate_on_submit())
            # assert new_form.is_submitted()
            # assert new_form.validate_on_submit()
            # assert 1 == 2
            return_object = {
                'submitted': new_form.is_submitted(),
                'validated': new_form.validate_on_submit()
            }
            return return_object

        res = client.post("/form")
        decoded_res = json.loads(res.data.decode())
        print('DECODED_RES: ', decoded_res)
        submitted = decoded_res['submitted']
        validated = decoded_res['validated']
        # print('SUBMITTED: ', submitted)

        # print('NEW FORM TOP LEVEL: ', new_form)
        # print('NEW FORM TOP LEVEL VALIDATE: ', new_form.validate_on_submit())

        # print('RES: ', res)
        # print('RES KEYS: ', dir(res))
        # print('RES.DATA: ', res.data)
        # print('DECODED RES.DATA: ', json.loads(res.data.decode()))
        # print('RES.__dict__: ', res.__dict__)
        # print('RES.RESPONSE: ', res.response)
        # print('RES.RESPONSE KEYS: ', dir(res.response))
        # print('RES.RESPONSE.__dict__: ', res.response.__dict__)
        # print('RES.DATA.VALIDATED: ', res.data.validated)

        # assert res.is_submitted()
        # assert res.validate_on_submit()

        assert 1 == 2

        # found_user = User.query.filter_by(
        #     email = 'unique@email.com'
        # ).first()

        # db.session.delete(found_user)
        # db.session.commit()
    
    # def test_submit_fails_validate_old_signup_form(self, app, client):
    #     new_user = User(
    #         name = 'test_submit',
    #         email = 'an@email.com',
    #         key = 'ABC123',
    #         date = datetime.now()
    #     )

    #     db.session.add(new_user)
    #     db.session.commit()

    #     @app.route("/otherform", methods=["POST"])
    #     def other_form_route():
    #         old_form = signup(
    #             name = 'test_submit',
    #             email = 'an@email.com',
    #             key = 'ABC123'
    #         )
    #         print('OLD FORM: ', old_form)
    #         print('OLD FORM KEYS: ', dir(old_form))
    #         assert old_form.is_submitted()
    #         assert not old_form.validate_on_submit()
    #         assert "email" in old_form.errors
    #         assert 1 == 2

    #     client.post("/otherform")

    #     found_user = User.query.filter_by(
    #         email = 'an@email.com'
    #     ).first()

    #     db.session.delete(found_user)
    #     db.session.commit()