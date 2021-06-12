import pytest
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

        new_regression = Regression(
            user_id = found_user.id,
            source = 'MockSource',
            title = 'Mock Title',
            independent = 'Mock Independent',
            dependent = 'Mock Dependent',
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
            user_id = found_user.id, 
            source = 'MockSource'
        ).first()

        res = client.get(
            '/api?key=ABC123&source=MockSource'
        )

        analysis = json.loads(res.data.decode())

        assert res.status_code == 200
        assert analysis['source'] == 'MockSource'
        assert analysis['title'] == 'Mock Title'
        assert analysis['best_fit'] == 'hyperbolic'
        assert analysis['sinusoidal_correlation'] == 0.5

        db.session.delete(found_regression)
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
            '/api?key=ABC123&source=MySource',
            json = {
                'title': 'Test Title',
                'independent': 'Test Independent',
                'dependent': 'Test Dependent',
                'precision': 4,
                'data_set': [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
            }
        )

        analysis = json.loads(res.data.decode())

        assert res.status_code == 201
        assert analysis['source'] == 'MySource'
        assert analysis['title'] == 'Test Title'
        assert analysis['best_fit'] == 'linear'
        assert analysis['sinusoidal_correlation'] == 0.3046

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_regression = Regression.query.filter_by(
            user_id = found_user.id, 
            source = 'MySource'
        ).first()

        db.session.delete(found_regression)
        db.session.delete(found_user)
        db.session.commit()