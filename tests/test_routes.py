import pytest

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

class TestSignupRoute:
    pass

class TestImagesRoute:
    pass

class TestAPIRoute:
    pass