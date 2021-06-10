class TestBaseTemplate:
    def test_base_renders_partials(app, client):
        res = client.get('/')
        assert b'<header>' in res.data
        assert b'<nav class="bar">' in res.data
        assert b'<footer>' in res.data
    
    def test_base_renders_main(app, client):
        res = client.get('/')
        assert b'<main>' in res.data
    
    def test_base_contains_script(app, client):
        res = client.get('/')
        assert b'Render inline LaTeX code' in res.data
    
    def test_base_contains_main_title(app, client):
        res = client.get('/')
        assert b'<title>' in res.data
        assert b'Regressionz' in res.data
    
    def test_base_contains_main_style(app, client):
        res = client.get('/')
        assert b'rel="stylesheet"' in res.data
        assert b'style/main.css' in res.data
    
    def test_base_contains_subheads(app, client):
        res = client.get('/')
        assert b'charset="UTF-8"' in res.data
        assert b'name="viewport"' in res.data
        assert b'name="description"' in res.data
        assert b'property="og:description"' in res.data
        assert b'property="og:title"' in res.data
        assert b'property="og:url"' in res.data
        assert b'property="og:type"' in res.data
        assert b'property="og:image"' in res.data
        assert b'property="twitter:image"' in res.data
        assert b'rel="icon"' in res.data
        assert b'rel="apple-touch-icon"' in res.data

class TestHomeTemplate:
    def test_home(app, client):
        res = client.get('/')
        assert res.status_code == 200

    def test_home_contents(app, client):
        res = client.get('/')
        assert b'<header>' in res.data
        assert b'<footer>' in res.data
        assert b'so much data in our day-to-day lives' in res.data

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