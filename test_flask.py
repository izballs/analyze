import pytest
from analyze import  create_app


@pytest.fixture
def app():
    app = create_app()
    return app

def test_app(client):
    assert client.post('/analyze', data=dict(text='hello 2 times  '), follow_redirects=True)
