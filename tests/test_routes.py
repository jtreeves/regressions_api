import pytest
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
    pass