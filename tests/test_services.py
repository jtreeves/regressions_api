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

class TestReadUserService:
    pass

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