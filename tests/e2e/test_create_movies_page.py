# TODO: Feature 2
from flask.testing import FlaskClient


def test_create_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/new')
    response_data = response.data
    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response_data
    assert b'<p class="mb-3">Create a movie rating below</p>' in response_data

def test_create_movies_form(test_app: FlaskClient):
    response = test_app.post('/movies', data={
        "name": "Star Wars",
        "dname": "George Lucas",
        "select": "5"})
    response_data = response.data
    assert b'<h1 class="mb-5">All Movies</h1>' in response_data

def test_create_movies_bad(test_app:FlaskClient):
    response = test_app.post('/movies', data={
        "name": "",
        "dname": "George Lucas",
        "select": 5,})
    response_data = response.data

    assert b'<div class="text-bg-danger p-3">Wrong input provided.</div>' in response_data
