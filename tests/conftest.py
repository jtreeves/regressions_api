import pytest
from app import app as test_app
from app import db as test_db

@pytest.fixture
def app():
    yield test_app

@pytest.fixture
def db():
    yield test_db

@pytest.fixture
def client(app, db):
    test_client = app.test_client()
    yield test_client

# ---------- 28 tests PASSED in 0.66s ---------- #