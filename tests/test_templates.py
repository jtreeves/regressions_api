class TestBaseTemplate:
    pass

class TestHomeTemplate:
    def test_home(app, client):
        res = client.get('/')
        assert res.status_code == 200

    def test_home_contents(app, client):
        res = client.get('/')
        assert b"<header>" in res.data
        assert b"<footer>" in res.data
        assert b"so much data in our day-to-day lives" in res.data

class TestAboutTemplate:
    def test_about(app, client):
        res = client.get('/about')
        assert res.status_code == 200

class TestUsageTemplate:
    def test_usage(app, client):
        res = client.get('/usage')
        assert res.status_code == 200

class TestMathTemplate:
    def test_math(app, client):
        res = client.get('/math')
        assert res.status_code == 200

class TestSignupTemplate:
    pass