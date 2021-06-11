import pytest
from datetime import datetime
from app import db
from app.models import User, Regression

class TestUserModel:
    def test_creates_user_full(self):
        new_user = User(
            name = 'test_user',
            email = 'test_user@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_user@email.com'
        ).first()

        assert hasattr(found_user, 'id')
        assert found_user.key == 'ABC123'

        db.session.delete(found_user)
        db.session.commit()

    def test_fails_create_user_no_email(self):
        with pytest.raises(Exception) as exception_info:
            new_user = User(
                name='test_fail_user'
            )

            db.session.add(new_user)
            db.session.commit() 

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "email" of relation "users" violates not-null constraint' in str(exception_info.value)

        db.session.close()
    def test_fails_create_user_no_name(self):
        with pytest.raises(Exception) as exception_info:
            new_user = User(
                email='test_fail_user@email.com'
            )

            db.session.add(new_user)
            db.session.commit() 

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "name" of relation "users" violates not-null constraint' in str(exception_info.value)

        db.session.close()

class TestRegressionModel:
    pass