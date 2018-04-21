import pytest


@pytest.fixture
def app():
    from app import create_app
    app = create_app()
    app.testing = True
    return app.test_client()


def test_index(app):
    r = app.get('/')
    assert r.status_code == 200
    assert 'Index' in r.data.decode('utf-8')
