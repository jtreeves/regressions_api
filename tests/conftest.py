import pytest
from app import app as test_app

@pytest.fixture
def app():
    yield test_app

@pytest.fixture
def client(app):
    test_client = app.test_client()
    yield test_client

# ---------- 127 tests PASSED in 2.22s ---------- #