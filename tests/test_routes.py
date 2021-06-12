import json
from datetime import datetime
from app import db
from app.models import User, Regression

class TestHomeRoute:
    def test_home_loads_get(self, client):
        res = client.get('/')
        assert res.status_code == 200
    
    def test_home_fails_post(self, client):
        res = client.post('/')
        assert res.status_code == 405
    
    def test_home_fails_put(self, client):
        res = client.put('/')
        assert res.status_code == 405
    
    def test_home_fails_delete(self, client):
        res = client.delete('/')
        assert res.status_code == 405

class TestAboutRoute:
    def test_about_loads_get(self, client):
        res = client.get('/about')
        assert res.status_code == 200
    
    def test_about_fails_post(self, client):
        res = client.post('/about')
        assert res.status_code == 405
    
    def test_about_fails_put(self, client):
        res = client.put('/about')
        assert res.status_code == 405
    
    def test_about_fails_delete(self, client):
        res = client.delete('/about')
        assert res.status_code == 405

class TestUsageRoute:
    def test_usage_loads_get(self, client):
        res = client.get('/usage')
        assert res.status_code == 200
    
    def test_usage_fails_post(self, client):
        res = client.post('/usage')
        assert res.status_code == 405
    
    def test_usage_fails_put(self, client):
        res = client.put('/usage')
        assert res.status_code == 405
    
    def test_usage_fails_delete(self, client):
        res = client.delete('/usage')
        assert res.status_code == 405

class TestMathRoute:
    def test_math_loads_get(self, client):
        res = client.get('/math')
        assert res.status_code == 200
    
    def test_math_fails_post(self, client):
        res = client.post('/math')
        assert res.status_code == 405
    
    def test_math_fails_put(self, client):
        res = client.put('/math')
        assert res.status_code == 405
    
    def test_math_fails_delete(self, client):
        res = client.delete('/math')
        assert res.status_code == 405

class TestImagesRoute:
    def test_images_loads_get(self, client):
        res = client.get('/images/test')
        assert res.status_code == 200
    
    def test_images_fails_post(self, client):
        res = client.post('/images/test')
        assert res.status_code == 405
    
    def test_images_fails_put(self, client):
        res = client.put('/images/test')
        assert res.status_code == 405
    
    def test_images_fails_delete(self, client):
        res = client.delete('/images/test')
        assert res.status_code == 405

class TestSignupRoute:
    def test_signup_loads_get(self, client):
        res = client.get('/signup')
        assert res.status_code == 200
    
    def test_signup_loads_post(self, client):
        res = client.post(
            '/signup',
            data = {
                'name': 'test signup route',
                'email': 'testing_route@email.com',
                'key': 'ABC123'
            }
        )

        assert res.status_code == 201
        assert b'<h1>Key</h1>' in res.data
        assert b'ABC123' in res.data

        found_user = User.query.filter_by(
            email = 'testing_route@email.com'
        ).first()

        db.session.delete(found_user)
        db.session.commit()
    
    def test_signup_loads_error_post_old(self, client):
        new_user = User(
            name = 'test fail signup route',
            email = 'test_fail_signup_route@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        res = client.post(
            '/signup',
            data = {
                'name': 'test fail signup route',
                'email': 'test_fail_signup_route@email.com',
                'key': 'ABC123'
            }
        )

        assert res.status_code == 409
        assert b'<h1>Error</h1>' in res.data
        assert b'Email already in use' in res.data

        found_user = User.query.filter_by(
            email = 'test_fail_signup_route@email.com'
        ).first()

        db.session.delete(found_user)
        db.session.commit()
    
    def test_signup_fails_put(self, client):
        res = client.put('/signup')
        assert res.status_code == 405
    
    def test_signup_fails_delete(self, client):
        res = client.delete('/signup')
        assert res.status_code == 405

class TestAPIRoute:
    def test_api_returns_get(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestGetSource',
            title = 'Test Get Title',
            independent = 'Test Get Independent',
            dependent = 'Test Get Dependent',
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
            source = 'TestGetSource'
        ).first()

        res = client.get(
            '/api?key=ABC123&source=TestGetSource'
        )

        analysis = json.loads(res.data.decode())

        assert res.status_code == 200
        assert analysis['source'] == 'TestGetSource'
        assert analysis['title'] == 'Test Get Title'
        assert analysis['best_fit'] == 'hyperbolic'
        assert analysis['sinusoidal_correlation'] == 0.5

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()
    
    def test_api_fails_get_without_key(self, client):
        res = client.get('/api')
        assert res.status_code == 403
        assert b'Key must be provided' in res.data
    
    def test_api_fails_get_unfound_key(self, client):
        res = client.get('/api?key=ABC123')
        assert res.status_code == 401
        assert b'User not authenticated' in res.data
    
    def test_api_fails_get_without_source(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.get(
            '/api?key=ABC123'
        )

        assert res.status_code == 403
        assert b'Source must be provided' in res.data

        db.session.delete(found_user)
        db.session.commit()
    
    def test_api_fails_get_unfound_source(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.get(
            '/api?key=ABC123&source=NonexistentSource'
        )

        assert res.status_code == 404
        assert b'Data set not found' in res.data

        db.session.delete(found_user)
        db.session.commit()
    
    def test_api_returns_post(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        res = client.post(
            '/api?key=ABC123&source=TestPostSource',
            json = {
                'title': 'Test Post Title',
                'independent': 'Test Post Independent',
                'dependent': 'Test Post Dependent',
                'precision': 4,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        analysis = json.loads(res.data.decode())

        assert res.status_code == 201
        assert analysis['source'] == 'TestPostSource'
        assert analysis['title'] == 'Test Post Title'
        assert analysis['best_fit'] == 'linear'
        assert analysis['sinusoidal_correlation'] == 0.3046

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        found_regression = Regression.query.filter_by(
            user_id = found_user_id, 
            source = 'TestPostSource'
        ).first()

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_post_without_key(self, client):
        res = client.post('/api')
        assert res.status_code == 403
        assert b'Key must be provided' in res.data
    
    def test_api_fails_post_unfound_key(self, client):
        res = client.post('/api?key=ABC123')
        assert res.status_code == 401
        assert b'User not authenticated' in res.data

    def test_api_fails_post_without_source(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.post(
            '/api?key=ABC123',
            json = {
                'title': 'Test Post Fails without Source Title',
                'independent': 'Test Post Fails without Source Independent',
                'dependent': 'Test Post Fails without Source Dependent',
                'precision': 4,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        assert res.status_code == 403
        assert b'Source must be provided' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_post_unavailable_source(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
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

        res = client.post(
            '/api?key=ABC123&source=TestPostSourceTaken',
            json = {
                'title': 'Test Post Fails when Source Already Taken Title',
                'independent': 'Test Post Fails when Source Already Taken Independent',
                'dependent': 'Test Post Fails when Source Already Taken Dependent',
                'precision': 4,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        assert res.status_code == 409
        assert b'Source already in use by other collection' in res.data

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_post_decimal_precision(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.post(
            '/api?key=ABC123&source=TestPostFailsDecimalPrecisionSource',
            json = {
                'title': 'Test Post Fails with Decimal Precision Title',
                'independent': 'Test Post Fails with Decimal Precision Independent',
                'dependent': 'Test Post Fails with Decimal Precision Dependent',
                'precision': 4.5,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        assert res.status_code == 403
        assert b'Precision must be a positive integer' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_post_negative_precision(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.post(
            '/api?key=ABC123&source=TestPostFailsNegativePrecisionSource',
            json = {
                'title': 'Test Post Fails with Negative Precision Title',
                'independent': 'Test Post Fails with Negative Precision Independent',
                'dependent': 'Test Post Fails with Negative Precision Dependent',
                'precision': -4,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        assert res.status_code == 403
        assert b'Precision must be a positive integer' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_post_small_set(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.post(
            '/api?key=ABC123&source=TestPostFailsSmallSetSource',
            json = {
                'title': 'Test Post Fails with Small Set Title',
                'independent': 'Test Post Fails with Small Set Independent',
                'dependent': 'Test Post Fails with Small Set Dependent',
                'precision': 4,
                'data_set': [[1, 2], [3, 4], [5, 6]]
            }
        )

        assert res.status_code == 403
        assert b'Data set must contain at least 10 points' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_post_nonlist_set(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.post(
            '/api?key=ABC123&source=TestPostFailsNonlistSetSource',
            json = {
                'title': 'Test Post Fails with Nonlist Set Title',
                'independent': 'Test Post Fails with Nonlist Set Independent',
                'dependent': 'Test Post Fails with Nonlist Set Dependent',
                'precision': 4,
                'data_set': {'first_point': {'x': 1, 'y': 2}, 'second_point': {'x': 3, 'y': 4}}
            }
        )

        assert res.status_code == 403
        assert b'Data set must be a list' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_post_nonlist_points(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.post(
            '/api?key=ABC123&source=TestPostFailsNonlistPointsSource',
            json = {
                'title': 'Test Post Fails with Nonlist Points Title',
                'independent': 'Test Post Fails with Nonlist Points Independent',
                'dependent': 'Test Post Fails with Nonlist Points Dependent',
                'precision': 4,
                'data_set': [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
            }
        )

        assert res.status_code == 403
        assert b'Each coordinate pair within data set must be a list' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_post_long_points(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.post(
            '/api?key=ABC123&source=TestPostFailsLongPointsSource',
            json = {
                'title': 'Test Post Fails with Long Points Title',
                'independent': 'Test Post Fails with Long Points Independent',
                'dependent': 'Test Post Fails with Long Points Dependent',
                'precision': 4,
                'data_set': [[1, 2, 3], [4, 5, 6]]
            }
        )

        assert res.status_code == 403
        assert b'Each coordinate pair within data set must contain exactly 2 numbers' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_post_string_points(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.post(
            '/api?key=ABC123&source=TestPostFailsStringPointsSource',
            json = {
                'title': 'Test Post Fails with String Points Title',
                'independent': 'Test Post Fails with String Points Independent',
                'dependent': 'Test Post Fails with String Points Dependent',
                'precision': 4,
                'data_set': [[1, 2], ['three', 4], [5, 6]]
            }
        )

        assert res.status_code == 403
        assert b'All numbers within coordinate pairs within data set must be integers or floats' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_returns_put(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPutSource',
            title = 'Test Put Title',
            independent = 'Test Put Independent',
            dependent = 'Test Put Dependent',
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
            source = 'TestPutSource'
        ).first()

        res = client.put(
            '/api?key=ABC123&source=TestPutSource',
            json = {
                'title': 'Test Change Put Title',
                'independent': 'Test Change Put Independent',
                'dependent': 'Test Change Put Dependent',
                'precision': 4,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        analysis = json.loads(res.data.decode())

        assert res.status_code == 200
        assert analysis['source'] == 'TestPutSource'
        assert analysis['title'] == 'Test Change Put Title'
        assert analysis['best_fit'] != 'hyperbolic'
        assert analysis['sinusoidal_correlation'] == 0.3046

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()
    
    def test_api_fails_put_without_key(self, client):
        res = client.put('/api')
        assert res.status_code == 403
        assert b'Key must be provided' in res.data
    
    def test_api_fails_put_unfound_key(self, client):
        res = client.put('/api?key=ABC123')
        assert res.status_code == 401
        assert b'User not authenticated' in res.data

    def test_api_fails_put_without_source(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.put(
            '/api?key=ABC123',
            json = {
                'title': 'Test Put Fails without Source Title',
                'independent': 'Test Put Fails without Source Independent',
                'dependent': 'Test Put Fails without Source Dependent',
                'precision': 4,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        assert res.status_code == 403
        assert b'Source must be provided' in res.data

        db.session.delete(found_user)
        db.session.commit()
    
    def test_api_fails_put_unfound_source(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.put(
            '/api?key=ABC123&source=NonexistentSource',
            json = {
                'title': 'Test Put Fails without Source Title',
                'independent': 'Test Put Fails without Source Independent',
                'dependent': 'Test Put Fails without Source Dependent',
                'precision': 4,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        assert res.status_code == 404
        assert b'Data set not found' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_put_decimal_precision(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPutFailsDecimalPrecisionSource',
            title = 'Test Put Fails with Decimal Precision Title',
            independent = 'Test Put Fails with Decimal Precision Independent',
            dependent = 'Test Put Fails with Decimal Precision Dependent',
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
            source = 'TestPutFailsDecimalPrecisionSource'
        ).first()

        res = client.put(
            '/api?key=ABC123&source=TestPutFailsDecimalPrecisionSource',
            json = {
                'title': 'Test Put Fails with Decimal Precision Updated Title',
                'independent': 'Test Put Fails with Decimal Precision Updated Independent',
                'dependent': 'Test Put Fails with Decimal Precision Updated Dependent',
                'precision': 4.5,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        assert res.status_code == 403
        assert b'Precision must be a positive integer' in res.data

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_put_negative_precision(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPutFailsNegativePrecisionSource',
            title = 'Test Put Fails with Negative Precision Title',
            independent = 'Test Put Fails with Negative Precision Independent',
            dependent = 'Test Put Fails with Negative Precision Dependent',
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
            source = 'TestPutFailsNegativePrecisionSource'
        ).first()

        res = client.put(
            '/api?key=ABC123&source=TestPutFailsNegativePrecisionSource',
            json = {
                'title': 'Test Put Fails with Negative Precision Updated Title',
                'independent': 'Test Put Fails with Negative Precision Updated Independent',
                'dependent': 'Test Put Fails with Negative Precision Updated Dependent',
                'precision': -4,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        assert res.status_code == 403
        assert b'Precision must be a positive integer' in res.data

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_put_small_set(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPutFailsSmallSetSource',
            title = 'Test Put Fails with Small Set Title',
            independent = 'Test Put Fails with Small Set Independent',
            dependent = 'Test Put Fails with Small Set Dependent',
            precision = 4,
            data_set = [[1.5, 2.5], [3.5, 4.5], [5.5, 6.5]],
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
            source = 'TestPutFailsSmallSetSource'
        ).first()

        res = client.put(
            '/api?key=ABC123&source=TestPutFailsSmallSetSource',
            json = {
                'title': 'Test Put Fails with Small Set Updated Title',
                'independent': 'Test Put Fails with Small Set Updated Independent',
                'dependent': 'Test Put Fails with Small Set Updated Dependent',
                'precision': 4,
                'data_set': [[1, 2], [3, 4], [5, 6]]
            }
        )

        assert res.status_code == 403
        assert b'Data set must contain at least 10 points' in res.data

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_put_nonlist_set(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPutFailsNonlistSetSource',
            title = 'Test Put Fails with Nonlist Set Title',
            independent = 'Test Put Fails with Nonlist Set Independent',
            dependent = 'Test Put Fails with Nonlist Set Dependent',
            precision = 4,
            data_set = [[1.5, 2.5], [3.5, 4.5], [5.5, 6.5]],
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
            source = 'TestPutFailsNonlistSetSource'
        ).first()

        res = client.put(
            '/api?key=ABC123&source=TestPutFailsNonlistSetSource',
            json = {
                'title': 'Test Put Fails with Nonlist Set Updated Title',
                'independent': 'Test Put Fails with Nonlist Set Updated Independent',
                'dependent': 'Test Put Fails with Nonlist Set Updated Dependent',
                'precision': 4,
                'data_set': {'first_point': {'x': 1, 'y': 2}, 'second_point': {'x': 3, 'y': 4}}
            }
        )

        assert res.status_code == 403
        assert b'Data set must be a list' in res.data

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_put_nonlist_points(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPutFailsNonlistPointsSource',
            title = 'Test Put Fails with Nonlist Points Title',
            independent = 'Test Put Fails with Nonlist Points Independent',
            dependent = 'Test Put Fails with Nonlist Points Dependent',
            precision = 4,
            data_set = [[1.5, 2.5], [3.5, 4.5], [5.5, 6.5]],
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
            source = 'TestPutFailsNonlistPointsSource'
        ).first()

        res = client.put(
            '/api?key=ABC123&source=TestPutFailsNonlistPointsSource',
            json = {
                'title': 'Test Put Fails with Nonlist Points Updated Title',
                'independent': 'Test Put Fails with Nonlist Points Updated Independent',
                'dependent': 'Test Put Fails with Nonlist Points Updated Dependent',
                'precision': 4,
                'data_set': [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
            }
        )

        assert res.status_code == 403
        assert b'Each coordinate pair within data set must be a list' in res.data

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_put_long_points(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPutFailsLongPointsSource',
            title = 'Test Put Fails with Long Points Title',
            independent = 'Test Put Fails with Long Points Independent',
            dependent = 'Test Put Fails with Long Points Dependent',
            precision = 4,
            data_set = [[1.5, 2.5], [3.5, 4.5], [5.5, 6.5]],
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
            source = 'TestPutFailsLongPointsSource'
        ).first()

        res = client.put(
            '/api?key=ABC123&source=TestPutFailsLongPointsSource',
            json = {
                'title': 'Test Put Fails with Long Points Updated Title',
                'independent': 'Test Put Fails with Long Points Updated Independent',
                'dependent': 'Test Put Fails with Long Points Updated Dependent',
                'precision': 4,
                'data_set': [[1, 2, 3], [4, 5, 6]]
            }
        )

        assert res.status_code == 403
        assert b'Each coordinate pair within data set must contain exactly 2 numbers' in res.data

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_put_string_points(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestPutFailsStringPointsSource',
            title = 'Test Put Fails with String Points Title',
            independent = 'Test Put Fails with String Points Independent',
            dependent = 'Test Put Fails with String Points Dependent',
            precision = 4,
            data_set = [[1.5, 2.5], [3.5, 4.5], [5.5, 6.5]],
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
            source = 'TestPutFailsStringPointsSource'
        ).first()

        res = client.put(
            '/api?key=ABC123&source=TestPutFailsStringPointsSource',
            json = {
                'title': 'Test Put Fails with String Points Updated Title',
                'independent': 'Test Put Fails with String Points Updated Independent',
                'dependent': 'Test Put Fails with String Points Updated Dependent',
                'precision': 4,
                'data_set': [[1, 2], ['three', 4], [5, 6]]
            }
        )

        assert res.status_code == 403
        assert b'All numbers within coordinate pairs within data set must be integers or floats' in res.data

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()

    def test_api_returns_delete(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        new_regression = Regression(
            user_id = found_user_id,
            source = 'TestDeleteSource',
            title = 'Test Delete Title',
            independent = 'Test Delete Independent',
            dependent = 'Test Delete Dependent',
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

        res = client.delete(
            '/api?key=ABC123&source=TestDeleteSource'
        )
        
        found_regression = Regression.query.filter_by(
            user_id = found_user_id, 
            source = 'TestDeleteSource'
        ).first()

        assert res.status_code == 204
        assert not found_regression
        
        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_delete_without_key(self, client):
        res = client.delete('/api')
        assert res.status_code == 403
        assert b'Key must be provided' in res.data
    
    def test_api_fails_delete_unfound_key(self, client):
        res = client.delete('/api?key=ABC123')
        assert res.status_code == 401
        assert b'User not authenticated' in res.data

    def test_api_fails_delete_without_source(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.delete(
            '/api?key=ABC123'
        )

        assert res.status_code == 403
        assert b'Source must be provided' in res.data

        db.session.delete(found_user)
        db.session.commit()

    def test_api_fails_delete_unfound_source(self, client):
        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.delete(
            '/api?key=ABC123&source=NonexistentSource'
        )

        assert res.status_code == 404
        assert b'Data set not found' in res.data

        db.session.delete(found_user)
        db.session.commit()