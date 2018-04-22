import pytest


@pytest.fixture
def app():
    from app import create_app
    config = 'dev'
    app = create_app(config_name=config)
    app.testing = True
    return app.test_client()


# test for Index
def test_index(app):
    r = app.get('/')
    assert r.status_code == 200
    assert 'Index' in r.data.decode('utf-8')


def test_bad_page(app):
    r = app.get('/bad_page')
    assert r.status_code == 404


# Tests for Distnace
def test_dist_no_input(app):
    r = app.get('/distance')
    assert r.status_code == 200
    assert 'Shortest Distance Calculator' in r.data.decode('utf-8')


def test_dist_input(app):
    r = app.post('/distance', data={
        'x1': '0',
        'y1': '0',
        'x2': '5',
        'y2': '5'})
    assert r.status_code == 200
    assert '7.0711' in r.data.decode('utf-8')


def test_dist_invalid(app):
    r = app.post('/distance', data={
            'x1': 'dflbvg',
            'y1': 'no',
            'x2': '5',
            'y2': '5'})
    assert r.status_code == 200
    assert 'Invalid Input' in r.data.decode('utf-8')
