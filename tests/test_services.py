import pytest
from datetime import datetime
from app import db
from app.models import User
from app.services.users.create_user import create_user
from app.services.users.read_user import read_user
from app.services.regressions.create_regression import create_regression
from app.services.regressions.find_regression import find_regression
from app.services.regressions.read_regression import read_regression
from app.services.regressions.update_regression import update_regression
from app.services.regressions.destroy_regression import destroy_regression

class TestCreateUserService:
    def test_creates_user_form_filled(self):
        class Form(object):
            pass
        class Field(object):
            pass
        
        new_form = Form()
        new_form.name = Field()
        new_form.email = Field()
        new_form.key = Field()
        new_form.name.data = 'Test Create User Service Success'
        new_form.email.data = 'test_create_user_service_success@email.com'
        new_form.key.data = 'ABC123'
        
        user_key = create_user(new_form)
        assert user_key == 'ABC123'

        found_user = User.query.filter_by(
            email = 'test_create_user_service_success@email.com'
        ).first()
        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_user_form_no_name(self):
        class Form(object):
            pass
        class Field(object):
            pass
        
        new_form = Form()
        new_form.name = Field()
        new_form.email = Field()
        new_form.key = Field()
        new_form.name.data = None
        new_form.email.data = 'test_fail_form_no_name@email.com'
        new_form.key.data = 'ABC123'

        with pytest.raises(Exception) as exception_info:
            create_user(new_form)

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "name" of relation "users" violates not-null constraint' in str(exception_info.value)

        db.session.close()
    
    def test_fails_create_user_form_no_email(self):
        class Form(object):
            pass
        class Field(object):
            pass
        
        new_form = Form()
        new_form.name = Field()
        new_form.email = Field()
        new_form.key = Field()
        new_form.name.data = 'Test Fail without Email'
        new_form.email.data = None
        new_form.key.data = 'ABC123'

        with pytest.raises(Exception) as exception_info:
            create_user(new_form)

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "email" of relation "users" violates not-null constraint' in str(exception_info.value)

        db.session.close()

class TestReadUserService:
    def test_read_user_exists(self):
        user_input = {
            'name': 'Test Read User Exists',
            'email': 'test_read_user_exists@email.com',
            'key': 'XYZ321'
        }

        new_user = User(
            name = user_input['name'],
            email = user_input['email'],
            key = user_input['key'],
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user_data = read_user(user_input['key'])
        assert found_user_data['name'] == user_input['name']
        assert found_user_data['email'] == user_input['email']
        assert found_user_data['key'] == user_input['key']
        assert 'id' in found_user_data.keys()
        assert 'date' in found_user_data.keys()

        found_user = User.query.filter_by(
            email = user_input['email']
        ).first()
        
        db.session.delete(found_user)
        db.session.commit()
    
    def test_read_user_nonexistent(self):
        found_user_data = read_user('PQR456')
        assert found_user_data == False

class TestCreateRegressionService:
    pass

class TestFindRegressionService:
    pass

class TestReadRegressionService:
    pass

class TestUpdateRegressionService:
    pass

class TestDestroyRegressionService:
    pass