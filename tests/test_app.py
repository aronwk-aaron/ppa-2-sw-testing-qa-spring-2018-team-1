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
