# TODO: Feature 1
# TODO: Feature 1
from flask.testing import FlaskClient
from app import movie_repository

def test_create_all_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data
    assert b'<h1 class="mb-5">All Movies</h1>' in response_data

def test_movies_form(test_app: FlaskClient):
    movie_repository.create_movie('Star Wars', 'George Lucas', 1)

    response = test_app.get('/movies')
    response_data = response.data

    assert b'<th>Star Wars</th>' in response_data
