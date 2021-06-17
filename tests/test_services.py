import pytest
from datetime import datetime
from app import db
from app.models import User, Regression
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
    def test_create_regression_success(self):
        submission = {
            'title': 'Test Create Regression Success Title',
            'independent': 'Test Create Regression Success Independent',
            'dependent': 'Test Create Regression Success Dependent',
            'precision': 4,
            'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
        }

        new_user = User(
            name = 'Test Create Regression Success',
            email = 'test_create_regression_success@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_success@email.com'
        ).first()

        found_user_id = found_user.id

        regression_data = create_regression(found_user_id, 'TestCreateRegressionSuccessSource', submission)
        assert regression_data['title'] == submission['title']
        assert 'best_fit' in regression_data.keys()

        found_regression = Regression.query.filter_by(
            source = 'TestCreateRegressionSuccessSource'
        ).first()
        
        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_regression_decimal_precision(self):
        submission = {
            'title': 'Test Create Regression Fails Decimal Precision Title',
            'independent': 'Test Create Regression Fails Decimal Precision Independent',
            'dependent': 'Test Create Regression Fails Decimal Precision Dependent',
            'precision': 4.5,
            'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
        }

        new_user = User(
            name = 'Test Create Regression Fails Decimal Precision',
            email = 'test_create_regression_fails_decimal_precision@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_fails_decimal_precision@email.com'
        ).first()

        found_user_id = found_user.id

        regression_data = create_regression(found_user_id, 'TestCreateRegressionFailsDecimalPrecisionSource', submission)
        assert regression_data[0] == 'Precision must be a positive integer'
        assert regression_data[1] == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_regression_negative_precision(self):
        submission = {
            'title': 'Test Create Regression Fails Negative Precision Title',
            'independent': 'Test Create Regression Fails Negative Precision Independent',
            'dependent': 'Test Create Regression Fails Negative Precision Dependent',
            'precision': -4,
            'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
        }

        new_user = User(
            name = 'Test Create Regression Fails Negative Precision',
            email = 'test_create_regression_fails_negative_precision@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_fails_negative_precision@email.com'
        ).first()

        found_user_id = found_user.id

        regression_data = create_regression(found_user_id, 'TestCreateRegressionFailsNegativePrecisionSource', submission)
        assert regression_data[0] == 'Precision must be a positive integer'
        assert regression_data[1] == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_regression_short_data_set(self):
        submission = {
            'title': 'Test Create Regression Fails Short Data Set Title',
            'independent': 'Test Create Regression Fails Short Data Set Independent',
            'dependent': 'Test Create Regression Fails Short Data Set Dependent',
            'precision': 4,
            'data_set': [[1, 2], [3, 4], [5, 6]]
        }

        new_user = User(
            name = 'Test Create Regression Fails Short Data Set',
            email = 'test_create_regression_fails_short_data_set@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_fails_short_data_set@email.com'
        ).first()

        found_user_id = found_user.id

        regression_data = create_regression(found_user_id, 'TestCreateRegressionFailsShortDataSetSource', submission)
        assert regression_data[0] == 'Data set must contain at least 10 points'
        assert regression_data[1] == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_regression_nonlist_data_set(self):
        submission = {
            'title': 'Test Create Regression Fails Nonlist Data Set Title',
            'independent': 'Test Create Regression Fails Nonlist Data Set Independent',
            'dependent': 'Test Create Regression Fails Nonlist Data Set Dependent',
            'precision': 4,
            'data_set': {
                'first_point': [1, 2],
                'second_point': [3, 4],
                'third_point': [5, 6]
            }
        }

        new_user = User(
            name = 'Test Create Regression Fails Nonlist Data Set',
            email = 'test_create_regression_fails_nonlist_data_set@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_fails_nonlist_data_set@email.com'
        ).first()

        found_user_id = found_user.id

        regression_data = create_regression(found_user_id, 'TestCreateRegressionFailsNonlistDataSetSource', submission)
        assert regression_data[0] == 'Data set must be a list'
        assert regression_data[1] == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_regression_nonlist_points(self):
        submission = {
            'title': 'Test Create Regression Fails Nonlist Points Title',
            'independent': 'Test Create Regression Fails Nonlist Points Independent',
            'dependent': 'Test Create Regression Fails Nonlist Points Dependent',
            'precision': 4,
            'data_set': [
                {'x': 1, 'y': 2},
                {'x': 3, 'y': 4},
                {'x': 5, 'y': 6}
            ]
        }

        new_user = User(
            name = 'Test Create Regression Fails Nonlist Points',
            email = 'test_create_regression_fails_nonlist_points@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_fails_nonlist_points@email.com'
        ).first()

        found_user_id = found_user.id

        regression_data = create_regression(found_user_id, 'TestCreateRegressionFailsNonlistPointsSource', submission)
        assert regression_data[0] == 'Each coordinate pair within data set must be a list'
        assert regression_data[1] == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_regression_long_points(self):
        submission = {
            'title': 'Test Create Regression Fails Long Points Title',
            'independent': 'Test Create Regression Fails Long Points Independent',
            'dependent': 'Test Create Regression Fails Long Points Dependent',
            'precision': 4,
            'data_set': [
                [1, 2, 3],
                [4, 5, 6]
            ]
        }

        new_user = User(
            name = 'Test Create Regression Fails Long Points',
            email = 'test_create_regression_fails_long_points@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_fails_long_points@email.com'
        ).first()

        found_user_id = found_user.id

        regression_data = create_regression(found_user_id, 'TestCreateRegressionFailsLongPointsSource', submission)
        assert regression_data[0] == 'Each coordinate pair within data set must contain exactly 2 numbers'
        assert regression_data[1] == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_regression_string_numbers(self):
        submission = {
            'title': 'Test Create Regression Fails String Numbers Title',
            'independent': 'Test Create Regression Fails String Numbers Independent',
            'dependent': 'Test Create Regression Fails String Numbers Dependent',
            'precision': 4,
            'data_set': [
                [1, 2],
                ['3', 4],
                [5, 6]
            ]
        }

        new_user = User(
            name = 'Test Create Regression Fails String Numbers',
            email = 'test_create_regression_fails_string_numbers@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_fails_string_numbers@email.com'
        ).first()

        found_user_id = found_user.id

        regression_data = create_regression(found_user_id, 'TestCreateRegressionFailsStringNumbersSource', submission)
        assert regression_data[0] == 'All numbers within coordinate pairs within data set must be integers or floats'
        assert regression_data[1] == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_regression_without_source(self):
        submission = {
            'title': 'Test Create Regression Fails without Source Title',
            'independent': 'Test Create Regression Fails without Source Independent',
            'dependent': 'Test Create Regression Fails without Source Dependent',
            'precision': 4,
            'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
        }

        new_user = User(
            name = 'Test Create Regression Fails without Source',
            email = 'test_create_regression_fails_without_source@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_fails_without_source@email.com'
        ).first()

        found_user_id = found_user.id

        regression_data = create_regression(found_user_id, '', submission)
        assert regression_data[0] == 'Source must be provided'
        assert regression_data[1] == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_create_regression_reserved_source(self):
        submission = {
            'title': 'Test Create Regression Fails Reserved Source Title',
            'independent': 'Test Create Regression Fails Reserved Source Independent',
            'dependent': 'Test Create Regression Fails Reserved Source Dependent',
            'precision': 4,
            'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
        }

        new_user = User(
            name = 'Test Create Regression Fails Reserved Source',
            email = 'test_create_regression_fails_reserved_source@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_create_regression_fails_reserved_source@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPostSourceTaken',
            title = 'Test Post Source Taken Title',
            independent = 'Test Post Source Taken Independent',
            dependent = 'Test Post Source Taken Dependent',
            precision = 4,
            data_set = [[1, 2], [3, 4], [5, 6]],
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
            user_id = found_user_id, 
            source = 'TestPostSourceTaken'
        ).first()

        regression_data = create_regression(found_user_id, 'TestPostSourceTaken', submission)
        assert regression_data[0] == 'Source already in use by other collection'
        assert regression_data[1] == 409

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

class TestFindRegressionService:
    def test_find_regression_success(self):
        new_user = User(
            name = 'Test Find Regression Success',
            email = 'test_find_regression_success@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_find_regression_success@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestFindRegressionSuccessSource',
            title = 'Test Find Regression Success Title',
            independent = 'Test Find Regression Success Independent',
            dependent = 'Test Find Regression Success Dependent',
            precision = 4,
            data_set = [[1, 2], [3, 4], [5, 6]],
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
            user_id = found_user_id, 
            source = 'TestFindRegressionSuccessSource'
        ).first()

        found_regression_from_service = find_regression(found_user_id, 'TestFindRegressionSuccessSource')
        assert found_regression_from_service == found_regression

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_find_regression_nonexistent(self):
        new_user = User(
            name = 'Test Find Regression Fails Nonexistent',
            email = 'test_find_regression_fails_nonexistent@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_find_regression_fails_nonexistent@email.com'
        ).first()

        found_user_id = found_user.id

        found_regression = find_regression(found_user_id, 'TestFindRegressionFailsNonexistentSource')
        assert not found_regression

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_find_regression_without_source(self):
        new_user = User(
            name = 'Test Find Regression Fails without Source',
            email = 'test_find_regression_fails_without_source@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_find_regression_fails_without_source@email.com'
        ).first()

        found_user_id = found_user.id

        found_regression = find_regression(found_user_id, '')
        assert found_regression[0] == 'Source must be provided'
        assert found_regression[1] == 403

        db.session.delete(found_user)
        db.session.commit()

class TestReadRegressionService:
    def test_read_regression_success(self):
        new_user = User(
            name = 'Test Read Regression Success',
            email = 'test_read_regression_success@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_read_regression_success@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestReadRegressionSuccessSource',
            title = 'Test Read Regression Success Title',
            independent = 'Test Read Regression Success Independent',
            dependent = 'Test Read Regression Success Dependent',
            precision = 4,
            data_set = [[1, 2], [3, 4], [5, 6]],
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
            user_id = found_user_id, 
            source = 'TestReadRegressionSuccessSource'
        ).first()

        regression_analysis = read_regression(found_user_id, 'TestReadRegressionSuccessSource')
        assert regression_analysis['source'] == 'TestReadRegressionSuccessSource'
        assert regression_analysis['title'] == 'Test Read Regression Success Title'
        assert 'best_fit' in regression_analysis.keys()

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_read_regression_without_source(self):
        new_user = User(
            name = 'Test Read Regression Success',
            email = 'test_read_regression_success@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_read_regression_success@email.com'
        ).first()

        found_user_id = found_user.id

        regression_analysis = read_regression(found_user_id, '')
        assert regression_analysis[0] == 'Source must be provided'
        assert regression_analysis[1] == 403

        db.session.delete(found_user)
        db.session.commit()
    
    def test_fails_read_regression_nonexistent_source(self):
        new_user = User(
            name = 'Test Read Regression Success',
            email = 'test_read_regression_success@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_read_regression_success@email.com'
        ).first()

        found_user_id = found_user.id

        regression_analysis = read_regression(found_user_id, 'potato')
        assert regression_analysis[0] == 'Data set not found'
        assert regression_analysis[1] == 404

        db.session.delete(found_user)
        db.session.commit()

class TestUpdateRegressionService:
    def test_update_regression_success(self):
        submission = {
            'title': 'Test Update Regression Success New Title',
            'independent': 'Test Update Regression Success New Independent',
            'dependent': 'Test Update Regression Success New Dependent',
            'precision': 4,
            'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
        }

        new_user = User(
            name = 'Test Update Regression Success',
            email = 'test_update_regression_success@email.com',
            key = 'VWU987',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'test_update_regression_success@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestUpdateRegressionSuccessSource',
            title = 'Test Update Regression Success Title',
            independent = 'Test Update Regression Success Independent',
            dependent = 'Test Update Regression Success Dependent',
            precision = 4,
            data_set = [[1, 2], [3, 4], [5, 6]],
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
            user_id = found_user_id, 
            source = 'TestUpdateRegressionSuccessSource'
        ).first()

        regression_analysis = update_regression(found_user_id, 'TestUpdateRegressionSuccessSource', submission)
        assert regression_analysis['title'] == 'Test Update Regression Success New Title'
        assert regression_analysis['best_fit'] != 'hyperbolic'
        
        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

class TestDestroyRegressionService:
    pass