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
    def test_creates_regression_full(self):
        new_regression = Regression(
            user_id = 1,
            source = 'TESTSOURCE',
            title = 'Test Title',
            independent = 'Test Independent',
            dependent = 'Test Dependent',
            precision = 4,
            data_set = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],
            linear_coefficients = [2, 3],
            linear_points = {'roots': [[1, 0]], 'inflections': [None]},
            linear_correlation = 0.5,
            quadratic_coefficients = [2, 3, 5],
            quadratic_points = {'roots': [[1, 0], [10, 0]], 'maxima': [[3, 57]]},
            quadratic_correlation = 0.5,
            cubic_coefficients = [2, 3, 5, 7],
            cubic_points = {'roots': [[1, 0], [5, 0], [10, 0]], 'maxima': [[3, 57]]},
            cubic_correlation = 0.5,
            hyperbolic_coefficients = [2, 3],
            hyperbolic_points = {'roots': [[1, 0]], 'maxima': [None]},
            hyperbolic_correlation = 0.5,
            exponential_coefficients = [2, 3],
            exponential_points = {'roots': [None], 'maxima': [None]},
            exponential_correlation = 0.5,
            logarithmic_coefficients = [2, 3],
            logarithmic_points = {'roots': [[1, 0]], 'maxima': [None]},
            logarithmic_correlation = 0.5,
            logistic_coefficients = [2, 3, 5],
            logistic_points = {'roots': [None], 'inflections': [[5, 7]]},
            logistic_correlation = 0.5,
            sinusoidal_coefficients = [2, 3, 5, 7],
            sinusoidal_points = {'roots': [[2, 0], [4, 0]], 'inflections': [[5, 7], [7, 7]]},
            sinusoidal_correlation = 0.5,
            best_fit = 'hyperbolic',
            date = datetime.now()
        )
        
        db.session.add(new_regression)
        db.session.commit()

        found_regression = Regression.query.filter_by(
            source = 'TESTSOURCE'
        ).first()

        assert hasattr(found_regression, 'id')
        assert found_regression.title == 'Test Title'

        db.session.delete(found_regression)
        db.session.commit()

    def test_fails_create_regression_no_source(self):
        with pytest.raises(Exception) as exception_info:
            new_regression = Regression(
                user_id = 1,
                title = 'Test Title',
                independent = 'Test Independent',
                dependent = 'Test Dependent',
                precision = 4,
                data_set = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            )
            
            db.session.add(new_regression)
            db.session.commit()

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "source" of relation "regressions" violates not-null constraint' in str(exception_info.value)

        db.session.close()

    def test_fails_create_regression_no_title(self):
        with pytest.raises(Exception) as exception_info:
            new_regression = Regression(
                user_id = 1,
                source = 'TESTSOURCE',
                independent = 'Test Independent',
                dependent = 'Test Dependent',
                precision = 4,
                data_set = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            )
            
            db.session.add(new_regression)
            db.session.commit()

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "title" of relation "regressions" violates not-null constraint' in str(exception_info.value)

        db.session.close()

    def test_fails_create_regression_no_independent(self):
        with pytest.raises(Exception) as exception_info:
            new_regression = Regression(
                user_id = 1,
                source = 'TESTSOURCE',
                title = 'Test Title',
                dependent = 'Test Dependent',
                precision = 4,
                data_set = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            )
            
            db.session.add(new_regression)
            db.session.commit()

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "independent" of relation "regressions" violates not-null constraint' in str(exception_info.value)

        db.session.close()

    def test_fails_create_regression_no_dependent(self):
        with pytest.raises(Exception) as exception_info:
            new_regression = Regression(
                user_id = 1,
                source = 'TESTSOURCE',
                title = 'Test Title',
                independent = 'Test Independent',
                precision = 4,
                data_set = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            )
            
            db.session.add(new_regression)
            db.session.commit()

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "dependent" of relation "regressions" violates not-null constraint' in str(exception_info.value)

        db.session.close()

    def test_fails_create_regression_no_precision(self):
        with pytest.raises(Exception) as exception_info:
            new_regression = Regression(
                user_id = 1,
                source = 'TESTSOURCE',
                title = 'Test Title',
                independent = 'Test Independent',
                dependent = 'Test Dependent',
                data_set = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            )
            
            db.session.add(new_regression)
            db.session.commit()

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "precision" of relation "regressions" violates not-null constraint' in str(exception_info.value)

        db.session.close()

    def test_fails_create_regression_no_data_set(self):
        with pytest.raises(Exception) as exception_info:
            new_regression = Regression(
                user_id = 1,
                source = 'TESTSOURCE',
                title = 'Test Title',
                independent = 'Test Independent',
                dependent = 'Test Dependent',
                precision = 4
            )
            
            db.session.add(new_regression)
            db.session.commit()

        assert 'IntegrityError' in str(exception_info.type)
        assert 'null value in column "data_set" of relation "regressions" violates not-null constraint' in str(exception_info.value)

        db.session.close()